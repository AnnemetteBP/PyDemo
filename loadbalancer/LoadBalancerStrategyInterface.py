class LoadBalancerStrategyInterface:
    def next_service(self, services: list) -> str:
        """Returns the url of the next service"""
        pass