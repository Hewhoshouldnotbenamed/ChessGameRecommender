import chess.pgn
import random
import pandas as pd


def extract_moves_from_pgn_file(pgn_file_path):
    moves = []
    with open(pgn_file_path) as f:
        while True:
            game = chess.pgn.read_game(f)
            if game is None:
                break
            moves.extend([move.uci() for move in game.mainline_moves()])
    return moves

pgn_file_path = "C:/Users/PMLS/Downloads/lichess_pgn_2024.03.07_Azaan23_vs_tinache.uh2eZC89.pgn"
moves = extract_moves_from_pgn_file(pgn_file_path)
game = chess.pgn.read_game(open(pgn_file_path))
opening_user = game.headers["Opening"]

# Initialize recommended games list
recommended_games = []

# Criteria for recommended games
desired_elo = 1600

# The dataset for evaluation based recommendation is for 2013-January.
with open("C:/Users/PMLS/Downloads/lichess_db_standard_rated_2013-01.pgn") as f:
    while True:
        game_higher_rated = chess.pgn.read_game(f)
        if game_higher_rated is None:
            break
        
        # Extract game details
        white_elo = game_higher_rated.headers.get("WhiteElo")
        black_elo = game_higher_rated.headers.get("BlackElo")
        game_opening = game_higher_rated.headers.get("Opening")

        # Check if game details are valid
        if (white_elo and black_elo and game_opening == opening_user and
            white_elo.isdigit() and black_elo.isdigit() and
            int(white_elo) >= desired_elo and int(black_elo) >= desired_elo):
            recommended_games.append(game_higher_rated)

# Check if there are recommended games
if recommended_games:
   print("Recommended Game:", random.choice(recommended_games))
    
else:
    print("No recommended games found.")


