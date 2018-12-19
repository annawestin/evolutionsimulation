from gui import *

class Save_to_file(tk.Frame):
    """
    Saves the data of the simulation into a file.
    """
    #Under development
    
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.gui = View()
        #question_frame = tk.Toplevel()
        question_label = tk.Label(self, text="Do you want to save your new species into a file?")
        question_label.pack()
        yesbutton = tk.Button(self, text="Yes", command=self.yes_on_saving_to_file)
        yesbutton.pack()
        nobutton = tk.Button(self, text="No", command=self.close_window)
        nobutton.pack()

    def yes_on_saving_to_file(self):
        lst = ""
        file = open("myspecies.txt", "w")
        #allergy = str(_get_allergy())

        lst += ("\n"+ "Species: "+str(self.gui.name)+"size: " + str(self.gui.size)
                +". \n"+ "Type of eater: "+ str(self.gui.eater_type())
                +". \n"+ "Survival temprature: ")
                #+str(self.self.gui.surv_temp()))
                #+"Allergies: " + str(allergy))
        file.write(lst)
        file.close()
        self.close.window()

    def close_window(self):
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    main = Save_to_file(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
