# Takes in 


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

with open("preflop-hands.csv", mode='w', newline='') as formatted_file:
    
    poker_writer = csv.writer(formatted_file)

    for hand in myHands:
        poker_writer.writerows([[hand]])  