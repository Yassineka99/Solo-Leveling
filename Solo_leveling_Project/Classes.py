class Character:
    def __init__(self, health, dammage):
        self.health = health
        self.dammage = dammage
class Armor :
    def __init__(self,dec_dammage,):
        self.dec_dammage=dec_dammage

class airarmor(Armor):
        def __init__(self):
            super().__init__(dec_dammage=20)
class firearmor(Armor):
        def __init__(self):
            super().__init__(dec_dammage=20)
class eartharmor(Armor):
        def __init__(self):
            super().__init__(dec_dammage=20)
class waterarmor(Armor):
        def __init__(self):
            super().__init__(dec_dammage=20)

class Weapons:
    def __init__(self,effect,dammage):
        self.effect=effect
        self.dammage=dammage

class Sword(Weapons):
    def __init__(self):
        super().__init__(effect=0.2,dammage=20)
class Katana(Weapons):
    def __init__(self):
        super().__init__(effect=0.3,dammage=18.5)
class Axe(Weapons):
    def __init__(self):
        super().__init__(effect=0.1,dammage=19)
class Machete(Weapons):
    def __init__(self):
        super().__init__(effect=0.4,dammage=18)

class Boss :
    def __init__(self,dammage,health,rewards):
        self.dammage=dammage
        self.health=health
        self.rewards=rewards    
class Ninja(Character):
    def __init__(self):
        super().__init__(health=70, dammage=60)

class Viking(Character):
    def __init__(self):
        super().__init__(health=90, dammage=60)

class Barbarian(Character):
    def __init__(self):
        super().__init__(health=100, dammage=30)

class Paladin(Character):
    def __init__(self):
        super().__init__(health=90, dammage=40)

class lvl1_boss(Boss):
    def __init__(self):
        super().__init__(dammage=30, health=90,  rewards=50)
class lvl2_boss(Boss):
    def __init__(self):
        super().__init__(dammage=40, health=100, rewards=60)
class lvl3_boss(Boss):
    def __init__(self):
        super().__init__(dammage=30, health=110, rewards=60)
class lvl4_boss(Boss):
    def __init__(self):
        super().__init__(dammage=40, health=130, rewards=40)
class lvl5_boss(Boss):
    def __init__(self):
        super().__init__(dammage=60, health=140, rewards=90)
class lvl6_boss(Boss):
    def __init__(self):
        super().__init__(dammage=70, health=200, rewards=70)
class lvl7_boss(Boss):
    def __init__(self):
        super().__init__(dammage=90, health=300, rewards=100)
class lvl7_boss(Boss):
    def __init__(self):
        super().__init__(dammage=90, health=390, rewards=100)
class lvl8_boss(Boss):
    def __init__(self):
        super().__init__(dammage=100, health=800, rewards=120)
class lvl9_boss(Boss):
    def __init__(self):
        super().__init__(dammage=100, health=800, rewards=190)
class lvl10_boss(Boss):
    def __init__(self):
        super().__init__(dammage=200, health=1800, rewards=200)

karthus=lvl10_boss()
darius=lvl9_boss()
draven=lvl8_boss()
rammus=lvl7_boss()
lilia=lvl6_boss()
Master_yi=lvl5_boss()
Vi=lvl4_boss()
belveth=lvl3_boss()
blitz=lvl2_boss()
nunu=lvl1_boss()

sword=Sword()
axe=Axe()
katana=Katana()
machete=Machete()

water=waterarmor()
fire=firearmor()
earth=eartharmor()
air=airarmor()

ninja = Ninja()
viking = Viking()
barbarian = Barbarian()
paladin = Paladin()

