# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:54:30 2021

@author: rohan
"""

# run like this: python preflop-extracter.py poker-log_formatted.csv

import csv
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('infile', metavar='input_file', nargs= 1,
                    help='Input filename')


args = parser.parse_args()

events = []

# read in all the flops, to get a list of lists
# PRE CONDITION: the csv has 3 cols, entry, at, and order.
with open(args.infile[0], 'r') as read_obj:
        
    csv_reader = csv.reader(read_obj)
    next(csv_reader)
    for row in csv_reader:
        events.append(row)
        
myHands = []

for event in events: 
    eventStr = event[0]
    if "Your hand is" in eventStr:
        myHands.append(eventStr[13:])
print(myHands)

# https://www.preflophands.co
# 6 ways to get pocket pair, 12 ways to get nonsuited cards, 4 ways to get suited cards
# hands[x] = #x+1 ranked hand
hands = ["AA", "KK", "QQ", "AKs", "JJ", "AQs", "KQs", "AJs", "KJs", "TT", "AKo", "ATs", "QJs", "KTs", "QTs", "JTs", "99", "AQo", "A9s", "KQo", "88", "K9s", "T9s", "A8s", "Q9s", "J9s", "AJo", "A5s", "77", "A7s", "KJo", "A4s", "A3s", "A6s", "QJo", "66", "K8s", "T8s", "A2s", "98s", "J8s", "ATo", "Q8s", "K7s", "KTo", "55", "JTo", "87s", "QTo", "44", "33", "22", "K6s", "97s", "K5s", "76s", "T7s", "K4s", "K3s", "K2s", "Q7s", "86s", "65s", "J7s", "54s", "Q6s", "75s", "96s", "Q5s", "64s", "Q4s", "Q3s", "T9o", "T6s", "Q2s", "A9o", "53s", "85s", "J6s", "J9o", "K9o", "J5s", "Q9o", "43s", "74s", "J4s", "J3s", "95s", "J2s", "63s", "A8o", "52s", "T5s", "84s", "T4s", "T3s", "42s", "T2s", "98o", "T8o", "A5o", "A7o", "73s", "A4o", "32s", "94s", "93s", "J8o", "A3o", "62s", "92s", "K8o", "A6o", "87o", "Q8o", "83s", "A2o", "82s", "97o", "72s", "76o", "K7o", "65o", "T7o", "K6o", "86o", "54o", "K5o", "J7o", "75o", "Q7o", "K4o", "K3o", "96o", "K2o", "64o", "Q6o", "53o", "85o", "T6o", "Q5o", "43o", "Q4o", "Q3o", "74o", "Q2o", "J6o", "63o", "J5o", "95o", "52o", "J4o", "J3o", "42o", "J2o", "84o", "T5o", "T4o", "32o", "T3o", "73o", "T2o", "62o", "94o", "93o", "92o", "83o", "82o", "72o"]

# convert from Skanda format into this list
# 7S, 2C = 7 of spades, 2 of 
# We don't want "2, 7" because there is no "27o" in our ranked list - we need "72o"
# parameters are strings formatted as "7C" or "KS"



def convert(card1, card2):
    value1 = convert_int(card1[0])
    value2 = convert_int(card2[0])
    
    if value1 == value2:
        return convert_str(value1) + convert_str(value2)
    
    if value1 < value2:
        return convert(card2, card1)
    
    suit1 = card1[1]
    suit2 = card2[1]
    
    if suit1 == suit2:
        return convert_str(value1) + convert_str(value2) + "s"
    if suit1 != suit2:
        return convert_str(value1) + convert_str(value2) + "o"
    

    
    
def convert_int(value):
    if value == "T":
        return 10
    if value == "J":
        return 11
    if value == "Q":
        return 12
    if value == "K":
        return 13
    if value == "A":
        return 14
        
    return int(value)
    
def convert_str(value):
    if value == 10:
        return "T"
    if value == 11:
        return "J"
    if value == 12:
        return "Q"
    if value == 13:
        return "K"
    if value == 14:
        return "A"
    
    return str(value)

def find_the_juice(handList):
    x = 0
    
    for hand in handList:
        card1 = hand[0:2]
        card2 = hand[4:6]
        converted_hand = convert(card1, card2)
        rank = (hands.index(converted_hand) + 1) * combinations(converted_hand)
        x += rank
    x /= (len(handList))
    print(x)
    print(str(len(handList)) + " hands")

def combinations(hand):
    if len(hand) == 2:
        return 6
    if hand[2] == "s":
        return 4
    if hand[2] == "o":
        return 12

find_the_juice(myHands)

handStrengths = {}

for hand in hands:
    handStrengths[hand] = (hands.index(hand) + 1) * combinations(hand)

print(dict(sorted(handStrengths.items(), key=lambda item: item[1])))
    