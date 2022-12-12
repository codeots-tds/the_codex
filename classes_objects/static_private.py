class MonsterSuper:
    super_monster_count = 0
    def __init__(self, name, typemonster, atk, defense):
        self.name = name
        self.typemonster = typemonster
        self.atk = atk
        self.defense = defense
        MonsterSuper.up_count()

    @property
    def monster_stats(self):
        return f"My {self.name} has {self.atk} attack points and {self.defense} defense points!"

    @staticmethod
    def monster_super_tier(x):
        if x >= 3000:
            return "super"
        return "normal"

    @classmethod
    def up_count(cls):
        cls.super_monster_count +=1

    @classmethod
    def get_count_num(cls):
        return cls.super_monster_count


if __name__ == "__main__":
    #calling using the class
    # print(MonsterSuper.get_count_num()) #0

    obelisk = MonsterSuper(name = "Obelisk The Tormentor", typemonster= "Egyptian God", 
    atk = 4000, defense = 4000)
    # print(f"{obelisk.name} is a {MonsterSuper.monster_super_tier(obelisk.atk)} monster!")
    # print(obelisk.get_count_num()) #1

    slifer = MonsterSuper(name = "Slifer The Sky Dragon", typemonster= "Egyptian God", 
    atk = 0000, defense = 0000)
    # print(slifer.get_count_num()) #2

    print(obelisk.monster_stats)
    pass



    # @classmethod
    # def monster_count(cls):
    #     cls.monster_num += 1

    # @classmethod
    # def monster_superclass(cls):
    #     if cls.atk >= 3000:
    #         return cls.superclass_rank
    #     return "normal"
      #calling using a class instance object
    # print(f"{obelisk.name} is a {obelisk.monster_superclass()} monster.")