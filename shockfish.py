import requests

class Stockfish:
    def __init__(self):
        self.URL = "https://stockfish.online/api/s/v2.php"
        self.METHOD = "GET"
        self.depth = 15
        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.Parameter = "&fen=" + self.fen + "&depth=" + str(self.depth)

    # Get the best move from the Stockfish engine
    def getMove(self):
        response = requests.request(self.METHOD, self.URL + "?" + self.Parameter)
        return response.text
    # Set the chess position in FEN format
    def setFen(self, fen):
        self.fen = fen
        self.Parameter = "&fen=" + self.fen + "&depth=" + str(self.depth)
    
if __name__ == "__main__":
    stockfish = Stockfish()
    print(stockfish.getMove())