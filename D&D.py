import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
name = input('enter name')
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n")

def intro():
    print('hi',name, 'welcome to the jungle')
    print("You wake up in a thick forest with few injuries and cannot remember anything, "
          "Head spinning and fighting to find what happened, you stand and look at the new, "
          "place, where it was so peaceful. The peace quickly fades when you hear a "
          "rattling sound emitting behind you. it was a killer monster and it is "
          "running towards you. You will:")
    time.sleep(1)
    print("""  A. Grab a nearby rock and throw it at the monster
  B. Lie down and wait to it to pass 
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print("\n it just stamped you and. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_rock():
    print("\nThe monster is injured, but regains control. He begins "
          "running towards you again. Will you:")
    time.sleep(1)
    print("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\nYou decided to throw another rock, as if the first "
              "rock thrown did much damage. The rock flew well over the "
              "monster's head. You missed it and it came to you. \n\nYou died!")
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_cave():
    print("\nYou were hesitant, since the cave was dark and "
          "ominous. Before you fully enter, you notice a shiny sword on "
          "the ground. Do you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1
    else:
        sword = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""  A. Hide in silence
  B. Fight
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nReally? You're going to hide in the dark? I think "
              "monstor can see very well in the dark, right? Not sure, but "
              "I'm going with YES, so...\n\nYou died!")
    elif choice in answer_B:
        if sword > 0:
            print("\nYou laid in wait. The shimmering sword attracted "
                  "the monster, which thought you were no match. As he walked "
                  "closer and closer, your heart beat rapidly. As the monster "
                  "reached out to grab the sword, you pierced the blade into "
                  "its chest. \n\nYou survived!")
        else:
            print("\nYou should have picked up that sword. You're "
                  "defenseless. \n\nYou died!")
    elif choice in answer_C:
        print("As the monster enters the dark cave, you quietly "
              "sneak out. You're several feet away, but the monster turns "
              "around and sees you running.")
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print("\nYou run as quickly as possible, but the monster's "
          "speed is too great. You will:")
    time.sleep(1)
    print("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
    choice = input(">>> ")
    if choice in answer_A:
        print("You're easily spotted. "
              "\n\nYou died!")
    elif choice in answer_B:
        print("\nYou're no match for an monster. seriously what do you think "
              "\n\nYou died!")
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print("\nWhile frantically running, you notice a rusted "
          "sword lying in the mud. You quickly reach down and grab it, "
          "but miss. You try to calm your heavy breathing as you hide "
          "behind a delapitated building, waiting for the monster to come "
          "charging around the corner. You notice a purple flower "
          "near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flower = 1
    else:
        flower = 0
    print("You hear its heavy footsteps and ready yourself for "
          "the impending monster.")
    time.sleep(1)
    if flower > 0:
        print("\nYou quickly hold out the purple flower, somehow "
              "hoping it will stop the monster. It does! The monster was looking "
              "for the flower which helps to come out of the curse. "
              "\n\nThis got weird, but you survived!")
    else:
        print("\nMaybe you should have picked up the flower. "
              "\n\nYou died!")


intro()