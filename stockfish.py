import requests

class Stockfish:
    def __init__(self):
        self.URL = "https://stockfish.online/api/s/v2.php"
        self.METHOD = "GET"
        self.depth = 15
        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.Parameter = "&fen=" + self.fen + "&depth=" + str(self.depth)

    # Set the chess position in FEN format
    def setFen(self, fen):
        self.fen = fen
        self.Parameter = "&fen=" + self.fen + "&depth=" + str(self.depth)
    
    # sets parameter for the API request
    def getParameter(self):
        return "&fen=" + self.fen + "&depth=" + str(self.depth)
    
    def ask_API(self):
        response = requests.request(self.METHOD, self.URL + "?" + self.getParameter())
        return response.text
    
    # Get the best move(s) from the Stockfish engine
    def getBestMoves(self):
        response = self.ask_API()
        best_moves = []
        moves = response.split()[1]

        while len(moves) > 3:
            if moves[2].isnumeric():
                best_moves.append(moves[:3])
                moves = moves[3:]
            else:
                best_moves.append(moves[:2])
                moves = moves[2:]
        else:
            best_moves.append(moves)
        return best_moves
    
    # Get the best move from the Stockfish engine
    def getBestMove(self):
        response = self.getBestMoves()
        return response[-1]
    
    """
    def getPonderMoves(self):
        response = self.ask_API()
        ponder_moves = []
        moves = response.split()[3]

        while len(moves) > 3:
            if moves[2].isnumeric():
                ponder_moves.append(moves[:3])
                moves = moves[3:]
            else:
                ponder_moves.append(moves[:2])
                moves = moves[2:]
        else:
            ponder_moves.append(moves)
        return ponder_moves

    def getPonderMove(self):
        response = self.getPonderMoves()
        return response[-1]
    """

    
if __name__ == "__main__":
    stockfish = Stockfish()
    print(stockfish.getBestMove())
    #print(stockfish.getPonderMoves())