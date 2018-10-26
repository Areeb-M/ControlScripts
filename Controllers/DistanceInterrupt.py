from Controller import Controller
import numpy as np


class DistanceInterrupt(Controller):
    def __init__(self):
        Controller.__init__(self)

    def update(self, ScanData):
        data = ScanData.ranges
        left = 120
        right = 150
        threshold = 0.5
        avg_distance = average_distance(data, left, right)

        if avg_distance < threshold and self.get_velocity() > 0:
            self.HALT()


def average_distance(data, a=0, b=270):
    PPD = 4 # points per degree
    data = data[a*PPD:b*PPD]
    arr = np.array(data)
    return arr.mean()
