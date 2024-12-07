from flask import Flask, request, jsonify
app = Flask(__name__)
from flask_sqlalchemy import SLQAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), unique=True, nullable=False)
    balance = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name} - {self.balance}"


@app.route('/balance')
def get_balance():
    return balance

@app.route('/add-money', methods=['POST'])
def add_money():

    return 

if __name__ == "__main__":
    app.run(debug=True)