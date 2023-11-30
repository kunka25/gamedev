import random

def intro():
    print("Welcome to the Forest of Mystery!")
    print("You find yourself standing at the edge of a dark and forbidding forest. A narrow path leads into the trees, and you can hear the faint sound of howling wind in the distance.")
    choice = input("Do you want to enter the forest? (yes/no) ")
    if choice.lower() == "yes":
        forest()
    else:
        print("You decide to turn back and leave the forest alone.")
        exit()

def forest():
    print("You venture into the forest, the trees growing thicker and taller around you. The path becomes darker and more difficult to follow.")
    choice = input("Do you continue along the path or explore the forest? (path/forest) ")
    if choice.lower() == "path":
        path()
    else:
        explore()

def path():
    print("You follow the path for what seems like hours, the trees never thinning. Suddenly, you come to a clearing in the forest. In the center of the clearing is a small cottage, its windows glowing with a warm light.")
    choice = input("Do you approach the cottage or continue along the path? (cottage/path) ")
    if choice.lower() == "cottage":
        cottage()
    else:
        print("You continue along the path, the forest growing darker and more ominous.")
        print("You are lost and alone, and the sounds of the forest grow ever louder.")
        print("GAME OVER")
        exit()

def explore():
    print("You leave the path and wander deeper into the forest, the trees closing in around you. The air grows colder, and you can hear the rustling of unseen creatures in the undergrowth.")
    choice = input("Do you continue exploring or return to the path? (explore/path) ")
    if choice.lower() == "explore":
        encounter()
    else:
        print("You turn back and find your way back to the path, relieved to be out of the dense undergrowth.")
        print("You continue along the path, the forest growing lighter and less ominous.")
        print("You eventually reach the edge of the forest and emerge into the sunlight.")
        print("You have escaped the Forest of Mystery!")
        exit()

def encounter():
    print("As you push through the thick undergrowth, you stumble upon a hidden cave. A faint glow emanates from within, beckoning you closer.")
    choice = input("Do you enter the cave or continue exploring? (cave/explore) ")
    if choice.lower() == "cave":
        cave()
    else:
        print("You continue exploring the forest, but you never find anything interesting.")
        print("You eventually reach the edge of the forest and emerge into the sunlight.")
        print("You have escaped the Forest of Mystery!")
        exit()

def cave():
    print("You cautiously enter the cave, the darkness swallowing you whole. The air is damp and cold, and you can hear the dripping of water in the distance.")
    choice = input("Do you continue deeper into the cave or turn back? (deeper/back) ")
    if choice.lower() == "deeper":
        treasure()
    else:
        print("You turn back and find your way out of the cave, relieved to be in the sunlight once more.")
        print("You continue along the path, the forest growing lighter and less ominous.")
        print("You eventually reach the edge of the forest and emerge into the sunlight.")
        print("You have escaped the Forest of Mystery!")
        exit()

def treasure():
    print("You stumble upon a hidden chamber deep within the cave. In the center of the chamber is a pile of glittering treasure!")
    choice = input("Do you take the treasure and leave the cave or continue exploring? (treasure/explore) ")
    if choice.lower() == "treasure":
        reward()
    else:
        print("You continue exploring the cave, but you never find anything else of value.")
        print("You eventually find your way out of the cave and emerge into the sunlight.")
        print("You have escaped the Forest of Mystery!")
        exit()

def reward():
    print("You take the treasure and leave the cave, feeling rich and powerful. You have conquered the Forest of Mystery!")
    print("GAME OVER")
    exit()

intro()
