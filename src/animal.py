class Animal(object):
    """
    Animal.
    """
    
    def __init__(self, species, type_of_food, type_of_eater, size_str,
                 generation_str, allergies, survival_temprature_str,
                 dna_symbols):
        self.allergy = allergies
        self.dna = dna_symbols
        self.species = species
        self.food_type = type_of_food
        self.eater_type = type_of_eater
        self.size = int(size_str) 
        self.generation = int(generation_str)
        self.survival_temprature = int(survival_temprature_str)

    def get_allergy(self):
        return self.allergy

    def get_dna(self):
        return self.dna

    def get_species(self):
        return self.species

    def get_food_type(self):
        return self.food_type

    def get_eater_type(self):
        return self.eater_type

    def get_size(self):
        return self.size

    def get_generation(self):
        return self.generation

    def get_survival_temprature(self):
        return self.survival_temprature
