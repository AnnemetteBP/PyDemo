# The "Controller" and server for the monitorering service
import time

import redis
from flask import Flask

app = Flask(__name__) # Starts server/controller
cache = redis.Redis(host='redis', port=6379, decode_responses=True) # Redis connection to save and read requests from Redis

"""Reads and count requests from services to Redis"""
def monitor_service_1():
    retries = 5
    while True:
        try:
            return cache.get('pyservice1')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

"""Reads and count requests from services to Redis"""
def monitor_service_2():
    retries = 5
    while True:
        try:
            return cache.get('pyservice2')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

"""Reads number of visits to LoadBalancer from Redis"""
def monitor_loadbalancer():
    retries = 5
    while True:
        try:
            return cache.get('loadbalancer')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

"""Base route for the LoadBalancer to execute the hello function"""
@app.route('/')
def hello():
    loadbalancer = monitor_loadbalancer() #Gets requests count to LoadBalanceren from Redis
    service1 = monitor_service_1() #Gets service requests count from Redis
    service2 = monitor_service_2() #Gets service requests count from Redis
    #Returns html
    return '<h1>MONITOR PANEL</h1><br>Loadbalancer requests: ' + str(loadbalancer) + '<br>Service 1 requests: ' + str(service1) + '<br>Service 2 requests: ' + str(service2)