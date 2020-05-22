import sys
sys.path.append('Model\StatisticsModel')

import unittest
import Model.StatisticsModel.LinearRegression

class TestLinearRegression(unittest.TestCase):
    def test_createLinearRegressionModel(self):
        linearModel = LinearRegression()