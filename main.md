why do i have this blog even though i already have [notion](ordoliberal.com) and [twitter](twitter.com/laraaaanguyen)? different formats produce different ideas.

if you look through our repos, there are like 8 different repos and like none of them have any real code. this could be a useful place to store random ideas and pseudocode that'll stay there until we feel like actually... making it code.

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

and then print the optimalmovelist

### moving my notion blog to github

notion is slow and it pisses me off.

i want to export my notion blog to github. not sure how that would work.

