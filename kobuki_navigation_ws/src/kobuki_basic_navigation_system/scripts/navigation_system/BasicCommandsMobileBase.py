#!/usr/bin/env python

from geometry_msgs.msg import Twist


class BasicCommandsMobileBase:

    def __init__(self):
        self.moveMessage = Twist()



    def reset_movement_parameters(self):

        self.moveMessage.linear.x  = 0.0
        self.moveMessage.linear.y  = 0.0
        self.moveMessage.linear.z  = 0.0
        self.moveMessage.angular.x = 0.0
        self.moveMessage.angular.y = 0.0
        self.moveMessage.angular.z = 0.0



    def x_axis_displacement(self, pVelocity):

        self.reset_movement_parameters()
        self.moveMessage.linear.x = pVelocity



    def rotate(self, pAngularVelocity):

        self.reset_movement_parameters()
        self.moveMessage.angular.z = pAngularVelocity



    def stop(self, pVelocityPublisher):

        self.reset_movement_parameters()
        pVelocityPublisher.publish(self.moveMessage)



    def move_forward(self, pVelocity, pVelocityPublisher):

        velocityForward = abs(pVelocity)
        self.x_axis_displacement(velocityForward)
        pVelocityPublisher.publish(self.moveMessage)



    def move_backward(self, pVelocity, pVelocityPublisher):

        velocityBackwards = - abs(pVelocity)
        self.x_axis_displacement(velocityBackwards)
        pVelocityPublisher.publish(self.moveMessage)



    def turn(self, pWhichWay, pAngularVelocity, pVelocityPublisher):

        if(pWhichWay == 'turn_left'):
            angdularVel = abs(pAngularVelocity)
        else:
            angdularVel = - abs(pAngularVelocity)

        self.rotate(angdularVel)
        pVelocityPublisher.publish(self.moveMessage)