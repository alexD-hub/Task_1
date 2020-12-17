#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Int8

from triangle_info.msg import ThreeSides

def triangle(data):
    rospy.loginfo('a = %d, b = %d, c = %d', data.a,
    data.b, data.c)
    pub = rospy.Publisher('is_right_triangle', Bool, queue_size=10)
    msg = Bool()
    if (data.c ** 2 == data.a ** 2 + data.b ** 2) or \
       (data.a ** 2 == data.c ** 2 + data.b ** 2) or \
       (data.b ** 2 == data.c ** 2 + data.a ** 2):
       msg.data = True
    else:
       msg.data = False
    rospy.loginfo(msg.data)
    pub.publish(msg)


def listener():
     rospy.init_node('listener', anonymous=True)
     rospy.Subscriber('length', ThreeSides, triangle)
     rospy.spin()


if __name__ == '__main__':
     listener()
