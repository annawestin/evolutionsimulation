from herbivore import Herbivore
from carnivore import Carnivore
from animal_factory import Factory
import random


CORNER_UP_R = "╮" 
SIDE_H = "─" 
CORNER_DOWN_L = "╰"
CORNER_DOWN_R = "╯"
SIDE_L = "│"
TABLE_WIDTH = 80
COLUMN_SPEC = 25
COLUMN_GEN = 10
COLUMN_EV = 45 
TABLE_TOP = "╭" + "─"*(TABLE_WIDTH) + "╮" + "\n"
TABLE_BOTTOM = "╰" + "─"*(TABLE_WIDTH) + "╯"
        

class Simulation(object):
    """
    Decides on the events and conditions of the simulation.
    """
    
    def __init__(self):
        self.plant_lst = []
        self.temporary_herbivore_lst = []
        self.temporary_carnivore_lst = []
        self.meat_eaters = []
        self.grass_eaters = []
        self.chance = 0
        self.herb_fac = Factory(self.plant_lst, Herbivore, 8,
                                self.temporary_herbivore_lst)
        
        self.carn_fac = Factory(self.grass_eaters, Carnivore, 1,
                                self.temporary_carnivore_lst)
        self.weather = 0

    def randomize_weather(self):
        """
        Randomize weather for the simulation.
        """
        
        self.weather = random.randint(-20,40)
        return self.weather


    def get_weather(self):
        return self.weather


    def set_weather(self, weather):
        self.weather = weather

        
    def user_create_herbivore(self, species, food_type, eater_type, size, generation,
                              allergy,survival_temprature):
        """
        A method that is only used by the View-class (the GUI-class).
        Creates the user's species for herbivores.
        """
        
        self.grass_eaters.extend(self.herb_fac.user_creatures(species,
                                                              food_type,
                                                              eater_type,
                                                              size, generation,
                                                              allergy,
                                                              survival_temprature))
        return self.grass_eaters


    def user_create_carnivore(self, species, food_type, eater_type, size, generation,
                              allergy,survival_temprature):
        """
        A method that is only used by the GUI-class. Creates the
        user's species for carnivore.
        """
        
        self.meat_eaters.extend(self.carn_fac.user_creatures(species,
                                                             food_type,
                                                             eater_type,
                                                             size, generation,
                                                             allergy,
                                                             survival_temprature))
        return self.meat_eaters
        

    def get_animal_count(self):
        """
        Puts the two lists of herbivores and carnivores together into one
        and generates the lenght of that list, which will show how many
        animals there are in the simulation.
        """

        return len(self.grass_eaters) + len(self.meat_eaters)
    

    def import_animal_lst(self):
        """
        Imports lines of animals and their attribute from a text file.
        """ 
        
        file = open("../data/animals.txt", "r")
        for line in file.readlines():
            if "herbivore" in line:
                self.temporary_herbivore_lst.append(line.strip().split(","))
            else:
                self.temporary_carnivore_lst.append(line.strip().split(","))


    def import_plant_lst(self):
        """
        Imports from a textfile.
        """
        
        file = open("../data/plants.txt", "r")
        for line in file.readlines():
            self.plant_lst.append(line.strip().strip(","))


    def the_purge(self):
        """
        Kills all the species that can't survive the climate.
        """
        
        for animal in self.meat_eaters:
            if int(animal.survival_temprature) < int(self.weather):
                print("The species", animal.species,
                      "did not survive this climate.")
                self.meat_eaters.remove(animal)

        for animals in self.grass_eaters:
            if int(animal.survival_temprature) < int(self.weather):
                print("The species", animals.species,
                      "did not survive this climate.")
                self.grass_eaters.remove(animals)


    def feeding(self):
        """
        All the animals feed. Some might die from poison or allergy.
        """

        for animal in self.grass_eaters:
            if animal.ate_poison() == True:
                self.grass_eaters.remove(animal)
                    
        for animal in self.meat_eaters:
            if animal.had_allergy_attack() == True:
                self.meat_eaters.remove(animal)
                        
        i = 0
        while i < len(self.meat_eaters):
            for food in self.meat_eaters[i].get_dna():
                if self.meat_eaters[i].feeding(food) == True:
                    try:
                        print(food.get_species(), "from generation",
                              food.get_generation(),
                              "got eaten by a", self.meat_eaters[i].get_species())
                        self.grass_eaters.remove(herbivore)
                    except:
                        pass
                elif food == None:
                    self.meat_eaters.remove(carnivore)
                i += 1
                  

    def babymaking(self):
        """ 
        The species make babies by first chunking the two lists 
        of animals so they become a pair of two. The herbivore 
        and carnivore makes babies in very different ways.
        The herbivores babies inherit their parents dna, while 
        the carnivores does not. This is because the carnivore's dna 
        need to have the list of the new herbivores (their food) from 
        the new generation and not the old one.
        """
        
        chunks_meat = [self.meat_eaters[x:x+2] for x in range(0, len(self.meat_eaters), 2)]
        chunks_grass = [self.grass_eaters[x:x+2] for x in range(0, len(self.grass_eaters), 2)]

        new_meat = []
        new_grass = []

        for a in chunks_grass:
            try:
                if len(a) != 1 and a[0].species == a[1].species:
                    new_grass += self.herb_fac.crossover(a[0], a[1])
                    new_grass.append(self.herb_fac.mutation(a[0]))
            except:
                print("The", a[0].species, "seem to get extinct in generation",
                      a[0].generation, "cause some could not make babies")

        self.grass_eaters = new_grass
        self.carn_fac.valid_dna_symbols = self.grass_eaters

        for b in chunks_meat:
            try:
                if len(b) != 1 and b[0].species == b[1].species:
                    for i in range(3):
                        new_meat.append(self.carn_fac.create_creatures(b[0]))
            except:
                print("The", b[0].species, "seem to get extinct in generation",
                      b[0].generation, "cause some could not make babies")

        self.meat_eaters = new_meat


    def print_table(self, world_specie, generation, event):
        """ 
        Prints a table with the result of the simulation.
        """
        #This method is still under development and and is not yet used. 
        
        table = (TABLE_TOP
                 + SIDE_L + self.pad_to_length(COLUMN_SPEC, "Species")
                 + self.pad_to_length(COLUMN_GEN, "Generation")
                 + self.pad_to_length(COLUMN_EV, "event") + "\n"
                 + SIDE_L + self.pad_to_length(COLUMN_SPEC, world_specie) 
                 + self.pad_to_length(COLUMN_GEN, str(generation)) 
                 + self.pad_to_length(COLUMN_EV, event)
                 + "\n" + TABLE_BOTTOM)
        return table
               

    def pad_to_length(self, column, word): 
        """ Adapts the lenght of a table.
        """
        
        lenght = column-len(word)
        return word + (" " * lenght) + SIDE_L
    
    
    def startup(self):
        """
        Uses the method "Create creatues for first tribe" from Factory, which
        creates creatures from the imported list. This method is called "Startup"
        because it's a method that is used in the View-class before the little
        start window opens.
        """
        
        self.grass_eaters.extend(self.herb_fac.create_creature_for_first_tribe())
        self.meat_eaters.extend(self.carn_fac.create_creature_for_first_tribe())


    def start_simulation(self):
        """
        A method that starts the whole simulation. After feeding there is a "second purge"
        that will end the simulation if any of the animal lists are too short, or kill
        off species that hasn't been able to make babies a couple of times.
        """
        
        self.the_purge()

        world = True
        while world == True:
            
            if len(self.grass_eaters) == 0 and len(self.meat_eaters) == 0:
                print("All the animals are dead. Simulation has ended")
                break

            else:
                    
                self.feeding()


                self.grass_eaters.sort(key=lambda grass: grass.species)
                if len(self.grass_eaters) == 1:
                    print("Only one poor", self.grass_eaters[0].species, "is left.")
            
                try:
                    if self.grass_eaters[0].species == self.grass_eaters[-1].species:
                        print("The", self.grass_eaters[0].species, "has taken over the earth")
                        print("Simulation has ended")
                        break
                except:
                    pass
                    
                self.meat_eaters.sort(key=lambda meat: meat.species)
                if len(self.meat_eaters) == 1:
                    print("Only one poor", self.meat_eaters[0].species, "is left.")

                try:
                    if self.meat_eaters[0].species == self.meat_eaters[-1].species:
                        print("The", self.meat_eaters[0].species, "has taken over the earth")
                        print("Simulation has ended")
                        break
                except:
                    pass

                    
                if len(self.meat_eaters) == 0:
                    print("All the carnivores has died out and now the world are only populated by herbivores")
                    break

                if len(self.grass_eaters) == 0:
                    print("All the food for carnivore are dead.")
                    print("Simulation has ended")
                    break

                self.babymaking()
                      


