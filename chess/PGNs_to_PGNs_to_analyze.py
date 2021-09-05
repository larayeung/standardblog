import io
import chess.pgn
from time import sleep
import requests
import sys
import pickle
import time

doing_black_reportoire = False

white_to_move_FENs = []
black_to_move_FENs = []
PGNs = [
        "1. Nf3 d5 2. d4 e6 3. c4 Nf6 4. Nc3 dxc4 5. e4 Bb4 6. Bg5 * ",
        "1. Nf3 c5 2. e4 e6 3. Nc3 * ",
        "1. Nf3 c5 2. e4 d6 3. Bb5+ Bd7 4. Bxd7+ Nxd7 * ",
        "1. Nf3 c5 2. e4 d6 3. Bb5+ Nd7 4. a4 * ",
        "1. Nf3 c5 2. e4 d6 3. Bb5+ Bd7 4. Bxd7+ Qxd7 * ",
        "1. Nf3 c5 2. e4 Nc6 3. d4 * ",
        "1. Nf3 c5 2. e4 Nf6 * ",
        "1. Nf3 c5 2. e4 a6 * ",
        "1. Nf3 c5 2. e4 g6 3. d4 * ",
        "1. Nf3 c5 2. e4 d5 3. exd5 * ",
        "1. Nf3 c5 2. e4 b6 3. d4 * ",
        "1. Nf3 c5 2. e4 Qc7 3. c3 * ",
        "1. Nf3 c5 2. e4 e5 3. Nxe5 * ",
        "1. Nf3 c5 2. e4 h6 3. c4 * ",
        "1. Nf3 c5 2. e4 Qb6 3. d4 * ",
        "1. Nf3 g6 2. d4 Bg7 3. e4 d6 * ",
        "1. Nf3 g6 2. d4 Bg7 3. e4 c6 4. c4 d5 5. e5 dxc4 6. Bxc4 * ",
        "1. Nf3 g6 2. d4 Bg7 3. e4 e6 4. Nc3 * ",
        "1. Nf3 e5 2. Nxe5 Nc6 3. Nxc6 dxc6 4. e4 Bc5 5. d3 Nf6 6. Be2 Ng4 7. Bxg4 Bxg4 8. Qxg4 Qd7 9. Qxd7+ Kxd7 *",
        "1. Nf3 e5 2. Nxe5 d6 3. Nf3 Bf5 4. c4 * ",
        "1. Nf3 e5 2. Nxe5 d6 3. Nf3 d5 4. d4 Bf5 5. c4 * ",
        "1. Nf3 e5 2. Nxe5 d6 3. Nf3 Nc6 4. e3 * ",
        "1. Nf3 e5 2. Nxe5 Nf6 3. d4 d6 4. Nf3 d5 5. Bg5 * ",
        "1. Nf3 e5 2. Nxe5 Nc6 3. Nxc6 dxc6 4. e4 Nf6 5. Qe2 * ",
        "1. Nf3 e5 2. Nxe5 Nc6 3. Nxc6 dxc6 4. e4 Bc5 5. d3 Nf6 6. Be2 h5 7. c3 Qd6 8. d4 *",
        "1. Nf3 e5 2. Nxe5 Nc6 3. Nxc6 dxc6 4. e4 Bc5 5. d3 Nf6 6. Be2 Ng4 7. Bxg4 Qh4 8. O-O Bxg4 9. Qe1 O-O *",
        "1. Nf3 c6 2. d4 e5 3. dxe5 * ",
        "1. Nf3 c6 2. d4 d5 * ",
        "1. Nf3 c6 2. d4 a5 3. e4 a4 4. c4 b5 5. cxb5 e6 6. Nc3 Bb4 7. Bd3 * ",
        "1. Nf3 Nc6 2. d4 e5 3. d5 Nb4 4. a3 Na6 5. Nxe5 * ",
        "1. Nf3 Nc6 2. d4 d5 * ",
        "1. Nf3 Nc6 2. d4 Nf6 3. c4 e5 * ",
        "1. Nf3 Nc6 2. d4 Nf6 3. c4 d5 * ",
        "1. Nf3 Nc6 2. d4 e6 3. a3 * ",
        "1. Nf3 Nc6 2. d4 d6 3. e4 Bg4 4. c3 * ",
        "1. Nf3 Nc6 2. d4 g6 3. d5 Nb4 4. Qd2 a5 5. e4 Bg7 * ",
        "1. Nf3 Nc6 2. d4 e5 3. d5 e4 4. Ng5 Ne5 5. Nxe4 * ",
        "1. Nf3 Nc6 2. d4 e5 3. d5 e4 4. Ng5 f6 5. Nxe4 * ",
        "1. Nf3 Nc6 2. d4 e5 3. d5 e4 4. Ng5 e3 5. Bxe3 * ",
        "1. Nf3 Nc6 2. d4 e5 3. d5 e4 4. Ng5 Nce7 5. Nxe4 * ",
        "1. Nf3 Nc6 2. d4 e5 3. d5 e4 4. Ng5 Nf6 5. dxc6 * ",
        "1. Nf3 Nc6 2. d4 e5 3. d5 Bb4+ 4. c3 * ",
        "1. Nf3 h6 2. d4 a6 3. e4 d5 4. exd5 Qxd5 5. c4 * ",
        "1. Nf3 a6 2. d4 c6 * ",
        "1. Nf3 a6 2. d4 c5 3. d5 Nf6 4. c4 b5 5. Nbd2 * ",
        "1. Nf3 e6 2. d4 Be7 3. e4 * ",
        "1. Nf3 e6 2. d4 d5 * ",
        "1. Nf3 e6 2. d4 b6 3. e4 * ",
        "1. Nf3 e6 2. d4 Qf6 3. e4 * ",
        "1. Nf3 b6 2. d4 e6 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 e6 4. c4 * ",
        "1. Nf3 b6 2. d4 Bb7 3. c4 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 g6 4. Bd3 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 Nf6 4. c4 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 d6 4. Bd3 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 d5 4. c4 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 f5 4. Be2 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 Bxf3 4. Qxf3 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 Nc6 4. d5 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 h6 4. Bd3 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 a6 4. Nbd2 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 c5 4. d5 * ",
        "1. Nf3 b6 2. d4 Bb7 3. e3 c6 4. e4 * ",
        "1. Nf3 b6 2. d4 a5 3. e4 * ",
        "1. Nf3 b6 2. d4 Ba6 3. e4 * ",
        "1. Nf3 b6 2. d4 g6 3. e4 * ",
        "1. Nf3 b6 2. d4 Nf6 3. g3 * ",
        "1. Nf3 b6 2. d4 d5 3. c4 * ",
        "1. Nf3 b6 2. d4 c5 3. d5 * ",
        "1. Nf3 b6 2. d4 d6 3. e4 * ",
        "1. Nf3 b6 2. d4 c6 3. e4 * ",
        "1. Nf3 b6 2. d4 f5 3. Bg5 * ",
        "1. Nf3 b6 2. d4 Nc6 3. d5 * ",
        "1. Nf3 d6 2. d4 Nf6 3. c4 g6 4. Nc3 Bg7 5. e4 c5 6. d5 O-O 7. h3 * ",
        "1. Nf3 d6 2. d4 Nc6 * ",
        "1. Nf3 d6 2. d4 Bg4 3. e4 * ",
        "1. Nf3 d6 2. d4 e6 3. e4 e5 4. dxe5 dxe5 5. Qxd8+ Kxd8 6. Nxe5 Ke7 7. Be3 * ",
        "1. Nf3 d6 2. d4 d5 3. c4 Nf6 * ",
        "1. Nf3 Nf6 2. d4 Nc6 * ",
        "1. Nf3 Nf6 2. d4 d5 * ",
        "1. Nf3 Nf6 2. d4 g6 3. c4 Bg7 4. Nc3 c5 5. d5 O-O 6. Qc2 * ",
        "1. Nf3 Nf6 2. d4 g6 3. c4 Bg7 4. Nc3 O-O 5. e4 d6 6. Be3 c5 7. h3 * ",
        "1. Nf3 h5 2. d4 g6 3. e4 e6 4. Nc3 * ",
        "1. Nf3 f6 2. d4 d5 * ",
        "1. Nf3 f6 2. d4 Nh6 * ",
        "1. Nf3 f6 2. d4 d6 * ",
        "1. Nf3 d5 2. d4 e5 3. dxe5 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 dxc4 4. e3 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 c6 4. Nc3 Bf5 5. cxd5 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 c6 4. Nc3 Bg4 5. Ne5 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 Bg4 4. Ne5 Qd6 5. Nxg4 Nxg4 6. e4 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 e6 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 Nc6 4. cxd5 Qxd5 5. Nc3 Qd8 6. e4 e6 7. a3 Be7 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 Nc6 4. cxd5 Nxd5 5. e4 Nb6 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 Nc6 4. cxd5 Qxd5 5. Nc3 Qa5 6. Bd2 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 Ne4 4. cxd5 Qxd5 5. e3 * ",
        "1. Nf3 d5 2. d4 Nf6 3. c4 Bf5 4. Qb3 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 e5 4. Nxe5 Nxe5 5. dxe5 Bb4+ 6. Nd2 dxc4 7. Qa4+ Qd7 8. Qxb4 *",
        "1. Nf3 d5 2. d4 Nc6 3. c4 Nf6 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 Bg4 4. cxd5 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 dxc4 4. d5 Nb8 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 dxc4 4. d5 Nb4 5. Qa4+ Nc6 6. dxc6 bxc6 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 dxc4 4. d5 Nb4 5. Qa4+ Bd7 6. Qxb4 b6 7. Qxc4 e6 8. dxe6 *",
        "1. Nf3 d5 2. d4 Nc6 3. c4 dxc4 4. d5 Nb4 5. Qa4+ Qd7 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 dxc4 4. d5 Nb4 5. Qa4+ Nc6 6. dxc6 b6 7. Bf4 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 dxc4 4. d5 Na5 5. Qa4+ c6 6. Bd2 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 dxc4 4. d5 Nf6 5. dxc6 Qxd1+ 6. Kxd1 bxc6 7. Nc3 *",
        "1. Nf3 d5 2. d4 Nc6 3. c4 e6 4. a3 Bd6 5. Nc3 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 e6 4. a3 Nf6 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 Be6 4. Ng5 * ",
        "1. Nf3 d5 2. d4 Nc6 3. c4 Bf5 4. cxd5 Nf6 5. dxc6 * ",
        "1. Nf3 d5 2. d4 c6 3. c4 dxc4 4. e3 * ",
        "1. Nf3 d5 2. d4 c6 3. c4 Nf6 * ",
        "1. Nf3 d5 2. d4 c6 3. c4 Qa5+ 4. Nc3 * ",
        "1. Nf3 d5 2. d4 c6 3. c4 Bf5 * ",
        "1. Nf3 d5 2. d4 c6 3. c4 e6 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 dxc4 5. e4 Bg4 6. Be3 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 dxc4 4. e3 Nf6 5. Bxc4 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 c5 5. Qb3 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 Bb4 5. cxd5 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 c6 5. Qb3 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 Nf6 5. cxd5 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 Nc6 5. Bf4 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 a6 5. Qb3 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 f6 5. Nh4 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 Nd7 5. cxd5 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 Be7 5. cxd5 * ",
        "1. Nf3 d5 2. d4 Bf5 3. c4 e6 4. Nc3 Bd6 5. Qb3 * ",
        "1. Nf3 d5 2. d4 Bg4 3. Ne5 Qd6 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 e6 4. Nc3 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 dxc4 4. e4 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 c6 4. Nc3 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 Bg4 4. Qb3 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 Be6 4. cxd5 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 e5 4. dxe5 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 Nc6 4. cxd5 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 Bf5 4. cxd5 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 c5 4. cxd5 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 g6 4. cxd5 * ",
        "1. Nf3 d5 2. d4 f6 3. c4 b6 4. cxd5 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 Nc6 4. cxd5 Nb4 5. e4 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 Bg4 4. Ne5 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 e6 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 dxc4 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 cxd4 4. cxd5 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 Nf6 4. cxd5 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 Bf5 4. cxd5 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 e5 4. dxe5 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 Qa5+ 4. Bd2 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 g6 4. dxc5 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 b6 4. cxd5 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 f6 * ",
        "1. Nf3 d5 2. d4 c5 3. c4 Nc6 4. cxd5 Qxd5 5. Nc3 Qd8 6. d5 Nd4 7. Nxd4 cxd4 8. Qxd4 e6 9. e4 *",
        "1. Nf3 d5 2. d4 e6 3. c4 c5 4. cxd5 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 Bb4+ 4. Nbd2 Nc6 5. a3 Bd6 6. c5 Bf4 7. e3 Bg5 8. b4 *",
        "1. Nf3 d5 2. d4 e6 3. c4 dxc4 4. e3 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 Bb4 5. a3 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 Nf6 5. Qc2 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 f5 5. g3 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 Bd6 5. e4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 Nd7 5. e4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 dxc4 5. Nxc4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 a6 5. e4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 Be7 5. e4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 g6 5. e4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 h6 5. e4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 Ne7 5. e4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 c6 4. Nbd2 b6 5. e4 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 g5 4. Bxg5 f6 5. Bf4 e5 6. dxe5 fxe5 7. Bxe5 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 Nf6 4. Nc3 Bb4 5. Qa4+ Qd7 6. Qxb4 Na6 7. Qb3 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 Nf6 4. Nc3 Bb4 5. Qa4+ Nc6 6. Bd2 O-O 7. a3 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 Nf6 4. Nc3 Bb4 5. Qa4+ Qd7 6. Qxb4 Nc6 7. Qa4 O-O *",
        "1. Nf3 d5 2. d4 e6 3. c4 Nf6 4. Nc3 Be7 5. cxd5 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 Nf6 4. Nc3 Nc6 5. a3 * ",
        "1. Nf3 d5 2. d4 e6 3. c4 Nf6 4. Nc3 dxc4 5. e4 Nc6 * "
        ]

def get_pgn_from_moves(moves):
    
    game = chess.pgn.Game()
    
    if len(moves) == 1 or len(moves) % 2 == 1:
        moves.append("")
    
    it = iter(moves)
    move_pairs = zip(it, it)
    
    pgn = ""
    count = 1
    for pair in move_pairs:
        text_to_add = str(count) + \
                      "." + \
                      pair[0] + \
                      " " + \
                      pair[1] +\
                      " "
                      
        pgn += text_to_add
                       
    
        count += 1
        
    return pgn

def get_pgn_from_moves_plus_uci(pgn,uci_move):
    game = chess.pgn.read_game(io.StringIO(pgn))
    board = game.board()
    
    for move in game.mainline_moves():
        current_moves.append(board.san(move))
        board.push(move)
    board.push((chess.Move.from_uci(uci_move)))

    game2 = chess.pgn.read_game(io.StringIO(pgn))
    game2.end().add_variation(chess.Move.from_uci(uci_move))
    
    return (str(game2[-1]), board.fen())

def move_already_included(uci_move,fen,someFENs):

    board = chess.Board(fen)
    board.push((chess.Move.from_uci(uci_move)))
    
    if board.fen() in someFENs:
        already_included = True
    elif board.fen() not in someFENs:
        already_included = False
    
    return already_included

white_to_move_FENs = {}
black_to_move_FENs = {}
for pgn in PGNs:
    
    game = chess.pgn.read_game(io.StringIO(pgn))
    board = game.board()
    
    current_moves = []
    
    for move in game.mainline_moves():
        current_moves.append(board.san(move))
        board.push(move)
        
        white_to_move = board.turn
        
        if white_to_move == True:
            white_to_move_FENs[get_pgn_from_moves(current_moves)] = {'fen': board.fen(),'move list' : current_moves}
        else:
            black_to_move_FENs[get_pgn_from_moves(current_moves)] = {'fen': board.fen(),'move list' : current_moves}
         

#if you're doing the Modern Defense (black), you're going to want to find common responses
#to what black is doing
#so, FENs should be when white is to move as the code blocks below will find moves for white
if doing_black_reportoire == True:
    FENs = white_to_move_FENs
    other_FENs = black_to_move_FENs
else:
    FENs = black_to_move_FENs
    other_FENs = white_to_move_FENs

to_analyze = {} 
number_of_unique_positions = 0   
for pgn in FENs:
    sleep(1)
    fen = FENs[pgn]['fen']
    
    url = "https://explorer.lichess.ovh/lichess?" + \
          "variant=standard&" + \
          "speeds[]=blitz&speeds[]=rapid&speeds[]=classical&" + \
          "ratings[]=1600&ratings[]=1800&ratings[]=2000&ratings[]=2200&ratings[]=2500&" + \
          "recentGames=0&moves=20&topGames=0&fen=" + \
          fen
    r = requests.get(url)
    print("requesting...")
    dictResponse =  r.json()
    
    for item in dictResponse['moves']:
        common_move = item['uci']
        totalgames = item['white'] + item['black'] + item['draws']
        
        if totalgames <= 10000 or move_already_included(common_move,fen,other_FENs) == True: 
            continue
        else:
            pgn_to_analyze, fen_to_analyze = get_pgn_from_moves_plus_uci(pgn,common_move)
            to_analyze[fen_to_analyze] = pgn_to_analyze
            
            print(pgn_to_analyze + " : " + fen_to_analyze)
            pass
    number_of_unique_positions += 1

print("total number of position to analyze: " + str(number_of_unique_positions)) 

with open('to_analyze.pickle', 'wb') as handle:
    pickle.dump((to_analyze,doing_black_reportoire), handle, protocol=pickle.HIGHEST_PROTOCOL)
    
sys.exit()

