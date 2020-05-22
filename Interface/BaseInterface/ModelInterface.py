class ModelInterface:
    def __init__(self, parameters, config):
        """get parameters of model"""
        pass
    
    def model(self, batch):
        """defining a machine learning model"""
        pass

    def train(self, dataset):
        """training a machine learning model"""
        pass
    
    def test(self, dataset):
        """testing a machine learning model"""
        pass 

    def save(self, path):
        """saving a machine learning model"""
        pass
    def load(self, path):
        """loading a machine learning model"""
        pass

    def predict(self, dataitem):
        """predict a dataitem"""
        pass
