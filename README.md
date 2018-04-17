# The Dumbest Kickstarter Pitch Generator

It's not even good. I saw the idea on Twitter to make a pitch generator so I made one.

Credit to https://webrobots.io/kickstarter-datasets/ for the  scraped Kickstarter data. I just
trimmed out the 'blurbs' columns from the CSV files, chucked all that into an 80000
line CSV, and ran markovify on it. Nothing fancy.

Sample output:
```
python pitchgenerator.py 10
I am doing a BBQ sauce business from home - Even in today's politically and socially divisive world.
PUT A LOCK ON IT! You don’t need to charge your battery.
Our jobs suck and I need funding to publish a coloring book will be used to enhance the natural world
PUT A LOCK ON IT! You don’t need to charge your battery.
Touch & Go is a re-imagined 80s Saturday morning cartoon that will lift your spirit.
Professional Artist interested in Futures Studies.
Pitch Piece that follows Jay Miller on his mission!
Five time travelling facility for adults!
Shoes for the mind. A fusion of art nouveau style.
We believe in UFOs & aliens? Then buy this RV from Craigslist and makes music lessons to be a mobile app
