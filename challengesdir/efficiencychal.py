#!/usr/bin/env python3

import pandas as pd

def menu():
    """this will print out a menu of choices so the user knows what is available."""
    while True:
          demolist = ["1. Apple","2. Banana","3. Cherries","4. Dragonfruit"]
          print("Choose a fruit: ")
          for x in demolist:
              print(x)
          break

    while True:
        choice= input(">")

        if choice == "1":
            print("You picked apple!")
            break
        elif choice == "2":
            print("You picked banana!")
            break
        elif choice == "3":
            print("You picked cherries!")
            break
        elif choice == "4":
            print("You picked dragonfruit!")
            break
        else:
            print("That was not an option.")
            break

def sports():
    """what is a more efficient way to return this info instead of using a bunch
    of if/elif/else lines?"""

    while True:

        quitwords= ["Q", "q", "Quit", "quit", "Stop", "stop", "End", "end"]

        print("\nPick a sport to see what equipment you need!")
        print(["football", "soccer", "tennis", "baseball"])

        sport= input("\n>")

        if sport in quitwords:
            break

        if sport == "football":
            print("football, pads, helmet")
            break

        elif sport == "soccer":
            print("soccer ball, shin guards")
            break

        elif sport == "tennis":
            print("two tennis rackets, tennis ball")
            break

        elif sport == "baseball":
            print("baseball, bat, glove")
            break

        else:
            print("That is not one of the correct sports!")


def creation():
    poke_df = pd.read_csv("pokedex.txt", index_col=1)
    
    print("\n10 best attackers:")
    new_df = poke_df.sort_values(["Attack"], ascending=False)    
    print(new_df.head(10))

    print("\n10 best defenders:")
    new_df = poke_df.sort_values(["Defense"], ascending=False)              
    print(new_df.head(10))

    print("\n10 highest HP:")
    new_df = poke_df.sort_values(["HP"], ascending=False)              
    print(new_df.head(10))


def challenge():
    # HARDER THAN IT LOOKS:
    # I have a bunch of numbers that I need to increase by 1!

    nums= [5,10,15,20,25]

    # this will cause an error! how should we do this, then?
    nums[0] = nums[0] + 1
    nums[1] = nums[1] + 1
    nums[2] = nums[2] + 1
    nums[3] = nums[3] + 1
    nums[4] = nums[4] + 1
 
# menu()
# sports()
# creation()
# challenge()
