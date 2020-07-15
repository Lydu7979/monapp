# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World...!"

@app.route("/meteo")
def meteo():
    return "Il fait chaud!"

@app.route("/names")
def names():
    name = {
        
        'Name': ['Clement','Ludovic','Lise','Valerie'
                ]
    } 
    return jsonify(name)



if __name__ == "__main__":
    app.run(debug=True)