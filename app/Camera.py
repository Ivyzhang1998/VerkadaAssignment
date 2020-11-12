"""
A thread-safe data structure to store log messages
Author: Ivy Zhang
Date: 11/11/2020
"""
import threading
import time

shared_logs = []
lock = threading.Lock()


def generate_logs():
    t = threading.Timer(10.0, generate_logs)
    t.start()
    message = "Detect an object"
    timestamp = time.time()
    shared_logs.append((timestamp,message))
    print(shared_logs)

def send_logs():
    try:
        lock.acquire()
    finally:
        lock.release()

generate_logs()
