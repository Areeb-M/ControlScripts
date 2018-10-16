from Controller import Controller
import numpy as np


class Forward(Controller):
    def __init__(self):
        Controller.__init__(self)
        self.set_turn(0)
        self.set_velocity(1)

    def update(self, ScanData):
        pass
        '''
        data = ScanData.ranges
        left = 120
        right = 150
        threshold = 0.5
        avg_distance = average_distance(data, left, right)

        if avg_distance < threshold:
            self.HALT()
        else:
            self.set_velocity(1)
            self.set_turn(0)
        '''

    def HALT(self):
        self.set_velocity(0)
        self.set_turn(0)


def average_distance(data, a=0, b=270):
    PPD = 4 # points per degree
    data = data[a*PPD:b*PPD]
    arr = np.array(data)
    return arr.mean()
