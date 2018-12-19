from animal import Animal

class Herbivore(Animal):
    """
    Every instance of this class is a grass eating animal.
    """
    
    def __init__(self, species, type_of_food, type_of_eater, size,
                 generation, allergies, survival_temprature,
                 dna_symbols):

        super().__init__(species, type_of_food, type_of_eater, size,
                         generation, allergies, survival_temprature,
                         dna_symbols)
        self.lst_of_herbivore = []
        self.allergy = allergies
        self.dna = dna_symbols
        self.species = species
        self.food_type = type_of_food
        self.eater_type = type_of_eater
        self.size = int(size)
        self.generation = int(generation)
        self.survival_temprature = int(survival_temprature)
        self.dna_length = 8


    def ate_poison(self):
        """
        Deletes the animal from the simulation if it has eaten poison.
        """
        for food in self.get_dna():
            i = food.split(",")
            if "poison" in food:
                print(self.get_species(), "from generation", self.get_generation(),
                      "died from poison after eating", i[0])
                return (True)
