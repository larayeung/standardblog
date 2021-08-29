import chess.pgn
import sys
import io

data_folder = sys.path[0]
file_to_open = data_folder + "\ModernDefense-Black.pgn"
reportoirePGN = open(file_to_open)

PGNs_done = []
PGNs_to_walk = []

game = chess.pgn.read_game(reportoirePGN)

#print(game.board().fen())
#print(game.board())

#return some_PGNs_done, some_PGNs_to_walk
def separate_into_done_and_towalk(some_game):
    some_PGNs_done = []
    some_PGNs_to_walk = []
    for item in some_game.variations:
        if "(" in str(item):
            some_PGNs_to_walk.append(str(item))
        else:
            some_PGNs_done.append(str(item))
    return some_PGNs_done, some_PGNs_to_walk

#return ????
def walk_each_PGN(some_PGNs_to_walk):
    some_PGNs_to_game = []
    for item in some_PGNs_to_walk:
        pgn2 = io.StringIO(item)
        game = chess.pgn.read_game(pgn2)
        game.board().push(game.mainline_moves()[0])

    return some_PGNs_to_game

#initial run, before the loop starts
ret_PGNs_done, ret_PGNs_to_walk = separate_into_done_and_towalk(game)
PGNs_done.extend(ret_PGNs_done)
PGNs_to_walk.extend(ret_PGNs_to_walk)
#

walked_PGNs = walk_each_PGN(PGNs_to_walk_copy)

PGNs_to_walk_copy = PGNs_to_walk
PGNs_to_walk = []
for pgn in PGNs_to_game:
    pgn2 = io.StringIO(pgn)
    game = chess.pgn.read_game(pgn2)

    game.board().push(game.mainline_moves()[0])
        
    for pgn in PGNs_to_walk_copy:
        pgn2 = io.StringIO(pgn)
        game = chess.pgn.read_game(pgn2)

#in this, you are trying to update PGNs_to_done
while True:

    #here we are given PGNs_done and PGNs_to_walk
    ret_PGNs_done, ret_PGNs_to_walk = separate_into_done_and_towalk(game)
    
    #they are now added to the main list
    PGNs_done.extend(ret_PGNs_done)
    PGNs_to_walk.extend(ret_PGNs_to_walk)

    # if PGNs_to_walk is 0, then this ends
    '''
    what does it mean when PGNs_to_walk is 0?
    its existence suggests that there is a function that updates it
    '''
    if len(PGNs_to_walk) == 0:
        break
    else:
        #here, we should empty PGNs_to_walk
        continue
    
    

#we reach this point when we meet these conditions:
'''
1. There are no more items in PGNs_to_walk
'''
for item in PGNs_done:
    print(item+'\n')
