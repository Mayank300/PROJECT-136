from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def homepage():
    return jsonify({
        "message": "😊 success !!!", 
        "data": data
    }), 200
    # return 'working'
    
if __name__ == "__main__":
    app.run(debug=True)