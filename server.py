from flask import Flask, request
from stockfish import Stockfish

app = Flask(__name__)

webpage = ""
with open("webpages/webpage.html", "r") as file:
    webpage = file.read()

@app.route('/')
def main():
    return webpage 

@app.route('/getBestMove', methods=['GET'])
def getBestMove():
    fen = request.args.get('fen')
    stockfish = Stockfish()
    stockfish.setFen(fen)
    return stockfish.getBestMove()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8289, debug=True)