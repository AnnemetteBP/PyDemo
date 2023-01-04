from LoadBalancerStrategy import *

class LoadBalancerInterface:
    """Loadbalancer for service1"""
    def get_all_services(self) -> list:
        """Returns a list of services"""
        pass
    
    def add_service(self, url: str) -> None:
        """Add a service to the loadbalancer"""
        pass
    
    def remove_service(self, url: str) -> None:
        """Removes a service to the loadbalancer"""
        pass

    def next_service(self) -> str:
        """Returns the url of the next service"""
        pass
    
    def get_loadbalancer_strategy(self) -> LoadBalancerStrategyInterface:
        """Returns the loadbalancing strategy"""
        pass
    
    def set_active_strategy(self, strategy: LoadBalancerStrategyInterface) -> None:
        """Sets the active loadbalancing strategy"""