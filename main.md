why do i have this blog even though i already have [notion](ordoliberal.com) and [twitter](twitter.com/laraaaanguyen)? different formats produce different ideas.

if you look through our repos as of July 2021, there are like 8 different repos and like none of them have any real code. this could be a useful place to store random ideas and pseudocode that'll stay there until we feel like actually... making it code.

it seems a bit weird to have one repo per idea which may never pan out, and it may end up actually crowding out the good ones if someone ever looks at our resume

### Spaced Repetition Software

(sam) Anki makes me mad. It's not the developers' fault, and I think they've done a great contribution to society. Nevertheless, the software frustrates because I wish they'd sell out and turn anki into a platform in and of itself that plugs into other stuff.

(lara) I disgree with Sam on where the issue lays. We've been using chesstempo to increase our elo, the basic spaced repetition algorithm - anki is a generalized solution to the "spaced repetition software" problem. Of course it won't work perfectly for like, math.

### Pseudocode for python script that finds an optimal move

hmm i will probably split this doc up when this doc is sufficiently big enough.

anyway what i want to do is to be able to create a piece of code that spits out the optimal move given like, a pgn code.

let's say i have an array of PGNs:

PGNs = ["1.Nf3 d5", "1.e4"]

now i need a loop to iterate through each item in that list

the output is a list that looks like

optimalMoveList = ["1.Nf3 d5 2.d4", "1.e5 g6"]

what goes on inside that loop is something like

  for pgn in PGNs:
    optimal move = go use that stockfish api to find the optimal move for that, at depth 30
  
    optimizedpgn = pgn + optimal move
  
    append optimizedpgn to optimalmovelist

... and then print the optimalmovelist

So the steps are

1. pip install stockfish
2. actually install stockfish 
3. create a file called
bestmove.py:
  from stockfish import Stockfish
  stockfish = Stockfish("/path/to/file")

  #make depth 30
  stockfish.set_depth(30)


### moving my notion blog to github

notion is slow and it pisses me off.

i want to export my notion blog to github. not sure how that would work.


### learning math by starting with set theory

the only thing that all six of us can agree on is that algebra sucks and learning set theory seems fun. i mean, at least one of us *knows* algebra but the other five don't want to learn math through that.

so, we want to be able to take something like [this](http://builds.openlogicproject.org/courses/set-theory/) and internalize it through anki.

there are a few strategies that we'll avoid off the bat:

Skimming it from front to back seems useless. Math is heavily based on mastery, and we will quickly not comprehend anything that goes on within a chapter or so.
I remember when we self-studied for something like AP Human in a weekend, which basically involved rereading the book multiple times and highlighting a bunch of stuff. Each time we re-read, we understood a little bit more. I don't think this will work for math.

(terry) What i think is a good idea, then, is to read the textbook [chapter-by-chapter](http://builds.openlogicproject.org/courses/set-theory/settheory-screen.pdf) chapter by chapter... maybe even section-by-section

After skimming each section, work on ankifying the components of each textbook. 

That process is basically

1. getting the section into a plain textfile, through typing or copy-pasting
2. separating that section into individual note-sized chunks (by the anki definition of notes)
3. cloze-ifying each note
4. importing the file into anki

### learning the game of go by cloning my python code

after countless revisions, i finally have something that produces expansions to my chess reportoire for chesstempo dot com.

i kind of want to do the same for go, except i'm starting from an empty reportoire.

black: one in the center

white: 

white b, in case the first slot is taken already by black:  


