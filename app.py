import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome To my Demo with Docker!"

@app.route('/about')
def about():
    return '<h1>This is the about page</h1>'

@app.route('/film')
def film():
    return 'Go to netflix.com for more information'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)