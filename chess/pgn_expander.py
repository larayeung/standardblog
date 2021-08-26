#https://twitter.com/standardfoil/status/1430668746968813569

#we are given a PGN of moves from chesstempo

#let's say we want to count how many more moves on that PGN tree result in positions that occur at least 10,000 times

#http://talkchess.com/forum3/viewtopic.php?t=61695

#the pgn tree can be converted into an array of FEN codes

#... with some code, of course

#if you're working on your repertoire for the Reti opening, then you are playing as white

#so of course you want an array of FEN codes where it's black to move

#for each FEN code, you can ask lichess's API, "hey, here's an FEN code. please return a list of X moves for black. you will also return a number corresponding to each move, which is basically the amount of times that the resulting FEN code occurs in lichess's database"

#you're not exactly sure how many FEN positions occur 10,000 times. it may be 1,000. it may be 10,000. it may be 10. so you're going to make a variable called "position_count_cutoff"

#you're going to be adjusting this variable and rerunning the code multiple times

#to be safe, we're going to make the amount of moves requested 30.

#we're going to take all the moves with a frequency greater than position_count_cutoff and put them into a temporary array.

#for each move in that array, a new FEN code is generated, which is then placed into the original array of FEN codes.

#in addition, each move in that array is subsequently added to the original pgn file, increasing the amount of moves in the reportoire

#we're going to want to count how many times a new move is added, so we're going to have a counter variable and have that printed at the end.
