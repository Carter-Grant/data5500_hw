
class Species:
    def __init__(self,name,avg_lifespan):
        self.name = name
        self.avg_lifespan = avg_lifespan
class Pet:
    species_data = {
        'dog': Species('dog', 13),  # average lifespan in years
        'cat': Species('cat', 15),
        'hamster': Species('hamster', 3),
        'parrot': Species('parrot', 50),
    }
    def __init__(self,name, age, animal_type):
        self.name = name
        self.age = age
        self.animal_type = animal_type
        if animal_type in self.species_data:
            self.species = self.species_data[animal_type]
        else:
            self.species = None

        
    def age_in_human_years(self):
        if self.species =='dog':
            return self.age * 7
        elif self.species == 'cat':
            return self.age *5
        else:
            return self.age
        
    def average_lifespan(self):
        return self.species.avg_lifespan if self.species else "Unknown species"
    
pet1 = Pet("Air_Bud", 5, "dog")
pet2 = Pet("Kitty_Cat", 3, "cat")
pet3 = Pet("Hammy", 2, "hamster")

pets = [pet1, pet2, pet3]
for pet in pets:
    human_years = pet.age_in_human_years()
    lifespan = pet.average_lifespan()
    print(f"{pet.name} is {human_years} human years old.")
    print(f"The average lifespan of a {pet.species.name if pet.species else 'unknown'} is {lifespan} years.")
#Q:how do i create a species class to store different species information. here is background informationa dn my code: 3.    Create a class called Pet with attributes name and age. Implement a method within the class to calculate the age of the pet in equivalent human years. Additionally, create a class variable called species to store the species of the pet. Implement a method within the class that takes the species of the pet as input and returns the average lifespan for that species.
#Instantiate three objects of the Pet class with different names, ages, and species.
#Calculate and print the age of each pet in human years.
#Use the average lifespan function to retrieve and print the average lifespan for each pet's species. code:class Pet:
    #def __init__(self,name,age,species):
    #    self.name = name
     #   self.age = age
     #   self.species = species
    #def species(self):
        
    #def age_in_human_years(self):
       # if self.species =='dog':
       #     return self.age * 7
       # elif self.species == 'cat':
        #    return self.age *5
       #else:
         #   return self.ages

#Q: How do i combine the 2 classes to print human age and species name? 

