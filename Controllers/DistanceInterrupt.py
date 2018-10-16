from Controller import Controller
import numpy as np


class DistanceInterrupt(Controller):
    def __init__(self):
        pass

    def update(self, data):
        pass

    def HALT(self):
        pass

def average_distance(data, a=0, b=270):
    PPD = 4 # points per degree
    data = data[a*PPD:b*PPD]
    arr = np.array(data)
    return arr.mean()
