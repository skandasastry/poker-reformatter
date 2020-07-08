## Reformatter for [pokernow.club](pokernow.club) logs.

I made this script to reformat [pokernow.club](pokernow.club) logs, since the current csv logs print out the
card suits as ASCII gibberish. 
I have instead made them into letters (C for club, D for diamond,
S for spade, H for heart). This is still able to be analyzed visually and better lends itself for
text analysis with a computer programming language. 

I would love if someone used this as a starting point to prove that [pokernow.club](pokernow.club) has a faulty, rigged random number 
generator that gives players really good hands (Quads, Full houses, flushes) at a much higher rate
than the actual mathematical probability.

### Instructions:

Run this python script on the command line like so:

poker_reformatter.py <NAME_OF_POKERNOW_LOG.csv>

The output will be <NAME_OF_POKERNOW_LOG>_formatted.csv
