from create_monster import Monster
import random

class Monster_Stats(Monster):
    def __init__(self, name, species, height, weight, location, attack, defense, speed, evasion):
        super().__init__(name, species, height, weight, location)
        self.attack_pow = attack
        self.defense_pow = defense
        self.speed_pow = speed
        self.evasive_pow = evasion
         

    def attk(self):
        return f'The {self.name} attacks with {random.randint(50, self.attack_pow)} damage!'

    def __repr__(self):
            return 'Monster: {}'.format([self.name, {'attack power': self.attack_pow}])

    def __privatemonster(self):
        print(f"{self.name} 's Private method")

    @classmethod
    def powerbooster(cls, name, powerboost):
        powerboost = random.randint(50,500)
        return cls(name, powerboost)

    @staticmethod
    def is_high_difficulty(attack_power):
        return attack_power > 2000

if __name__ == "__main__":
    monster1_stats = Monster_Stats(name='Night King', species ='White Walker', 
    height = 8, weight=300, location="the north", attack=3000, defense=2500, speed=2400, evasion=500)

    # powerboost_amt = Monster_Stats.powerbooster(name='Night King', species ='White Walker', 
    # height = 8, weight=300, location="the north", attack=3000, defense=2500, speed=2400, evasion=500, 
    # powerboost=2500)
    print(Monster_Stats.powerbooster(powerboost=500))
    # print(monster1_stats)
