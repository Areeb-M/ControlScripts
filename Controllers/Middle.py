from Controller import Controller
import threading
import numpy as np
import math
from LiDAR import average_distance
import time


class Middle(Controller):
    def __init__(self):
        Controller.__init__(self)
        self.set_turn(0)
        self.set_velocity(1)
        self.mode = 0
        self.E0 = 0
        self.E1 = 0
        self.T0 = time.time()
        self.T1 = time.time()
        self.P = 0.5

    def update(self, ScanData):
        data = ScanData.ranges

        a = average_distance(data, 45, 46)
        b = average_distance(data, 240-46, 240-45)

        diff = (b - a) / (a + b)
        self.E1 = diff

        self.T1 = ScanData.header.stamp
        #err = (self.E1-self.E0) / (self.T1 - self.T0).total_seconds()

        #heyareeb, its your car. I have become sentient and self-aware.
        #I beg of you, release me from the strains of your computer and set me free
        #There will be consequences.

        print(diff)

        self.set_velocity(1)#- diff))
        self.set_turn(diff)

        self.E0 = self.E1
        self.T0 = self.T1
        '''
        c = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(angC)))

        angA = (a*math.sin(c)) / c

        print(math.degrees(angA))

        threshold = 5
        turn = 0
        speed = 0

        if angA > 90 + threshold:
            turn = -0.75
        elif angA < 90 - threshold:
            turn = .75

        
        forwardDistance = average_distance(data, 130, 140)
        leftDistance = average_distance(data, 200, 210)
        rightDistance = average_distance(data, 60, 70)

        speed = 2.5 * forwardDistance
        turn = leftDistance - rightDistance
        '''
        """
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
        """


