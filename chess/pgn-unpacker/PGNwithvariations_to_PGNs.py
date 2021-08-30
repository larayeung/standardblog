import chess.pgn
import sys
import io
from time import sleep

data_folder = sys.path[0]
file_to_open = data_folder + "\ModernDefense-Black.pgn"
reportoirePGN = open(file_to_open)

PGNs_done = []
PGNs_to_walk = []
walked_PGNs_to_separate = []

game = chess.pgn.read_game(reportoirePGN)
some_PGNs_done = []
some_PGNs_to_walk = []
for item in game.variations:
    if "(" in str(item):
        some_PGNs_to_walk.append(str(item))
        print("still need to walk: " + str(item) + "\n")        
        sleep(.25)
    else:
        some_PGNs_done.append(str(item))
        print("done with: " + str(item) + "\n")
        sleep(.25)
        
PGNs_done.extend(some_PGNs_done)
PGNs_to_walk.extend(some_PGNs_to_walk)

#print(game.board().fen())
#print(game.board())

#return some_PGNs_done, some_PGNs_to_walk
def separate_into_done_and_towalk(some_walked_PGNs_to_separate):
    some_PGNs_done = []
    some_PGNs_to_walk = []
    
    for pgn in some_walked_PGNs_to_separate:
        pgn2 = io.StringIO(pgn)
        some_game = chess.pgn.read_game(pgn2)
        for item in some_game.variations:
            if "(" in str(item):
                some_PGNs_to_walk.append(str(item))
            else:
                some_PGNs_done.append(str(item))
    return some_PGNs_done, some_PGNs_to_walk

#return ????
def walk_each_PGN(some_PGNs_to_walk):
    some_walked_PGNs_to_separate = []
    
    for item in some_PGNs_to_walk:
        print("we are walking: " + str(item) + "\n")
        sleep(1)
        pgn2 = io.StringIO(item)
        game = chess.pgn.read_game(pgn2)
        
        board = game.board()
        for move in game.mainline_moves():
            some_walked_PGNs_to_separate.append(str(board.san(move)))
            print("this is a walked PGN we are going to separate: " + \
                  str(board.san(move)) + \
                  "\n")
            break

    return some_walked_PGNs_to_separate



#in this, you are trying to update three objects
while True:
   
    PGNs_to_walk_copy = PGNs_to_walk
    PGNs_to_walk = []
    walked_PGNs_to_separate = walk_each_PGN(PGNs_to_walk_copy)
    
    #here we are given PGNs_done and PGNs_to_walk
    ret_PGNs_done, ret_PGNs_to_walk = \
        separate_into_done_and_towalk(walked_PGNs_to_separate)
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
        #past this, we should empty PGNs_to_walk
        pass


    
    

#we reach this point when we meet these conditions:
'''
1. There are no more items in PGNs_to_walk
1. th
'''
for item in PGNs_done:
    print(item+'\n')
