import chess

board = chess.Board()

# Make a move on the board
move = chess.Move.from_uci("e2e4")
board.push(move)

# Check if the game is over
if board.is_checkmate():
    print("Checkmate!")
elif board.is_stalemate():
    print("Stalemate")
elif board.is_insufficient_material():
    print("Insufficient material")
elif board.is_variant_draw():
    print("Variant draw")
else:
    print("The game is ongoing")

# Print the current state of the board
print(board)
