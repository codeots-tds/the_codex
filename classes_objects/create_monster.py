class Monster:
    def __init__(self, name, species, height, weight, location):
        self.name = name
        self.species = species
        self.height = height 
        self.weight = weight
        self.location = location 


    def monster_data(self):
        return self.__dict__    

    
if __name__ == "__main__":
    monster1 = Monster(name = "Terror", species = "beast", height = 1500, weight = 10000, location = "Mordor")
    monster2 = Monster(name = "Torementor", species = "reaper", height = 700, weight = 500, location = "Kalimdor") 

    monster1.height = 3250
    monster2.name = "Obelisk"
    print(monster1.height)
    print(monster2.name)

    