import petl
import os

# Use this file to prepare CSV data from
# webrobot.io's kickstarter data

# change this listdir input to whatever
# your path to your data is
files = os.listdir(".")[0:-1]
print(files)
first = True
for i in files:
    data = petl.fromcsv(i)
    blurbs = petl.cut(data, 'blurb')
    print(petl.look(blurbs))
    if first:
        petl.tocsv(blurbs, 'blurbs.csv')
        first = False
    else:
        petl.appendcsv(blurbs, 'blurbs.csv')

