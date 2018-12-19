import tkinter as tk
from simulation import Simulation
import random


class View(tk.Frame):
    """
    The ugly but simple gui that the user is presented with when starting
    the program.
    """
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.name = ""
        self.size = 0
        self.surv_temp = 0
        self.my_allergies = True
        self.others_allergies = True
        self.eater_type = "Herbivore"
        self.delete_choice = ""
        self.weather_choice = 0
        self.sim = Simulation()
        self.textwidg = tk.Text(self, width=40, height=7)
        self.textwidg.insert(tk.END, self.main_window())
        self.textwidg.grid(row=1, column=0, rowspan=6, columnspan=3, sticky=tk.N)
        
        label = tk.Label(self, text="Welcome to a Evolution-simulation!")
        label.grid(row=0, column=0, sticky=tk.N)
        button = tk.Button(self, text="Create new species", command= self.create_new_species)
        button.grid(row=7,column=0)
        button2 = tk.Button(self, text="Delete existing species", command= self.delete_window)
        button2.grid(row=8,column=0)
        button3 = tk.Button(self, text="Change climate", command=self.change_climate)
        button3.grid(row=9,column=0)
        button4 = tk.Button(self, text="Start simulation", command=self.sim.start_simulation)
        button4.grid(row=10,column=0)
    
    
    def create_new_species(self):
        """
        Window that pops up when the "Create new species"-button is pushed. In this window
        the user can create a new species of both herbivore and carnivore. It
        has a lot of private functions in it, that can't be used outside the methos or
        the class.
        """
        
        frame2 = tk.Toplevel(self)
        label1 = tk.Label(frame2, text="Welcome to making your own species! Choice your animals attribute below")
        label1.grid(row=0, column=0, columnspan=1, sticky=tk.N)
        
        def key(event):
            """
            Takes care of key-events.
            """
            
            if event.widget == entry1:
                self.name = entry1.get()
            if event.widget == entry2:
                self.size = entry2.get()
            if event.widget == entry3:
                self.surv_temp = entry3.get()

        label2 = tk.Label(frame2, text="Name of species")
        label2.grid(row=1, column=0, columnspan=1, sticky=tk.NW)

        entry1 = tk.Entry(frame2)
        entry1.bind("<KeyRelease>", key)
        entry1.grid(row=2, column=0, columnspan=1, sticky=tk.NW)

        label3 = tk.Label(frame2, text="Size (write a number between 1-3000)")
        label3.grid(row=1, column=1, columnspan=1, sticky=tk.NW)

        entry2 = tk.Entry(frame2)
        entry2.bind("<KeyRelease>", key)
        entry2.grid(row=2, column=1, columnspan=1, sticky=tk.NW)

        label7 = tk.Label(frame2, text="What temprature can it survive in? (write a number between -20 to 40")
        label7.grid(row=3, column=0, columnspan=1, sticky=tk.NW)

        entry3 = tk.Entry(frame2)
        entry3.bind("<KeyRelease>", key)
        entry3.grid(row=4, column=0, columnspan=1, sticky=tk.NW)
        

        def _get_allergy():
            """
            Returns "bird" if the user want their species to have allergies, which will
            make the species allergic to animals whom's meat type is of bird. If the user
            don't want the species to have this weakness, it returns "nothing".
            """

            if self.my_allergies == True:
                return "bird"
            else:
                return "nothing"
        allergy = property(_get_allergy)

        label5 = tk.Label(frame2, text="Do you want your species to have allergies?")
        label6 = tk.Label(frame2, text="(only relevant if you choosen Carnivore. if not press No)")
        label5.grid(row=5, column=0, sticky=tk.NW)
        label6.grid(row=6, column=0, sticky=tk.NW)

        radio_value = tk.StringVar()
        radio_value2 = tk.StringVar()
        radio_value.set('Yes')
        radio_value2.set('Yes')


        def radio():
            """
            Writes out the value of the radio-buttons.
            """
            
            if radio_value.get() == "Yes":
                self.my_allergies = True
        
            if radio_value.get() == "No":
                self.my_allergies = False


        def radio2():
            """
            Also writes out the value of radio-button but on  a different question.
            """
            
            if radio_value2.get() == "Yes":
                self.my_allergies = True
        
            if radio_value2.get() == "No":
                self.my_allergies = False
        
        radio_button1 = tk.Radiobutton(frame2, text="Yes",
                                       variable=radio_value,
                                       value="Yes",command=radio)
        radio_button1.grid(row=7, column=0, sticky=tk.W)


        radio_button2 = tk.Radiobutton(frame2, text="No",
                                       variable=radio_value,
                                       value="No",
                                       command=radio)
        radio_button2.grid(row=7, column=1, sticky=tk.W)
        radio_button1.select()
        radio_button2.deselect()
                          

        def _get_otherallergies():
            """
            Returns "bird" if the user want other species to have allergies on their
            new species, which will make their meat type "bird" when the species is created.
            """

            if self.others_allergies == True:
                return "bird"
            else:
                return "meat"
        otherallergies = property(_get_otherallergies)

        
        label6 = tk.Label(frame2, text="Do you want other species to have allergies against you? (not everone will, but some)")
        label6.grid(row=8, column=0)
        radio_button3 = tk.Radiobutton(frame2, text="Yes",
                                       variable=radio_value2,
                                       value="Yes",command=radio2)
        radio_button3.grid(row=9, column=0, sticky=tk.W)
        
        radio_button4 = tk.Radiobutton(frame2, text="No",
                                       variable=radio_value2,
                                       value="No",
                                       command=radio2)
        radio_button4.grid(row=10, column=1, sticky=tk.W)         


        def herb_or_carn(event):
            """
            Sets the eater_type-attribute into herbivore or carnivore, depending on
            what the user has chosen.
            """
            
            self.eater_type = option_variable.get()

        label4 = tk.Label(frame2, text="What kind of eater?")
        label4.grid(row=3, column=1, columnspan=1, sticky=tk.NW)

        option_variable = tk.StringVar(frame2)
        option_variable.set("Herbivore") 
        option = tk.OptionMenu(frame2, option_variable,"Herbivore", "Carnivore", command=herb_or_carn)
        option.grid(row=4, column=1, columnspan=1, sticky=tk.NW)


        def error_window(error_string):
            """
            Prints out an error message-window if the user written wrong somewhere
            when creating the species.
            """
            
            frajm = tk.Toplevel()
            label1 = tk.Label(frajm, text="Error message")
            label1.pack()
            label2 =  tk.Label(frajm, text=error_string)
            label2.pack()
            
            
        def try_to_close_window():
            """
            Checks if the user has written right evertwhere or if it needs to send out
            an error-message. If not, it goes to the method that creates the new species.
            """
            
            def error_window():
                error_string = ""
                try:
                    int(self.size)
                    if int(self.size) > 3000:
                        error_string += "The size of the creature is to large \n"
                    if int(self.size) < 1:
                        error_string += "The size of the creature is to small \n"
                except:
                    error_string += "Please write a number in size \n"
                try:
                    int(self.surv_temp)
                    if int(self.surv_temp) > 40:
                        error_string += "Please write a smaller number in survival temprature \n"
                    if int(self.surv_temp) < -20:
                        error_string += "Please write a larger number in survival temprature \n"
                except:
                    error_string += "Please write a number in survival temprature \n"
                if error_string != "":
                    error_window(error_string)
                else:
                    close_window()


        def close_window():
            """
            Creates new species from the user's choices and then closes
            the window.
            """
            
            if self.eater_type == "Carnivore":
                self.sim.user_create_carnivore(self.name,
                                                self.others_allergies,
                                                self.eater_type,
                                                self.size,
                                                1,
                                                self.my_allergies,
                                                self.surv_temp)
            elif self.eater_type == "Herbivore":
                self.sim.user_create_herbivore(self.name,
                                                self.others_allergies,
                                                self.eater_type,
                                                self.size,
                                                1,
                                                self.my_allergies,
                                                self.surv_temp)


            def yes_on_saving_to_file():
                lst = ""
                file = open("myspecies.txt", "w")
                allergy = str(_get_allergy())

                lst += ("\n"+ "Species: "+str(self.name)
                        +"size: " + str(self.size)
                        +". \n"+ "Type of eater: "
                        + str(self.eater_type())
                        +". \n"+ "Survival temprature: "
                        +str(self.surv_temp())
                        +"Allergies: " + str(allergy))
                file.write(lst)
                file.close()

            question_frame = tk.Toplevel()
            question_label = tk.Label(question_frame, text="Do you want to save your new species into a file?")
            question_label.pack()
            yesbutton = tk.Button(question_frame, text="Yes", command=yes_on_saving_to_file)
            yesbutton.pack()
            nobutton = tk.Button(question_frame, text="No", command=close_window)
            nobutton.pack()
            self.update_window()
            frame2.destroy()


        def reset_changes():
            """
            Resets eveything and closes the window.
            """
            
            self.name = ""
            self.size = 0
            self.surv_temp = 0
            self.my_allergies = True
            self.others_allergies = True
            self.eater_type = ""
            close_window()

        button3 =  tk.Button(frame2, text="return without saving", command=reset_changes)
        button4 =  tk.Button(frame2, text="Save and return", command=try_to_close_window)
        button3.grid(row=11, column=0)
        button4.grid(row=11, column=1)


    #=============Delete species=================

    def delete_window(self):
        """
        A method that opens up a new window that pops up when the user push "Delete existing
        species". This method has a lot of private functions that can't be used outside of
        this method.
        """
        
        frame3 = tk.Toplevel(self)
        textwidg2 = tk.Text(frame3, width=80, height=25)
        
        def info():
            spec = ""
            for species in self.sim.grass_eaters:
                if species.species not in spec:
                    spec += ("\n"+ "Species: "+str(species.get_species())
                             +". \n"+ "Type of eater: "
                             + str(species.get_eater_type())
                             +". \n"+ "Survival temprature: "
                             +str(species.get_survival_temprature())
                             +". \n"+"DNA:" + str(species.get_dna())
                             + "\n")

            lst = ""
            for species in self.sim.meat_eaters:
                if species.species not in lst:
                    lst += ("\n"+ "Species: "+str(species.get_species())
                            +". \n"+ "Type of eater: "
                            + str(species.get_eater_type())
                            +". \n"+ "Survival temprature: "
                            +str(species.get_survival_temprature())
                            +". \n"+"DNA:" + str(species.get_dna()[0].get_species())
                            + "\n")
            infos = ("Press on the screen and scroll down to read the information about the species " +
                    "of this simulation. You can only delete one species at a time." +
                    " The animals in this world are: " + str(spec)+ str(lst))
            return infos
        
        textwidg2.insert(tk.END, info())
        textwidg2.grid(row=0, column=0, rowspan=6, columnspan=3, sticky=tk.N)


        def delete_instanses(event):
            """
            Deletes species from the simulation. Only one specie at a time can be deleted.
            """
            
            self.delete_choice = option_variable3.get()
       
                    
        def close_window():
            """
            The user's action to delete a species is performed and the main
            window gets updates with how many species there are in the world.
            Then it closes the "Delete existing species"-window.
            """
            self.sim.grass_eaters[:] = [species for species in self.sim.grass_eaters if species.get_species() != self.delete_choice]
            self.sim.meat_eaters[:] = [species for species in self.sim.meat_eaters if species.get_species() != self.delete_choice]            
            
            self.update_window()
            frame3.destroy()

        def reset_choice():
            """
            Doesn't save the changes if the user realises that the choices that was
           made was wrong"""
            
            self.delete_choice = ""
            close_window()
            

        label7 = tk.Label(frame3, text="What species do you want to delete from the simulation?")
        label7.grid(row=7, column=0, sticky=tk.N)

        option_variable3 = tk.StringVar(frame3)
        option_variable3.set("Option") 
        option = tk.OptionMenu(frame3, option_variable3, "goat","ostrich", "walking shark", "lama", "kangaroo", "wombat",
                               "black bird", "lion", "snake","penguin", self.name,command=delete_instanses)
        option.grid(row=8, column=0)

        button3 =  tk.Button(frame3, text="Return without saving", command=reset_choice)
        button4 =  tk.Button(frame3, text="Save and return", command=close_window)
        button3.grid(row=9, column=0)
        button4.grid(row=9, column=1)


    #===============Change climate==============

    def change_climate(self):
        """
        Opens up a new window where the user can change the climate from the administration
        class "Simulation".
        """
        
        frame4 = tk.Toplevel(self)
        textwidg = tk.Text(frame4, width=70, height=7)

        textwidg.insert(tk.END, "Welcome! Not all animals can survive in every climate,and here you have the chance to change it to your preference. You won't know until after the simulation has started what animals can survive what. It's all put into chance.")
        textwidg.grid(row=0, column=0, rowspan=6, columnspan=3, sticky=tk.N)

        def choice(event):
            """
            Randomizes a temprature from the span that the user has decided on.
            """
            
            choice = option_variable3.get()
            if choice == "Snowstorm(-20 to -15 degrees)":
                self.weather_choice = random.randint(-20, -15)
            elif choice == "Summer in Alaska(-15 to -5 degrees)":
                self.weather_choice = random.randint(-15, -5)
            elif choice == "Swedish pissweather(-5 to 5 degrees)":
                self.weather_choice = random.randint(-5, 5)
            elif choice == "Can't believe it's not summer (5-15 degrees)":
                self.weather_choice = random.randint(5, 15)
            elif choice == "bikini-weather (15-25 degrees)":
                self.weather_choice = random.randint(15, 25)
            elif choice == "Not even gonna bother with a bikini (25-30 degrees)":
                self.weather_choice = random.randint(25, 30)
            elif choice == "Feeeel the bern (30 to 40 degrees)":
                self.weather_choice = random.randint(30, 40)


        def close_window():
            """
            Changes the temprature and closes the window.
            """
            
            self.sim.set_weather(self.weather_choice)
            self.update_window()
            frame4.destroy()


        def delete_choice():
            """
            Resets the temprature and closes the window.
            """
            
            self.weather_choice = self.sim.get_weather()
            frame4.destroy()

        option_variable3 = tk.StringVar(frame4)
        option_variable3.set("Option meny") 
        option = tk.OptionMenu(frame4, option_variable3, "Snowstorm(-20 to -15 degrees)",
                               "Summer in Alaska(-15 to -5 degrees)",
                               "Swedish pissweather(-5 to 5 degrees)",
                               "Can't believe it's not summer (5-15 degrees)",
                               "bikini-weather (15-25 degrees)",
                               "Not even gonna bother with a bikini (25-30 degrees)",
                               "Feeeel the bern (30 to 40 degrees)", command=choice)
        option.grid(row=7, column=1)

        button3 =  tk.Button(frame4, text="Return without saving", command=delete_choice)
        button4 =  tk.Button(frame4, text="save and return", command=close_window)
        button3.grid(row=8, column=0)
        button4.grid(row=8, column=1)


    def update_window(self):
        """Updates the main window"""
        
        self.textwidg.delete('1.0', tk.END)
        self.textwidg.insert(tk.END, self.main_window2())
        

    def main_window(self):
        """
        Generates and return information about the creatures in the 
        simulation to the main window that pops up when the program starts.
        """
        self.sim.randomize_weather()
        self.sim.import_plant_lst()
        self.sim.import_animal_lst()
        self.sim.startup()
        
        info = ("There are " + str(self.sim.get_animal_count()) +
                " creatures in the world right now of different species." +
                " The temprature is " + str(self.sim.get_weather()) + "." +
                " Do you like the chances or do you want to change anything?")

        return info


    def main_window2(self):
        """
        Updates window with new information without generating it all again.
        """

        info = (" There are " + str(self.sim.get_animal_count()) +
                " creatures in the world right now of different species." +
                " The temprature is " + str(self.sim.get_weather()) + "." +
                " Do you like the chances or do you want to change anything?")

        return info
