import random

class Factory(object):
    """
    Factory where the animals are made.
    """
    
    def __init__(self, dna_symbols, ind_class, dna_length, animal_lst=[]):
        self.valid_dna_symbols = dna_symbols
        self.ind_class = ind_class
        self.instance_lst = animal_lst
        self.dna_length = dna_length
        self.animal = []

    def get_dna(self):
        return self.valid_dna_symbols


    def create_creature_for_first_tribe(self):
        """
        Takes arguments from a list and creates up to four
        instances depending on if they're "lucky" enought 
        to get born.
        """
        
        for instance_lst in self.instance_lst:
            
            survival_tempratures = random.randint(-20,40)

            dna = []
            for i in range(self.dna_length):
                dna.append(random.choice(self.get_dna()))

            chance = random.randint(0,10)

            if chance < 4:
                self.animal.append(self.ind_class(instance_lst[0],
                                                   instance_lst[1],
                                                   instance_lst[2],
                                                   int(instance_lst[3]),
                                                   int(instance_lst[4]),
                                                   instance_lst[5],
                                                   survival_tempratures,
                                                   dna))
            if chance < 7:
                self.animal.append(self.ind_class(instance_lst[0],
                                                   instance_lst[1],
                                                   instance_lst[2],
                                                   int(instance_lst[3]),
                                                   int(instance_lst[4]),
                                                   instance_lst[5],
                                                   survival_tempratures,
                                                   dna))
            
                self.animal.append(self.ind_class(instance_lst[0],
                                                   instance_lst[1],
                                                   instance_lst[2],
                                                   int(instance_lst[3]),
                                                   int(instance_lst[4]),
                                                   instance_lst[5],
                                                   survival_tempratures,
                                                   dna))
            if chance < 11:
                self.animal.append(self.ind_class(instance_lst[0],
                                                   instance_lst[1],
                                                   instance_lst[2],
                                                   int(instance_lst[3]),
                                                   int(instance_lst[4]),
                                                   instance_lst[5],
                                                   survival_tempratures,
                                                   dna))

        
        return self.animal
    

    def user_creatures(self, species, food_type, eater_type, size, generation,
                       allergy,survival_temprature):
        """
        Creates two instances with attributes that the user himself 
        has decided on. 
        """
        
        dna = []
        for index in range(self.dna_length):
            dna.append(random.choice(self.valid_dna_symbols))
        instance = self.ind_class(species, food_type, eater_type,
                                  size,generation,allergy,
                                  survival_temprature,dna)

        dna2 = []
        for index in range(self.dna_length):
            dna2.append(random.choice(self.get_dna()))
        instance2 = self.ind_class(species, food_type, eater_type,
                                  size,generation,allergy,
                                  survival_temprature,dna2)
        
        instances = [instance, instance2]
        return instances
    

    def create_creatures(self, p1):
        """
        Create creatures for the new generations.
        """
        dna = []
        for index in range(self.dna_length):
            dna.append(random.choice(self.valid_dna_symbols))
        instance = self.ind_class(p1.get_species(), p1.get_food_type(), p1.get_eater_type(),
                                  p1.get_size(),p1.get_generation()+1,
                                  p1.get_allergy(),p1.get_survival_temprature(),
                                  dna)
        return instance


    def crossover(self, p1, p2):
        """ 
        Mixes the "DNA" of the parents to create two babies.
        """
        
        mom = p1
        dad = p2

        #dominant mom:
        split_mom = random.randint(3, 7)
        moms_dna = mom.get_dna()[:split_mom]
        dads_dna = dad.get_dna()[split_mom:]
        new_dna = moms_dna + dads_dna
        new_dna2 = dads_dna + moms_dna
        baby1 = self.ind_class(mom.get_species(),mom.get_food_type(),
                                mom.get_eater_type(), mom.get_size(),
                                mom.get_generation()+1,
                                mom.get_allergy(),
                                mom.get_survival_temprature(), new_dna)
        
        #dominant dad:
        spliter = random.randint(2,8)
        moms_dna = mom.get_dna()[spliter:]
        dads_dna = dad.get_dna()[:spliter]

        baby2 = self.ind_class(dad.get_species(),dad.get_food_type(),
                                dad.get_eater_type(),dad.get_size(),
                                dad.get_generation()+1,
                                dad.get_allergy(),
                                dad.get_survival_temprature(),
                                new_dna2)
        

        babies = [baby1, baby2]
        return babies


    def mutation(self,p1):
        """ 
        Mutates the species into eating different food. 
        """
        
        dna = p1.get_dna()
        pick_place = random.randint(2,7)
        for mutate in range(4):
            dna[pick_place] = random.choice(self.valid_dna_symbols)
            mutated_baby = self.ind_class(p1.get_species(), p1.get_food_type(),
                                          p1.get_eater_type(),
                                          p1.get_size(), p1.get_generation()+1,
                                          p1.get_allergy(),
                                          p1.get_survival_temprature(),dna)
        return mutated_baby




