from flask import Flask, Request, jsonify

app = Flask(__name__)

@app.route('/msg', methods = ['Post'])
def enviar():
