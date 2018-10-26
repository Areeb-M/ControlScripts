from Controller import Controller
import threading
import numpy as np
from LiDAR import average_distance


class Forward(Controller):
    def __init__(self):
        Controller.__init__(self)
        self.set_turn(0)
        self.set_velocity(1)
        self.mode = 0

    def update(self, ScanData):
        if self.mode == 0:
            self.set_velocity(1)
            self.set_turn(0)
        elif self.mode == 1:
            self.set_turn(.5)
            self.set_velocity(-1)

        if Controller.halt:
            self.UNHALT()
            self.mode = 1

            def switch_to_0():
                self.mode = 0
            threading.Timer(1, switch_to_0).start()



