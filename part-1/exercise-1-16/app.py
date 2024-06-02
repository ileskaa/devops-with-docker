import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello Helsinki University!"
@app.route('/waddup')
def hello_world():
    return 'How you doing?'

if __name__ == "__main__":
    app.run(debug=True)
