'''
This is responsible for storing all the data about the current state of a chess game, also responsible for detecting the legal moves for the current state.It was also keep a move log.
'''
class game_state():
    def _init_(self):
        # board is an 8x8 Lis,each element of the list has 2 characters
        # first character represents colour of piece i.e. 'b' for black and 'w' for white
        # second character represents type of piece i.e 'R' for rook, 'N' for knight, 'B' for bishop
        # 'Q' for queen, 'K' for king and 'p' for pawn
        # "--" represents an empty space  
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.white_to_move = True
        self.move_log = []