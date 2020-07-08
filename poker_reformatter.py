
"made by: u/JokicOrEmbiid"
"date: 6/15/20"



# with that said, here is a script to convert the ascii chars in poker now logs,
# into sensible C, D, S, and H letters to represent each card.



import math
import csv
import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('infile', metavar='input_file', nargs= 1,
                    help='Input filename')


args = parser.parse_args()

# they use some crazy ascii shit so i map the last character in the string to
# each suit
suitmap = {}

suitmap["heart"] = "â™¥"
suitmap["spade"] = "â™\xa0"
suitmap["club"] = "â™£"
suitmap["diamond"] = "â™¦"


events = []
# read in all the flops, to get a list of lists
# PRE CONDITION: the csv has 3 cols, entry, at, and order.
with open(args.infile[0], 'r') as read_obj:
        
    csv_reader = csv.reader(read_obj)
    next(csv_reader)
    for row in csv_reader:
        events.append(row)







for event in events:
    eventStr = event[0]
    if (suitmap.get("heart") in eventStr or suitmap.get("club") in eventStr or 
            suitmap.get("spade") in eventStr or suitmap.get("diamond") in eventStr):
            
        eventStr = eventStr.replace(suitmap.get("spade"), "S")
        eventStr = eventStr.replace(suitmap.get("club"), "C")
        eventStr = eventStr.replace(suitmap.get("heart"), "H")
        eventStr = eventStr.replace(suitmap.get("diamond"), "D")
    
    event[0] = eventStr



with open(args.infile[0][:-4] + "_formatted.csv", mode='w', newline='') as formatted_file:
    
    poker_writer = csv.writer(formatted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for event in events:
        poker_writer.writerow(event)
        
