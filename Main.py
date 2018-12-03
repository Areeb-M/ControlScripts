#!/usr/bin/env python

import rospy
rospy.init_node('main_controller')

import time
import sys
#import threading
import timeit
import PrimaryInterface as PI
from Interrupts import *
from Controllers.Middle import Middle
from Controllers.DistanceInterrupt import DistanceInterrupt
from sensor_msgs.msg import *
from MotorController import HALT

#class AutonomousControl(threading.Thread):
class AutonomousControl:
    def __init__(self):
        safety_controller = DistanceInterrupt()
        controller = Middle()
        PI.subscribe_topic("/filtered", LaserScan)
        PI.register_callback("/filtered", controller.update)
        PI.register_callback("/filtered", safety_controller.update)

    def run(self):
        sys.settrace(do_nothing_trace_function)
        try:
            while True:
                time.sleep(1)
        except RacecarException:
            sys.exit(0)


controller = AutonomousControl()
controller.run()
HALT()
