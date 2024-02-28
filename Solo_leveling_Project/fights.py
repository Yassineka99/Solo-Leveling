from Classes import *
import time     
def fights_(player,sleh,deraa):
    def fight_1(player,sleh,deraa,nunu):
        print("click any key to hit the monster")
        time.sleep(2)
        while(nunu.health>0 and player.health>0):
            boss1=open("boss1.txt","r")
            for line in boss1.readlines():
                print(line)
            boss1.close()
            print("HEALTH",nunu.health,"||","DAMMAGE",nunu.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    nunu.health=nunu.health-(player.dammage*sleh.effect+sleh.dammage+player.dammage)
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((nunu.dammage*deraa.dec_dammage)/100)
        if(nunu.health<=0):
            
            print("Well done you killed the boss")
            print("You won",nunu.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=nunu.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+nunu.rewards
            return True
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close()
            return False
    def fight_2(player,sleh,deraa,blitz):
        print("click any key to hit the monster")
        time.sleep(2)
        while(blitz.health>0 and player.health>0):
            boss2=open("boss2.txt","r")
            for line in boss2.readlines():
                print(line)
            boss2.close()
            print("HEALTH",blitz.health,"||","DAMMAGE",blitz.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    blitz.health=blitz.health-(player.dammage*sleh.effect+sleh.dammage+player.dammage)
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((blitz.dammage*deraa.dec_dammage)/100)
        if(blitz.health<=0):
            print("Well done you killed the boss")
            print("You won",blitz.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=blitz.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+blitz.rewards
            return True
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close() 
            return False  
    def fight_3(player,sleh,deraa,belveth):
        print("click any key to hit the monster")
        time.sleep(2)
        while(belveth.health>0 and player.health>0):
            boss3=open("boss3.txt","r")
            for line in boss3.readlines():
                print(line)
            boss3.close()
            print("HEALTH",belveth.health,"||","DAMMAGE",belveth.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    belveth.health=belveth.health-((player.dammage*sleh.effect+sleh.dammage+player.dammage))
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((belveth.dammage*deraa.dec_dammage)/100)
        if(belveth.health<=0):
            print("Well done you killed the boss")
            print("You won",belveth.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=belveth.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+belveth.rewards
            return True 
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close()
            return False
    def fight_4(player,sleh,deraa,Vi):
        print("click any key to hit the monster")
        time.sleep(2)
        while(Vi.health>0 and player.health>0):
            boss4=open("boss4.txt","r")
            for line in boss4.readlines():
                print(line)
            boss4.close()
            print("HEALTH",Vi.health,"||","DAMMAGE",Vi.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    Vi.health=Vi.health-(player.dammage*sleh.effect+sleh.dammage+player.dammage)
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((Vi.dammage*deraa.dec_dammage)/100)
        if(Vi.health<=0):
            print("Well done you killed the boss")
            print("You won",Vi.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=Vi.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+Vi.rewards
            return True 
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close()        
            return False   
    def fight_5(player,sleh,deraa,Master_yi):
        print("click any key to hit the monster")
        time.sleep(2)
        while(Master_yi.health>0 and player.health>0):
            boss5=open("boss5.txt","r")
            for line in boss5.readlines():
                print(line)
            boss5.close()
            print("HEALTH",Master_yi.health,"||","DAMMAGE",Master_yi.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    Master_yi.health=Master_yi.health-(player.dammage*sleh.effect+sleh.dammage+player.dammage)
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((Master_yi.dammage*deraa.dec_dammage)/100)
        if(Master_yi.health<=0):
            print("Well done you killed the boss")
            print("You won",Master_yi.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=Master_yi.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+Master_yi.rewards
            return True 
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close()           
            return False
    def fight_6(player,sleh,deraa,lilia):
        print("click any key to hit the monster")
        time.sleep(2)
        while(lilia.health>0 and player.health>0):
            boss6=open("boss6.txt","r")
            for line in boss6.readlines():
                print(line)
            boss6.close()
            print("HEALTH",lilia.health,"||","DAMMAGE",lilia.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    lilia.health=lilia.health-((player.dammage*sleh.effect+sleh.dammage+player.dammage))
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((lilia.dammage*deraa.dec_dammage)/100)
        if(lilia.health<=0):
            print("Well done you killed the boss")
            print("You won",lilia.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=lilia.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+lilia.rewards
            return True 
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close()
            return False
    def fight_7(player,sleh,deraa,rammus):
        print("click any key to hit the monster")
        time.sleep(2)
        while(rammus.health>0 and player.health>0):
            boss7=open("boss7.txt","r")
            for line in boss7.readlines():
                print(line)
            boss7.close()
            print("HEALTH",rammus.health,"||","DAMMAGE",rammus.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    rammus.health=rammus.health-(player.dammage*sleh.effect+sleh.dammage+player.dammage)
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((rammus.dammage*deraa.dec_dammage)/100)
        if(rammus.health<=0):
            print("Well done you killed the boss")
            print("You won",rammus.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=rammus.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+rammus.rewards
            return True
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close()
            return False   
    def fight_8(player,sleh,deraa,draven):
        print("click any key to hit the monster")
        time.sleep(2)
        while(draven.health>0 and player.health>0):
            boss8=open("boss8.txt","r")
            for line in boss8.readlines():
                print(line)
            boss8.close()
            print("HEALTH",draven.health,"||","DAMMAGE",draven.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    draven.health=draven.health-((player.dammage*sleh.effect+sleh.dammage+player.dammage))
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((draven.dammage*deraa.dec_dammage)/100)
        if(draven.health<=0):
            print("Well done you killed the boss")
            print("You won",draven.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=draven.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+draven.rewards
            return True 
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close()
            return False
    def fight_9(player,sleh,deraa,darius):
        print("click any key to hit the monster")
        time.sleep(2)
        while(darius.health>0 and player.health>0):
            boss9=open("boss9.txt","r")
            for line in boss9.readlines():
                print(line)
            boss9.close()
            print("HEALTH",darius.health,"||","DAMMAGE",darius.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    darius.health=darius.health-(player.dammage*sleh.effect+sleh.dammage+player.dammage)
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((darius.dammage*deraa.dec_dammage)/100)
        if(darius.health<=0):
            print("Well done you killed the boss")
            print("You won",darius.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=darius.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+darius.rewards
            return True 
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close() 
            return False          
    def fight_10(player,sleh,deraa,karthus):
        print("click any key to hit the monster")
        time.sleep(2)
        while(karthus.health>0 and player.health>0):
            boss10=open("boss10.txt","r")
            for line in boss10.readlines():
                print(line)
            boss10.close()
            print("HEALTH",karthus.health,"||","DAMMAGE",karthus.dammage)
            print("Your HEALTH",player.health,"||"," Your DAMMAGE",player.dammage)
            rep=input()
            match rep:
                case _:
                    karthus.health=karthus.health-(player.dammage*sleh.effect+sleh.dammage+player.dammage)
            time.sleep(1)
            print("boss is hitting back")
            time.sleep(1)
            player.health=player.health-((karthus.dammage*deraa.dec_dammage)/100)
        if(karthus.health<=0):
            print("Well done you killed the boss")
            print("You won",karthus.rewards,"Points")
            print("Do yo want to add them to Hp or attack ?")
            rep=input()
            match rep :
                case 'hp' :
                    x= player.health
                    player.health=karthus.rewards+x
                    print("Your hp went from ",x, "to ",player.health)
                case 'dammage' :
                    player.dammage= player.dammage+karthus.rewards
            return True 
        else :
            end=open("defeat.txt","r")
            for line in end.readlines():
                print(line)
            end.close()
            return False          
    reply=fight_1(player,sleh,deraa,nunu)
    game="not finished"
    if reply==True:
        print("fight 2 loading",end='')
        i=1
        for i in range(3):
            time.sleep(1)
            print('. ',end='')
        reply=fight_2(player,sleh,deraa,blitz)
        if reply==True:
            print("fight 3 loading",end='')
            i=1
            for i in range(3):
                time.sleep(1)
                print('. ',end='')
            reply=fight_3(player,sleh,deraa,belveth)
            if reply==True:
                print("fight 4 loading",end='')
                i=1
                for i in range(3):
                    time.sleep(1)
                    print('. ',end='')
                reply=fight_4(player,sleh,deraa,Vi)
                if reply==True:
                    print("fight 5 loading",end='')
                    i=1
                    for i in range(3):
                        time.sleep(1)
                        print('. ',end='')
                    reply=fight_5(player,sleh,deraa,Master_yi)
                    if reply==True:
                        print("fight 6 loading",end='')
                        i=1
                        for i in range(3):
                            time.sleep(1)
                            print('. ',end='')
                        reply=fight_6(player,sleh,deraa,lilia)
                        if reply==True:
                            print("fight 7 loading",end='')
                            i=1
                            for i in range(3):
                                time.sleep(1)
                                print('. ',end='')
                            reply=fight_7(player,sleh,deraa,rammus)
                            if reply==True:
                                print("fight 8 loading",end='')
                                i=1
                                for i in range(3):
                                    time.sleep(1)
                                    print('. ',end='')
                                reply=fight_8(player,sleh,deraa,draven)
                                if reply==True:
                                    print("fight 9 loading",end='')
                                    i=1
                                    for i in range(3):
                                        time.sleep(1)
                                        print('. ',end='')
                                    reply=fight_9(player,sleh,deraa,darius)
                                    if reply==True:
                                        print("fight 10 loading",end='')
                                        i=1
                                        for i in range(3):
                                            time.sleep(1)
                                            print('. ',end='')
                                        fight_10(player,sleh,deraa,karthus)
                                        game="finished"
    return game