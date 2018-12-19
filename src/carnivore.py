from animal import Animal
import random

class Carnivore(Animal):
    """
    Every instance of this class is a meat-eating animal.
    """
    
    def __init__(self, species, type_of_food, type_of_eater, size,
                 generation, allergies, survival_temprature,
                 dna_symbols, value=0):
        super().__init__(species, type_of_food, type_of_eater, size,
                         generation, allergies, survival_temprature,
                         dna_symbols)
        lst_of_carnivore = []
        self.allergy = allergies
        self.dna = dna_symbols
        self.species = species
        self.food_type = type_of_food
        self.eater_type = type_of_eater
        self.size = int(size)
        self.generation = int(generation)
        self.survival_temprature = int(survival_temprature)
        self.dna_length = 1

    def had_allergy_attack(self):
        """
        Deletes the animal from the simulation if it has eaten something
        that the species is allergic to.
        """
        
        for food in self.get_dna():
            if self.allergy == food.food_type:
                    print(self.get_species(), "from generation",
                          self.get_generation(),"died from allergy after eating",
                          food.get_species())
                    return(True)
                    

    def feeding(self, food):
        if food.get_size() < self.get_size():
            return (True) 
