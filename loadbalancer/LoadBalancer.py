from LoadBalancerInterface import *

class LoadBalancer(LoadBalancerInterface):    
    """Loadbalancer for service1"""

    services: list
    strategy: LoadBalancerStrategyInterface

    """Constructor"""
    def __init__(self):
        self.services = list()
        self.strategy = LoadBalancerStrategy()

    """Returns a list of services"""
    def get_all_services(self) -> list:
        return self.services
    
    """Add a service to the loadbalancer"""
    def add_service(self, url: str) -> None:
        self.services.append(url)
    
    """Removes a service to the loadbalancer"""
    def remove_service(self, url: str) -> None:
        self.services.remove(url)

    """Returns the url of the next service"""
    def next_service(self) -> str:
        return self.get_loadbalancer_strategy().next_service(self.services)
    
    """Returns the loadbalancing strategy"""
    def get_loadbalancer_strategy(self) -> LoadBalancerStrategyInterface:
        return self.strategy
    
    """Sets the active loadbalancing strategy"""
    def set_active_strategy(self, strategy: LoadBalancerStrategyInterface) -> None:
        self.strategy = strategy