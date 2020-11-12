"""
A thread-safe data structure to store log messages
Author: Ivy Zhang
Date: 11/11/2020
"""
import threading
import time
import requests

class Camera:

    def __init__(self):
        self.shared_logs = []
        self.lock = threading.Lock()
        self.command_status = False

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
    #    self.lock.acquire()
            command = requests.get('http://127.0.0.1:5000/command')
            if command.text == "send_logs": #Get the "send_logs" command in response
                self.command_status = True
                r = requests.post('http://127.0.0.1:5000/', data = self.shared_logs)
                print(r)
                #upload the current logs to the server
                self.command_status = False
            print(command.text)
        except requests.ConnectionError as e:
            print(e)
            print("Can't conect to the web server!!!")
    #    self.lock.release()

if __name__ == "__main__":
    c = Camera()
    c.send_logs()
