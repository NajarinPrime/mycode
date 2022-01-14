#!/usr/bin/env python3
runners= {"a":1, "b":2, "c":5, "d":10}
ttc= 17
end= 0
start= ["a","b","c","d"]
finish= []
def crosser():
    global ttc
    while True:
        choice= input("Which runner will cross: a, b, c, d? ").lower()
        if choice in ["a","b","c","d"]:
            break
        else:
            print("Please only choose a, b, c, or d.")
    while True:
        second_choice= input("Who will join them? ").lower()
        if second_choice == choice:
            print("You already chose this runner, choose another.")
        elif second_choice in ["a","b","c", "d"]:
            break
        else:
            print("Please only choose a, b, c, or d.")
    while True:
        if runners[choice] < runners[second_choice]:
            ttc= ttc - runners[second_choice]
            print(f'Runners {choice} and {second_choice} have made it across with {ttc} minutes left')
        else:
            ttc= ttc - runners[choice]
            print(f'Runners {choice} and {second_choice} have made it across with {ttc} minutes left')
        break
def returner():
    global ttc
    while True:
        choice= input("Choose one runner to return the lamp: ").lower()
        if choice in ["a","b","c","d"]:
            break
        else:
            print("Please only choose a, b, c, or d.")
    while True:
        ttc= ttc - runners[choice]
        print(f'Runner {choice} returns the lantern with {ttc} minutes left')
        break

def crossing():
    while True:
        crosser()
        if ttc > end:
            returner()
        elif ttc == end:
            break
        elif ttc < end:
            print("You ran out of time")
            break
        else:
            print("You ran out of time")
            break

print("Welcome to the bridge riddle.You have 17 minutes to cross this very dangerous bridge - AT NIGHT! There are 3 other people who need to cross this bridge with you. Only 2 people can cross the bridge at once since it is dark and unstable. There is only one lantern available among the group, so both people must cross together. Each person crosses the bridge at their own pace. Person A can cross the bridge in 1 minute, Person B in 2, Person C in 5, Person D is the slowest and takes 10 minutes to cross. Any person can wait on either side of the bridge in the darkness, but all 4 people must have crossed to the other side by the end of 17 minutes or the bridge will break.\n")
crossing()
if ttc == end:
    print("Congratulations!!!")
