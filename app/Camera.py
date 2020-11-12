"""
A thread-safe data structure to store and send log messages
Author: Ivy Zhang
Date: 11/11/2020
"""
import threading
import time
import requests

class Camera:

    def __init__(self):
        self.shared_logs = [] #list of messages being generated every 10 second
        self.lock = threading.Lock()
        # lock: avoid multiple threads accessing the resource simultaneousl
        self.command_status = False
        #True: there is send_logs command from the server; False: no command

    def generate_logs(self):
        """
        Generate a log message and its timestamp every 10 seconds
        """
        t = threading.Timer(10.0, self.generate_logs)
        t.start()
        message = "Detect an object"
        timestamp = time.time()
        self.shared_logs.append((timestamp,message))
        print(self.shared_logs)

    def send_logs(self):
        """
        Send the current logs to the server
        """
        try:
            command = requests.get('http://127.0.0.1:5000/command')
            #Get the "send_logs" command in response
            if command.text == "send_logs":
                self.lock.acquire()
                self.command_status = True
                r = requests.post('http://127.0.0.1:5000/', data = self.shared_logs)
                #upload the current logs to the server
                self.command_status = False
                self.lock.release()
        except requests.ConnectionError as e:
            print(e)
            print("Can't conect to the web server!!!")
