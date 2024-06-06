import os

class person():
    def __init__(person, attack: int, health: int) -> None:
        person.attack = attack
        person.health = health

#Break down:
#This code is meant to define Mars as a class 'person' and then I defined what their attacks and health equals
Mars = person(attack=30, health=100)
Leo = person(attack=30, health=150) 

#This is a loop to keep the battle running
while True:
    #The def fight(person,target) is to show the computer that their are two arguments/or 'people fighting' if you will.
    def fight(person, target)-> None:
        print("Leo ATTACKS!")
        #this is the math to show the targets health and the persons attack so: 150
        target.health -= person.attack
        print(f" Mars Health: {Mars.health}\n\n_______________\n\n")
        print("Mars ATTACKS!")
        person.health -= target.attack
        print(f" Leo health {Leo.health}")

        #This makes it os that if the objects/'Mars' health goes below zero then the battle is over!
        if Mars.health < 0:
            os.system("cls")
            print("Mars has died in battle")
            input()

        if Leo.health < 0:
            os.system("cls")
            print("Leo has died in battle!")
            input()


    



    fight(Leo, Mars)
    
    input()

