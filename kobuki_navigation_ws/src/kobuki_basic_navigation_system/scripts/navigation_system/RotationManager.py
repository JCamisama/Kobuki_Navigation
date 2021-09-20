#!/usr/bin/env python

import rospy

class RotationManager:

    def __init__(self, pPublisher, pMovementCommander):

        self.infoOrientationGlobal = 0.0
        self.orientations = {'north': 0.0,
                             'east' : 270.0,
                             'south': 180.0,
                             'west' : 90.0,
                             }
        self.normalSpinVelocity     = 0.5  #rad/s
        self.adjustmentSpinVelocity = 0.25 #rad/s
        self.normalError            = 1    #degrees
        self.adjustmentError        = 0.5  #degrees

        self.velocityPublisher = pPublisher
        self.movementCommander = pMovementCommander



    def update_orientation_info(self, pCurrentOrientation):

        self.infoOrientationGlobal = pCurrentOrientation



    def perform_rotation(self, pRotationCommand):

        rospy.sleep(1) # Allow the orientation to be updated

        targetOrientation = pRotationCommand.split('_')[1] # 'face_orientation'.split('_') ---> [0]=face; [1]=orientation
        targetAngle       = self.orientations[targetOrientation]

        self.rotate_until_target_reached(targetAngle)
        print("Done! Current Angle: " + str(self.infoOrientationGlobal) + " degrees.")



    def rotate_until_target_reached(self, pTargetAngle):

        if not( self.is_adjusted_precise(pTargetAngle) ):
            rotationWhichWay  = self.select_rotation_side(pTargetAngle)

            while(not self.is_adjusted(pTargetAngle)):
                self.movementCommander.turn(rotationWhichWay, self.normalSpinVelocity, self.velocityPublisher)

            self.movementCommander.stop(self.velocityPublisher)
            rospy.sleep(0.5)

            self.perform_adjustment(pTargetAngle)



    def perform_adjustment(self, pTargetAngle):

        while (not self.is_adjusted_precise(pTargetAngle)):
            rotationWhichWay = self.select_rotation_side(pTargetAngle)
            self.movementCommander.turn(rotationWhichWay, self.adjustmentSpinVelocity, self.velocityPublisher)
            self.movementCommander.stop(self.velocityPublisher)

        self.movementCommander.stop(self.velocityPublisher)
        rospy.sleep(0.1)



    def select_rotation_side(self, pTargetAngle ):

        if( self.must_turn_left(pTargetAngle) ):
            direction = 'turn_left'
        else:
            direction = 'turn_right'

        return direction



    def must_turn_left(self, pTargetAngle):

        return ( pTargetAngle > self.infoOrientationGlobal and
                 not (pTargetAngle == 270.0 and self.infoOrientationGlobal < 10)  or
                (pTargetAngle == 0.0 and self.infoOrientationGlobal >= 260)  or
                (pTargetAngle == 90.0 and self.infoOrientationGlobal >= 350) )



    def is_adjusted_precise(self, pTargetAngle):

        return self.is_in_range(pTargetAngle, self.adjustmentError)



    def is_adjusted(self, pTargetAngle):

        return self.is_in_range(pTargetAngle, self.normalError)



    def is_in_range(self, pTargetAngle, pError):

        currentAngle = self.infoOrientationGlobal

        if(pTargetAngle == 0.0 and currentAngle > 180):
            currentAngle -= 360

        isBelowTopMargin = currentAngle < pTargetAngle + pError
        isAboveLowMargin = currentAngle > pTargetAngle - pError

        return isBelowTopMargin and isAboveLowMargin




