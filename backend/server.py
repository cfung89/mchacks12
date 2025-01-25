from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/user', methods=['POST'])
def user():
    response = request.get_json()
    return jsonify(response), 200

@app.route('/tasks', methods=['POST'])
def tasks():
    response = request.get_json()
    return response, 200

if __name__ == "__main__":
    app.run(debug=True)
