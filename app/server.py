"""
An API server built in Flask that implements "GET/logs" functionality
Author: Ivy Zhang
Date: 11/11/2020
"""

from flask import Flask, render_template, request
from flask_apscheduler import APScheduler
from Camera import Camera
import json
import time
app = Flask(__name__)
camera = Camera()

@app.route('/' ,methods=['GET', 'POST'])
def index():
    """
    home page where the users are able to send requests
    """
    global camera
    if request.method == 'POST':
        camera.command_status = True
        data = request.get_json() #retrive the log messages in json form
        return "Successfully requested! "
    return render_template('index.html')

@app.route('/command')
def command():
    """
    camera sends request to check whether there is send_logs command
    """
    global camera
    if camera.command_status == True:
       return "send_logs"
    return "no command from the server"


if __name__ == '__main__':
    camera.generate_logs()
    scheduler = APScheduler()
    #Camera sends a request to the server every second
    scheduler.add_job(func=camera.send_logs, trigger='interval', id='job', seconds=1)
    scheduler.start()
    app.run(debug=False)
    scheduler.remove_job('job')
     #Camera stops making requests when the server shuts down
    print("Server has shut down!")
