import random

import os

import time

class setUp:

    def __init__(self): #makes deck and shuffles

        global deck

        deck = {"season":[], "value":[]}

        Seasons = ["Pine", "Cherry Blossom", "Iris", "Clover", "Chrysanthemum", "Willow", "Plum BLossom", "Wisteria", "Peony", "Pampas", "Maple", "Paulownia", "Pine", "Cherry Blossom", "Iris", "Clover", "Chrysanthemum", "Willow", "Plum BLossom", "Wisteria", "Peony", "Pampas", "Maple", "Paulownia", "Pine", "Cherry Blossom", "Iris", "Clover", "Chrysanthemum", "Willow", "Plum BLossom", "Wisteria", "Peony", "Pampas", "Maple", "Paulownia", "Pine", "Cherry Blossom", "Iris", "Clover", "Chrysanthemum", "Willow", "Plum BLossom", "Wisteria", "Peony", "Pampas", "Maple", "Paulownia"]

        Values = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, ]

        deck = [(Seasons[i], Values[i]) for i in range(0, len(Seasons))]

        random.shuffle(deck)

    def deal(self): #deals cards 

        global hand

        hand = deck[0:8]

        del deck[0:8]

        return hand


def deal(self):  #creates hands

    global p1_hand

    global middle

    global p2_hand

    p1_hand = setUp.deal(self)

    middle = setUp.deal(self)

    p2_hand = setUp.deal(self)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


class play: #defines actions players can make

    check = 1

    def p1_turn(self):

        global check

        global choice

        global p1_scored

        p1_seasons = ([x[0] for x in p1_hand])

        middle_seasons = ([x[0] for x in middle])

        match = list(set(p1_seasons) & set(middle_seasons))

        num = len(match)

        if len(match) > 0:

            if num > 0: num = num - 1

            choice = match[random.randint(0, num)]

            p1_scored = [p1_hand[p1_seasons.index(choice)]]  #adds played card from p1_hand to pp1's scored deck

            del p1_hand[p1_seasons.index(choice)]    #removes played card from p1's hand

            p1_scored.append(middle[middle_seasons.index(choice)])     #adds played card from middle to p1's scored deck

            del middle[middle_seasons.index(choice)]     #removes played card from middle




class end:   #defines round endings

    def draw(self):
        print("Draw")








   
End = False
        





setUp()

deal(1)

counter = 0

while True:
    play.p1_turn(play)

    counter = counter + 1

    print(counter)

    print(p1_hand)

    time.sleep(1)






