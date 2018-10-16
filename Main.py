#!/usr/bin/env python

import rospy
rospy.init_node('main_controller')

import time
import sys
#import threading
import timeit
import PrimaryInterface as PI
from Interrupts import *
from Controllers.Forward import Forward
from Controllers.DistanceInterrupt import DistanceInterrupt
from sensor_msgs.msg import *


#class AutonomousControl(threading.Thread):
class AutonomousControl:
    def __init__(self):
        safety_controller = DistanceInterrupt()
        controller = Forward()
        PI.subscribe_topic("/scan", LaserScan)
        PI.register_callback("/scan", controller.update)
        PI.register_callback("/scan", safety_controller.update)

    def run(self):
        sys.settrace(do_nothing_trace_function)
        try:
            while True:
                time.sleep(1)
        except RacecarException:
            sys.exit(0)


controller = AutonomousControl()
controller.run()