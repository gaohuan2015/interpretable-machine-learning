import numpy

class LinearRegression():
    def __init__(self, w, b, config):
        self.w = w
        self.b = b
        self.config = config

    def model(self, batch):
        y = self.w*batch + self.b
        return y

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
