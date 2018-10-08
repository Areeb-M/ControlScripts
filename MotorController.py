#!/usr/bin/env python
import rospy
from ackermann_msgs.msg import AckermannDriveStamped

forward_velocity = 0.0
turn = 0.0

pub = rospy.Publisher('/vesc/ackermann_cmd_mux/input/teleop', AckermannDriveStamped, queue_size=1)
rospy.init_node('MotorController')


def set_velocity(v):
    global forward_velocity
    forward_velocity = v
    update_car()


def set_turn(t):
    global turn
    turn = t
    update_car()


def update_car():
    global forward_velocity, turn, pub

    msg = AckermannDriveStamped();
    msg.header.stamp = rospy.Time.now();
    msg.header.frame_id = "base_link";

    msg.drive.speed = forward_velocity;
    msg.drive.acceleration = 1;
    msg.drive.jerk = 1;
    msg.drive.steering_angle = turn
    msg.drive.steering_angle_velocity = 1

    pub.publish(msg)


def get_velocity():
    global forward_velocity
    return forward_velocity


def get_turn():
    global turn
    return turn


# Emergency Functions


def HALT():
    global forward_velocity, turn
    forward_velocity = 0
    turn = 0
    update_car()