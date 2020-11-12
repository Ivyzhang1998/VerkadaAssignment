"""
An API server built in Flask that implements "GET/logs" functionality
Author: Ivy Zhang
Date: 11/11/2020
"""

from flask import Flask, render_template, request
from Camera import Camera
app = Flask(__name__)
command_status = False
camera = Camera()

@app.route('/' ,methods=['GET', 'POST'])
def index():
    global command_status
    if request.method == 'POST':
        command_status = True
        return "successfully requested!"
    return render_template('index.html')

@app.route('/command')
def command():
    global command_status
    global camera
    if command_status == True:
       command_status = False
       return "send_logs"
    return "don't send logs"


if __name__ == '__main__':
    camera.generate_logs()
    while True:
        camera.send_logs()
        app.run(debug=False)
        break
    print("haha")    
