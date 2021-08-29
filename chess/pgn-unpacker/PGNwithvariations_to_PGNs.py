import chess.pgn
import sys

data_folder = sys.path[0]
file_to_open = data_folder + "\ModernDefense-Black.pgn"

reportoirePGN = open(file_to_open)

game = chess.pgn.read_game(reportoirePGN)

#print(game.board().fen())
#print(game.board())

for item in game.variations:
    print(item)

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