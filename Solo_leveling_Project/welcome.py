from Classes import *
from fights import *
import time

def Game():
    print('welcome to solo leveling')


    print('Ninja :' , "  Health:",ninja.health," || Attack:",ninja.dammage)
    print('paladin :' , "  Health",paladin.health,"|| Attack:",paladin.dammage)
    print('barbarian :' , "  Health",barbarian.health,"|| Attack:",barbarian.dammage)
    print('viking :' , "  Health",viking.health,"|| Attack:",viking.dammage)

    check=False
    while (check==False):
        print('choose your character')
        rep=input()
    
        match rep :                  
            case 'ninja':
                player=Ninja()
                check=True
            case 'paladin':
                player=Paladin()
                check=True
            case 'viking':
                player=Viking()
                check=True
            case 'barbarian':
                player=Barbarian()
                check=True
    check=False
    while (check==False):
        time.sleep(1)
        print('axe :' , "  effect:",axe.effect," || Attack:",axe.dammage)
        print('sword :' , "  effect",sword.effect,"|| Attack:",sword.dammage)
        print('katana :' , "  effect",katana.effect,"|| Attack:",katana.dammage)
        print('machete :' , "  effect",machete.effect,"|| Attack:",machete.dammage)
        print('choose your Weapon')
        rep=input()
    
        match rep :                  
            case 'axe':
                Sleh=Axe()
                check=True
            case 'sword':
                Sleh=Sword()
                check=True
            case 'katana':
                Sleh=Katana()
                check=True
            case 'machete':
                Sleh=Machete()
                check=True


    check=False
    while (check==False):
        time.sleep(1)
        print("Fire Armor:",fire.dec_dammage)
        print("Air Armor:",air.dec_dammage)
        print("Earth Armor:",earth.dec_dammage)
        print("Water Armor:",water.dec_dammage)
        print('choose your Armor')
        rep=input()
    
        match rep :                  
            case 'fire':
                deraa=firearmor()
                check=True
            case 'air':
                deraa=airarmor()
                check=True
            case 'earth':
                deraa=eartharmor()
                check=True
            case 'water':
                deraa=waterarmor()
                check=True
    W=fights_(player,Sleh,deraa)
    return W

