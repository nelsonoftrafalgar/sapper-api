from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS, cross_origin
from board_generator import BoardGenerator

app = Flask(__name__)
cors = CORS(app)

@app.route('/api')
@cross_origin()
def api():
    level = float(request.args.get('level'))
    rows = int(request.args.get('rows'))
    cols = int(request.args.get('cols'))
    board_generator = BoardGenerator(rows, cols, level)
    return {'board': board_generator.board}

if __name__ == '__main__':
    app.run()
