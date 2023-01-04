# The LoadBalancer "Controller" and server only responsible for 1 route "/" 
# Utilizes a LoadBalancer class for selecting registered services.
import urllib.request
import redis
from flask import Flask
from LoadBalancer import *

app = Flask(__name__) #Start server/controller
strategy = LoadBalancerStrategy() #Create new load balancer strategy
loadbalancer = LoadBalancer() #Create new LoadBalancer
loadbalancer.set_active_strategy(strategy) #Set LoadBalancer strategy
loadbalancer.add_service("http://192.168.96.4:5000") #Add pyservice1
loadbalancer.add_service("http://192.168.96.6:5000") #Add pyservice2
cache = redis.Redis(host='redis', port=6379) #Redis connection for registering LoadBalancer requests

"""Registrere at der er lavet 1 request til LoadBalanceren og gemmer dette i Redis"""
def register_request():
    retries = 5
    while True:
        try:
            return cache.incr('loadbalancer')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

"""Base route for LoadBalanceren kører funktionen hello"""
@app.route('/')
def hello():
    register_request() # Registrers incoming requests from a client
    service = loadbalancer.next_service() # LoadBalancer switching between pyservice1 and pyservice2 in a RR fashion
    contents = urllib.request.urlopen(service).read() # Selected service gets and saves requests
    return contents # Returns stored message to client
