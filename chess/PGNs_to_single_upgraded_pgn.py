import io
import chess.pgn
from time import sleep
import requests
import sys
import pickle
from stockfish import Stockfish
import time

doing_black_reportoire = True

white_to_move_FENs = []
black_to_move_FENs = []
PGNs = [
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Bc4 Nf6 5. f3 * ",
        "1. Nf3 g6 2. d4 Bg7 3. Bf4 Nf6 * ",
        "1. Nf3 g6 2. e4 * ",
        "1. Nf3 g6 2. Nc3 Bg7 3. e4 * ",
        "1. Nf3 g6 2. h3 Bg7 3. d3 c5 * ",
        "1. Nf3 g6 2. d4 Bg7 3. e4 * ",
        "1. Nf3 g6 2. d4 Bg7 3. Nc3 Nf6 4. Bf4 d5 5. e3 O-O 6. Nb5 Na6 7. Nc3 Nh5 * ",
        "1. Nf3 g6 2. d4 Bg7 3. c4 Nf6 * ",
        "1. Nf3 g6 2. d4 Bg7 3. g3 d5 * ",
        "1. Nf3 g6 2. d4 Bg7 3. c3 Nf6 * ",
        "1. Nf3 g6 2. d4 Bg7 3. e3 Nf6 4. Bc4 d5 * ",
        "1. Nf3 g6 2. d4 Bg7 3. Bg5 c5 * ",
        "1. Nf3 g6 2. d4 Bg7 3. b3 c5 * ",
        "1. Nf3 g6 2. d4 Bg7 3. Nbd2 c5 * ",
        "1. d4 g6 2. e4 * ",
        "1. d4 g6 2. c4 Bg7 3. Be3 Nf6 4. Nf3 O-O * ",
        "1. d4 g6 2. c4 Bg7 3. e4 * ",
        "1. d4 g6 2. c4 Bg7 3. Bf4 c5 * ",
        "1. d4 g6 2. c4 Bg7 3. Nc3 Nf6 4. Nf3 * ",
        "1. d4 g6 2. c4 Bg7 3. e3 Nf6 4. Nc3 O-O 5. f3 d5 6. cxd5 Nxd5 7. Nxd5 Qxd5 8. e4 Qxd4 *",
        "1. d4 g6 2. c4 Bg7 3. Nf3 * ",
        "1. d4 g6 2. Bf4 Bg7 3. e3 Nf6 * ",
        "1. d4 g6 2. d5 Bg7 3. e4 * ",
        "1. d4 g6 2. Nf3 * ",
        "1. d4 g6 2. e3 Bg7 3. Nf3 * ",
        "1. d4 g6 2. e3 Bg7 3. g3 d5 * ",
        "1. d4 g6 2. Nc3 Bg7 3. Be3 d5 * ",
        "1. g3 g6 2. Bg2 Bg7 3. h4 Nf6 4. h5 * ",
        "1. g3 g6 2. Nc3 Bg7 3. Bg2 * ",
        "1. g3 g6 2. Bg2 Bg7 3. Nc3 c5 4. Nf3 Nf6 * ",
        "1. g3 g6 2. Bg2 Bg7 3. d4 d5 * ",
        "1. g3 g6 2. Bg2 Bg7 3. c4 c5 * ",
        "1. g3 g6 2. Bg2 Bg7 3. Nf3 c5 * ",
        "1. g3 g6 2. Bg2 Bg7 3. e4 c5 * ",
        "1. g3 g6 2. Bg2 Bg7 3. d3 d5 * ",
        "1. g3 g6 2. Bg2 Bg7 3. f4 d5 * ",
        "1. g3 g6 2. Bg2 Bg7 3. a3 d5 * ",
        "1. f4 g6 2. Nf3 Bg7 3. e3 Nf6 * ",
        "1. f4 g6 2. Nf3 Bg7 3. e4 * ",
        "1. Nc3 g6 2. Nf3 * ",
        "1. b3 g6 2. Bb2 Nf6 3. Bxf6 exf6 * ",
        "1. e3 g6 2. d4 * ",
        "1. e3 g6 2. Nc3 Bg7 3. b3 d5 4. Bb2 c5 * ",
        "1. e3 g6 2. b3 Bg7 3. Nc3 * ",
        "1. e4 g6 2. Nc3 Bg7 3. Nf3 c5 4. e5 Nc6 5. Bc4 Nxe5 6. Ng5 Nxc4 * ",
        "1. e4 g6 2. Nc3 Bg7 3. Nd5 c6 * ",
        "1. e4 g6 2. Nc3 Bg7 3. f4 c5 4. Nf3 Nc6 * ",
        "1. e4 g6 2. Nc3 Bg7 3. d4 * ",
        "1. e4 g6 2. Nc3 Bg7 3. Nf3 c5 4. Bc4 Nc6 5. O-O * ",
        "1. e4 g6 2. Nc3 Bg7 3. Nf3 c5 4. d4 cxd4 5. Nxd4 Nc6 6. Nxc6 bxc6 * ",
        "1. e4 g6 2. e5 Bg7 3. d4 * ",
        "1. e4 g6 2. f4 Bg7 3. f5 d5 4. fxg6 hxg6 * ",
        "1. e4 g6 2. f4 Bg7 3. Nf3 c5 4. d3 Nf6 * ",
        "1. e4 g6 2. f4 Bg7 3. f5 d5 4. exd5 Bxf5 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d4 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Bb5 c5 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Bc4 c5 4. Ng5 e6 5. d4 cxd4 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Bc4 c5 4. c3 e6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Bc4 c5 4. d4 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Bc4 c5 4. O-O d6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Bc4 c5 4. Ne5 Bxe5 5. d3 Nf6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Bc4 c5 4. Ng5 e6 5. d3 d5 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Bc4 c5 4. Ng5 e6 5. Qf3 Qxg5 6. O-O Qd8 * ",
        "1. e4 g6 2. Nf3 Bg7 3. h3 c5 * ",
        "1. e4 g6 2. Nf3 Bg7 3. Nc3 * ",
        "1. e4 g6 2. Nf3 Bg7 3. c4 c5 4. d4 * ",
        "1. e4 g6 2. Nf3 Bg7 3. c3 e5 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Be2 Nc6 5. c3 Nf6 6. h3 e5 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. c3 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. g3 Nf6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Nc3 Nf6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Nbd2 Nf6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. c4 Nc6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Be3 Bxb2 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. h3 Nc6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. h4 Nf6 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. d4 cxd4 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Bd2 Bxb2 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Bf4 Bxb2 * ",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Be2 Nc6 5. c3 Nf6 6. e5 Nd5 7. c4 Nc7 8. d4 cxd4 9. e6 dxe6 *",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Be2 Nc6 5. c3 Nf6 6. e5 Nd5 7. c4 Nc7 8. d4 cxd4 9. Nxd4 Nxd4 10. Qxd4 d6 11. exd6 Bxd4 *",
        "1. e4 g6 2. Nf3 Bg7 3. d3 c5 4. Be2 Nc6 5. c3 Nf6 6. e5 Nd5 7. c4 Nc7 8. d4 cxd4 9. Nxd4 Nxd4 10. Qxd4 d6 11. c5 Bxe5 12. Qa4+ Bd7 *",
        "1. e4 g6 2. Bc4 Bg7 3. Nf3 * ",
        "1. e4 g6 2. Bc4 Bg7 3. g4 Nf6 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. d3 c6 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. Ne2 c5 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. c3 c5 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. Nh3 Nc6 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. d4 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. h4 Nc6 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. Be2 d5 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. a3 Nc6 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. Bb3 b5 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. Qb3 Ne7 * ",
        "1. e4 g6 2. Bc4 Bg7 3. Qf3 e6 4. h3 Nc6 * ",
        "1. e4 g6 2. f3 Bg7 3. Bc4 e6 * ",
        "1. e4 g6 2. d3 Bg7 3. Nf3 * ",
        "1. e4 g6 2. b3 Bg7 3. Nc3 c5 * ",
        "1. e4 g6 2. Qf3 Bg7 3. Bc4 * ",
        "1. e4 g6 2. g4 Bg7 3. h3 d5 * ",
        "1. e4 g6 2. g4 Bg7 3. Bc4 * ",
        "1. e4 g6 2. g4 Bg7 3. d3 d5 * ",
        "1. e4 g6 2. g4 Bg7 3. c3 d5 * ",
        "1. e4 g6 2. g4 Bg7 3. f3 e5 * ",
        "1. e4 g6 2. g4 Bg7 3. Nf3 d5 * ",
        "1. e4 g6 2. g4 Bg7 3. Nc3 Nc6 * ",
        "1. e4 g6 2. g4 Bg7 3. f4 e5 * ",
        "1. e4 g6 2. g4 Bg7 3. g5 d5 * ",
        "1. e4 g6 2. g4 Bg7 3. Bg2 d5 4. exd5 Nf6 5. c4 Bxg4 6. f3 Bf5 * ",
        "1. e4 g6 2. g4 Bg7 3. h4 d5 * ",
        "1. e4 g6 2. g4 Bg7 3. d4 d5 * ",
        "1. e4 g6 2. c4 Bg7 3. Nf3 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bd3 Nf6 5. e5 dxe5 6. dxe5 Nd5 7. c4 Nb4 8. Be4 Qxd1+ *",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. c4 Bg4 5. h3 Bxf3 6. Qxf3 Bxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. c4 Bg4 5. Be2 Bxf3 6. Bxf3 c6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. c3 Nf6 5. Ng5 h6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. e5 Ng4 6. exd6 Nxe3 7. fxe3 exd6 *",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. Bd3 Nbd7 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. Bc4 Nxe4 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. Qd2 Nbd7 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. h3 a6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. Be2 a6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. e5 Ng4 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. h4 c5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. Qd3 c6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. Qe2 c6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. g3 c5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. Qc1 c5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Nc3 O-O 6. a3 Nbd7 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Be3 Nf6 5. Bd3 O-O 6. O-O d5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. e5 dxe5 5. dxe5 Qxd1+ 6. Kxd1 Bg4 7. Be2 Nc6 8. Bf4 Bxf3 *",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. e5 dxe5 5. Nc3 exd4 6. Ne4 e5 7. Bd3 f5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. d5 c6 5. Nc3 Nf6 6. dxc6 O-O 7. Bd3 bxc6 8. Ng5 e5 *",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Nc3 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bf4 Nf6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bg5 c5 5. Bb5+ Bd7 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. b3 c5 5. Bb2 Nf6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. b3 c5 5. dxc5 Bxa1 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bb5+ c6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bc4 Nf6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bd3 Nf6 5. O-O Nc6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bd3 Nf6 5. c3 Nbd7 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bd3 Nf6 5. Nbd2 c5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bd3 Nf6 5. h3 O-O * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bd3 Nf6 5. Nc3 * ",
        "1. e4 g6 2. d4 Bg7 3. Nf3 d6 4. Bd3 Nf6 5. c4 Bg4 * ",
        "1. e4 g6 2. d4 Bg7 3. Be3 d6 4. Nf3 * ",
        "1. e4 g6 2. d4 Bg7 3. c3 d6 4. Be3 Nf6 5. Bd3 O-O * ",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. Bf4 dxe5 5. dxe5 Qxd1+ 6. Kxd1 Nc6 7. g3 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. e6 dxe6 5. dxc5 Qxd1+ 6. Kxd1 Nd7 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. c3 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. Nf3 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. f4 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. Be3 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. dxc5 Bxe5 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. d5 Bxe5 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. Bc4 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. Nc3 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. Bf4 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 c5 4. c4 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. f4 dxe5 5. fxe5 c5 6. Nf3 cxd4 7. Nxd4 Bxe5 8. Nf3 $2 Qxd1+ 9. Kxd1 Bg7 10. Bb5+ Nd7 11. Re1 a6 12. Bxd7+ Bxd7 13. Na3 Nf6 14. Be3 Ng4 *",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. f4 dxe5 5. fxe5 c5 6. c3 Nc6 7. d5 Nxe5 8. Qa4+ Bd7 9. Qb3 e6 10. Qxb7 Rb8 *",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. f4 dxe5 5. fxe5 c5 6. Be3 Nh6 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. f4 dxe5 5. fxe5 c5 6. Nf3 cxd4 7. c3 Nc6 8. cxd4 Qb6 *",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. exd6 cxd6 5. d5 Qa5+ 6. c3 Nd7 7. b4 Qc7 8. Bb2 a5 9. c4 Bxb2 *",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. exd6 cxd6 5. d5 Qa5+ 6. c3 Nd7 7. b4 Qc7 8. Bb5 Nf6 9. c4 a6 10. Ba4 Nh5 11. Bc2 Bxa1 *",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. Nf3 * ",
        "1. e4 g6 2. d4 Bg7 3. e5 d6 4. Bf4 dxe5 5. dxe5 Qxd1+ 6. Kxd1 Nc6 7. Nf3 Bg4 8. h3 Bxf3+ 9. gxf3 Bxe5 10. Bb5 O-O-O+ *",
        "1. e4 g6 2. d4 Bg7 3. Qf3 e6 4. Bc4 Bxd4 5. c3 Bg7 6. Bh6 Nxh6 * ",
        "1. e4 g6 2. d4 Bg7 3. f4 c5 4. dxc5 Qa5+ * ",
        "1. e4 g6 2. d4 Bg7 3. Bf4 c5 4. c3 Qb6 5. Qd2 cxd4 * ",
        "1. e4 g6 2. d4 Bg7 3. c4 d6 4. Nf3 * ",
        "1. e4 g6 2. d4 Bg7 3. c4 d6 4. Nc3 Nf6 * ",
        "1. e4 g6 2. d4 Bg7 3. d5 e6 4. dxe6 fxe6 * ",
        "1. e4 g6 2. d4 Bg7 3. d5 e6 4. Qd2 Nf6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. f3 Nf6 5. Be3 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. e5 dxe5 6. dxe5 Qxd1+ 7. Nxd1 Ng4 8. e6 Bxe6 9. Bb5+ Nd7 10. Bd2 a6 11. Ba4 Ne5 *",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. h3 a6 6. Bd3 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. h3 a6 6. Bc4 b5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. h3 a6 6. a4 O-O * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. h3 a6 6. Bg5 b5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. h3 a6 6. Be2 O-O * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. h3 a6 6. a3 b5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. h3 a6 6. Bf4 c5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. h3 a6 6. e5 dxe5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. Bf4 O-O 6. Bc4 Nxe4 7. Nxe4 d5 8. Qe2 dxc4 9. Qxc4 *",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. Bc4 O-O 6. Bf4 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. Bd3 O-O * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. Bd3 Nc6 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. d5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. e5 dxe5 6. Nxe5 * ",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. e5 dxe5 6. dxe5 Qxd1+ 7. Nxd1 Ng4 8. Bf4 Nc6 9. Nc3 Ngxe5 10. Nxe5 Bxe5 11. Bxe5 Nxe5 *",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Nf3 Nf6 5. e5 dxe5 6. dxe5 Qxd1+ 7. Nxd1 Ng4 8. h3 Nxe5 9. Nxe5 Bxe5 10. Bc4 Nc6 *",
        "1. e4 g6 2. d4 Bg7 3. Nc3 d6 4. Bd3 Nc6 5. d5 Ne5 * "
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
            black_to_move_FENs[get_pgn_from_moves(current_moves)] = {'fen': board.fen(),'move list' : current_moves}
        else:
            white_to_move_FENs[get_pgn_from_moves(current_moves)] = {'fen': board.fen(),'move list' : current_moves}
         

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


stockfish = Stockfish("/root/stockfishengine/stockfish_14_x64_avx2")

stockfish = Stockfish(parameters={"Threads":15,"Hash": 104537,"Write Debug Log": "true"})

print(stockfish.get_parameters())

stockfish.set_depth(40)

localtime = time.localtime()
result = time.strftime("%I:%M:%S %p", localtime)
print(result)

to_consolidate = {}
for fen in to_analyze:
    stockfish.set_fen_position(fen)
    
    best_move_uci = stockfish.get_best_move())
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    
    to_print = fen + "\t" + \
               to_analyze[fen] + "\t" + \
               best_move_uci + "\t" + \
               result
               
    to_consolidate[fen] = str(best_move_uci)        
    print(to_print)

'''
the below code should take no more than a few minutes
'''
gamesPGN = []
for pgn, bestresponse in to_consolidate.items():
    game = chess.pgn.read_game(io.StringIO(pgn))
    game.end().add_variation(chess.Move.from_uci(bestresponse))
    gamesPGN.append(str(game[-1]))

# A significant amount of the below code comes from Aven Bross
# https://github.com/permutationlock/merge-pgn
# their code is under the MIT license
# Description: A simple tool to merge several pgn games into a single game with
# variations.

games = []
for pgn in gamesPGN:
    game = chess.pgn.read_game(io.StringIO(pgn))
    if game is not None:
        games.append(game)
        game = chess.pgn.read_game(io.StringIO(pgn))

master_node = chess.pgn.Game()
mlist = []
for game in games:
    mlist.extend(game.variations)

variations = [(master_node, mlist)]
done = False

while not done:
    newvars = []
    done = True
    for vnode, nodes in variations:
        newmoves = {}
        for node in nodes:
            if node.move is None:
                continue
            elif node.move not in list(newmoves):
                nvnode = vnode.add_variation(node.move)
                if len(node.variations) > 0:
                    done = False
                newvars.append((nvnode, node.variations))
                newmoves[node.move] = len(newvars) - 1
            else:
                nvnode, nlist = newvars[newmoves[node.move]]
                if len(node.variations) > 0:
                    done = False
                nlist.extend(node.variations)
                newvars[newmoves[node.move]] = (nvnode, nlist)
    variations = newvars

print(master_node)

if doing_black_reportoire == True:
    filename = "black_reportoire.pgn"
else: 
    filename = "white_reportoire.pgn"

with open(filename, "w") as f:
    f.write(str(masternode))