"""
An API server built in Flask that implements "GET/logs" functionality
Author: Ivy Zhang
Date: 11/11/2020
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
