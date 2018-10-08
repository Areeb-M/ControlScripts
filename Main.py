#!/usr/bin/env python

import time
import sys
import threading
import timeit
from Interrupts import *
from MotorController import *


class AutonomousControl(threading.Thread):
    def __init__(self):
        pass

    def run(self):
        sys.settrace(do_nothing_trace_function)
        try:
            while True:
                pass
        except RacecarException:
            pass
