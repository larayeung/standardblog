from stockfish import Stockfish
import time

FENs = [
        'rnbqk1nr/pp3ppp/2p1p3/3p4/1bPP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 2 5',
        'rnbqkb1r/pp3ppp/2p1pn2/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 2 5',
        'rnbqkbnr/pp4pp/2p1p3/3p1p2/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 0 5',
        'rnbqk1nr/pp3ppp/2pbp3/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 2 5',
        'r1bqkbnr/pp1n1ppp/2p1p3/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 2 5',
        'rnbqkbnr/pp3ppp/2p1p3/8/2pP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 0 5',
        'rnbqkbnr/1p3ppp/p1p1p3/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 0 5',
        'rnbqk1nr/pp2bppp/2p1p3/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 2 5',
        'rnbqkbnr/pp3p1p/2p1p1p1/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 0 5',
        'rnbqkbnr/pp3pp1/2p1p2p/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 0 5',
        'rnbqkb1r/pp2nppp/2p1p3/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 2 5',
        'rnbqkbnr/p4ppp/1pp1p3/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 0 5',
        'rn1qkbnr/pbpp1ppp/1p2p3/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkbnr/pbpppp1p/1p4p1/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkb1r/pbpppppp/1p3n2/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 1 4',
        'rn1qkbnr/pbp1pppp/1p1p4/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkbnr/pbp1pppp/1p6/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkbnr/pbppp1pp/1p6/5p2/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkbnr/p1pppppp/1p6/8/3P4/4Pb2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'r2qkbnr/pbpppppp/1pn5/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 1 4',
        'rn1qkbnr/pbppppp1/1p5p/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkbnr/1bpppppp/pp6/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkbnr/pb1ppppp/1p6/2p5/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkbnr/pb1ppppp/1pp5/8/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4',
        'rnbqkbnr/pp2p1pp/2p2p2/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'rn1qkbnr/ppp1p1pp/5p2/3p4/2PP2b1/5N2/PP2PPPP/RNBQKB1R w KQkq - 1 4',
        'rn1qkbnr/ppp1p1pp/4bp2/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 1 4',
        'rnbqkbnr/ppp3pp/5p2/3pp3/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'r1bqkbnr/ppp1p1pp/2n2p2/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 1 4',
        'rn1qkbnr/ppp1p1pp/5p2/3p1b2/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 1 4',
        'rnbqkbnr/pp2p1pp/5p2/2pp4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'rnbqkbnr/ppp1p2p/5pp1/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'rnbqkbnr/p1p1p1pp/1p3p2/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'rnbqkbnr/pp1ppp1p/6p1/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkbnr/pp2pppp/8/2pp4/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkbnr/p2ppppp/1p6/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3',
        'rnb1kbnr/ppqppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 1 3',
        'rnbqkbnr/pp1p1ppp/8/2p1p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkbnr/pp1pppp1/7p/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3',
        'rnb1kbnr/pp1ppppp/1q6/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 1 3',
        'rn1qkbnr/pbpppppp/1p6/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 1 3',
        'rnbqkbnr/2pppppp/1p6/p7/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkbnr/p1pp1ppp/1p2p3/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3',
        'rn1qkbnr/p1pppppp/bp6/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 1 3',
        'rnbqkbnr/p1pppp1p/1p4p1/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkb1r/p1pppppp/1p3n2/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 1 3',
        'rnbqkbnr/p1p1pppp/1p6/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkbnr/p2ppppp/1p6/2p5/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkbnr/p1p1pppp/1p1p4/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkbnr/p2ppppp/1pp5/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3',
        'rnbqkbnr/p1ppp1pp/1p6/5p2/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 0 3',
        'r1bqkbnr/p1pppppp/1pn5/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq - 1 3',
        'rn1qk1nr/ppp2ppp/4p3/3p1b2/1bPP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 2 5',
        'rn1qkbnr/pp3ppp/2p1p3/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 0 5',
        'rn1qkb1r/ppp2ppp/4pn2/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 2 5',
        'r2qkbnr/ppp2ppp/2n1p3/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 2 5',
        'rn1qkbnr/1pp2ppp/p3p3/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 0 5',
        'rn1qkbnr/ppp3pp/4pp2/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 0 5',
        'r2qkbnr/pppn1ppp/4p3/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 2 5',
        'rn1qk1nr/ppp1bppp/4p3/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 2 5',
        'rn1qk1nr/ppp2ppp/3bp3/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq - 2 5',
        'rnbqkbnr/pp2pppp/8/3p4/2Pp4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'rnbqkb1r/pp2pppp/5n2/2pp4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 1 4',
        'rn1qkbnr/pp2pppp/8/2pp1b2/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 1 4',
        'rnbqkbnr/pp3ppp/8/2ppp3/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'rnb1kbnr/pp2pppp/8/q1pp4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 1 4',
        'rnbqkbnr/pp2pp1p/6p1/2pp4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'rnbqkbnr/p3pppp/1p6/2pp4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4',
        'rnbqkbnr/pp2p1pp/5p2/2pp4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4'
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
