from LoadBalancerStrategyInterface import *

class LoadBalancerStrategy(LoadBalancerStrategyInterface):

    current_service_index: int

    """Constructor"""
    def __init__(self):
        self.current_service_index = 0

    """Returns the url of the next service"""
    def next_service(self, services: list) -> str:           
        if (self.current_service_index < (len(services) - 1)):
            self.current_service_index += 1
        else:
            self.current_service_index = 0
        return services[self.current_service_index]