#!/usr/bin/env python3
print("Welcome to the bridge riddle.You have 17 minutes to cross this very dangerous bridge - AT NIGHT! There are 3 other people who need to cross this bridge with you. Only 2 people can cross the bridge at once since it is dark and unstable. There is only one lantern available among the group, so both people must cross together. Each person crosses the bridge at their own pace. Person A can cross the bridge in 1 minute, Person B in 2, Person C in 5, Person D is the slowest and takes 10 minutes to cross. Any person can wait on either side of the bridge in the darkness, but all 4 people must have crossed to the other side by the end of 17 minutes or the bridge will break.\n")


ttc= 17
#person_a= 1
#person_b= 2
#person_c= 5
#person_d= 10
runners= {"person_a":1, "person_b":2, "person_c":5, "person_d":10}

while True:
    first_runner=input("Who will be the first person you choose? Person A, B, C, or D?\n").lower()
    if first_runner in ["a","b","c","d"]:
        break
    else:
        print("(Please type a, b, c, or d, to specify first runner)")
while True:
    second_runner=input("Who will accompany them?\n").lower()
    if second_runner == first_runner:
        print(f'(You already chose {first_runner})')
    elif second_runner in ["a","b","c","d"]:
        break
    else:
        print(f'(Please choose a runner to accompany {first_runner})')
while True:
                                         # first_runner will be equal to either a, b, c, or d
    first_runner = runners["person_" + first_runner]
    break
while True:
    second_runner = runners["person_" + second_runner]
    break
if first_runner < second_runner:
    ttc = ttc-second_runner
else:
    ttc = ttc-first_runner

print(f'You have made it across with {ttc} minutes left!')


print(f'{ttc}')
print(f'{first_runner}')
print(f'{second_runner}')
