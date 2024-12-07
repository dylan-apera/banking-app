from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add-money", methods=["POST"])
def add_money():
    return 0

#To be continued