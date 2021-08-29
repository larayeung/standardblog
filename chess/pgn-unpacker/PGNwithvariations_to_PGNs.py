import chess.pgn
import sys
import io

data_folder = sys.path[0]
file_to_open = data_folder + "\ModernDefense-Black.pgn"
reportoirePGN = open(file_to_open)

PGNs_done = []
PGNs_to_unpack = []

game = chess.pgn.read_game(reportoirePGN)

#print(game.board().fen())
#print(game.board())

for item in game.variations:
    if "(" in str(item):
        PGNs_to_unpack.append(str(item))
    else:
        PGNs_done.append(str(item))

for pgn in PGNs_to_unpack:
    pgn2 = io.StringIO(pgn)
    game = chess.pgn.read_game(pgn2)

    game.board().push(game.mainline_moves()[0])
        
while True:
    PGNs_to_unpack_copy = PGNs_to_unpack
    PGNs_to_unpack = []
    for pgn in PGNs_to_unpack_copy:
        pgn2 = io.StringIO(pgn)
        game = chess.pgn.read_game(pgn2)
        for item in game.variations:
            if "(" in str(item):
                PGNs_to_unpack.append(str(item))
                print("found")
            else:
                PGNs_done.append(str(item))
    print("loop")

for item in PGNs_done:
    print(item+'\n')

    
#board = game.board()
#for move in game.mainline_moves():
    #board.push(move)
    #print(board.fen())
    #print(board)
    #print(board.fen())
#while True:
     #print pgn
     #if not last node on branch:
         #step forward
         #continue
     #else:
         #either step sideways or step back