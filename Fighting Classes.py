class person():
    def __init__(person, attack: int, health: int) -> None:
        person.attack = attack
        person.health = health

Mars = person(attack=30, health=100)
Leo = person(attack=30, health=150) 

def fight(person, target)-> None:
    print("Leo Gets attacked!")
    target.health -= person.attack
    print(f" Leos Health: {Mars.health}\n\n_______________\n\n")
    print("Mars gets attacked")
    person.health -= target.attack
    print(f" Mars health {Leo.health}")


fight(Leo, Mars)