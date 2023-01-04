# This is the "Controller" and the server for pyservice1. Handles 1 route and responds with simple html
import time

import redis
from flask import Flask

app = Flask(__name__) # Server/controller starts
cache = redis.Redis(host='redis', port=6379) # Connects to Redis to registrers visits to Redis monitorering

"""Registrer 1 request to pyservice1 and saves this to Redis"""
def register_request():
    retries = 5
    while True:
        try:
            return cache.incr('pyservice1')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

"""Base route for loadbalancer runs the hello function"""
@app.route('/')
def hello():
    register_request() # Registrer visits from pyservice1 to Redis
    # Simple html response
    return '<h1>Hello from Docker!</h1><br> The container contacted runs pyservice1'