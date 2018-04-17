import markovify
import sys

# Simple Markov Chain Generator to create fake Kickstarter pitches
# that is basically my Sherlock Holmes sentence generator.
# By default it creates one pitch.

# to get more than one output, just type a number when running
# the script like so:
# 'python pitchgenerator.py 10'
file = open("blurbs.csv", "r")
blurbs = file.read()

model = markovify.NewlineText(blurbs)

if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
    num_sentences = int(sys.argv[1])
    
    for i in range(num_sentences):
        print(model.make_sentence(tries=100))
else:
    print(model.make_short_sentence(140))
