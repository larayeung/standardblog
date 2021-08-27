from stockfish import Stockfish
import time

FENs = [
        'rnbqk1nr/ppppppbp/6p1/8/4PPP1/8/PPPP3P/RNBQKBNR b KQkq - 0 3',
        'rnbqk1nr/ppppppbp/6p1/6P1/4P3/8/PPPP1P1P/RNBQKBNR b KQkq - 0 3',
        'rnbqk1nr/ppppppbp/6p1/8/4P1P1/8/PPPP1PBP/RNBQK1NR b KQkq - 2 3',
        'rnbqk1nr/ppppppbp/6p1/8/4P1PP/8/PPPP1P2/RNBQKBNR b KQkq - 0 3',
        'rnbqk1nr/ppppppbp/6p1/8/3PP1P1/8/PPP2P1P/RNBQKBNR b KQkq - 0 3'
]

stockfish = Stockfish("/root/stockfishengine/stockfish_14_x64_avx2")

stockfish = Stockfish(parameters={"Threads":14,"Hash": 65336,"Write Debug Log": "true"})

print(stockfish.get_parameters())

stockfish.set_depth(40)

localtime = time.localtime()
result = time.strftime("%I:%M:%S %p", localtime)
print(result)

for FEN in FENs:
    stockfish.set_fen_position(FEN)
    print(stockfish.get_best_move())
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
