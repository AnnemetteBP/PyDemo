# The "Controlleren" and server for pyservice2 responsible for handeling 1 route and reply with simple html.
import time

import redis
from flask import Flask

app = Flask(__name__) # Server/controller starts
cache = redis.Redis(host='redis', port=6379) # Redis connection for registrering visits to Redis for monitorering

"""Registreing 1 request to service and saves to Redis"""
def register_request():
    retries = 5
    while True:
        try:
            return cache.incr('pyservice2')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

"""Base route for LoadBalancer to execute hello function"""
@app.route('/')
def hello():
    register_request() # Registrers visits from service to Redis
    # Returns simple html
    return '<h1>Hello from Docker!</h1><br> The container contacted runs pyservice2'