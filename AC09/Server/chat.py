from flask import Flask, Request, jsonify

app = Flask(__name__)



@app.route('/')
def home():
    return True





if __name__ == "__main__":
    app.run(host="localhost",port=5000)