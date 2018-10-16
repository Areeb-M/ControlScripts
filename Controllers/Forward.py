from Controller import Controller
import numpy as np


class Forward(Controller):
    def __init__(self):
        Controller.__init__(self)
        self.set_turn(0)
        self.set_velocity(1)

    def update(self, ScanData):
        self.set_velocity(1)
        self.set_turn(0)
