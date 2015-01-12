# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 21:03:32 2015

@author: USER
"""

# First we will define some joint coordinates
from  robot.puma560 import *
# Next define the tool for plot
import matplotlib.pyplot as plt

# The path will move the robot from its zero angle pose to the upright (or 
# READY) pose.

# First create a time vector, completing the motion in 2 seconds with a
# sample interval of 56ms.
t = arange(0, 2, 0.056)    #generate a time vector
 
 # A polynomial trajectory between the 2 poses is computed using jtraj() in robot/trajectory
from robot.trajectory import jtraj
 
(q, qd, qdd) = jtraj(qz, qr, t)
 
# For this particular trajectory most of the motion is done by joints 2 and 3,
# and here I use matplotlib which has similar command like MATLAB
plt.subplot(2,1,1)
plt.plot(t, q[:,1])
plt.title('Theta')
plt.xlabel('Time (s)')
plt.ylabel('Joint 2 (rad)')
plt.subplot(2,1,2)
plt.plot(t, q[:,2])
plt.xlabel('Time (s)')
plt.ylabel('Joint 3 (rad)')
plt.draw()
#plt.show(block=False)

plt.figure()
plt.subplot(2,1,1)
plt.plot(t, qd[:,1])
plt.title('Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Joint 2 vel (rad/s)')
plt.subplot(2,1,2)
plt.plot(t, qd[:,2])
plt.xlabel('Time (s)')
plt.ylabel('Joint 3 vel (rad/s)')
plt.draw()
#plt.show(block=False)

plt.figure()
plt.subplot(2,1,1)
plt.plot(t, qdd[:,1])
plt.title('Acceleration')
plt.xlabel('Time (s)')
plt.ylabel('Joint 2 accel (rad/s^2)')
plt.subplot(2,1,2)
plt.plot(t, qdd[:,2])
plt.xlabel('Time (s)')
plt.ylabel('Joint 3 accel (rad/s^2)')
#plt.draw()
plt.show()