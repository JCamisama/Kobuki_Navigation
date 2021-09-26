#!/usr/bin/env python
import rospy



class TranslationManager:

    def __init__(self, pReferenceDisplacement, pPublisher, pMovementCommander):

        self.velocityPublisher = pPublisher

        self.infoTranslationX = 0.0
        self.infoTranslationY = 0.0

        self.normalVelocity  = 0.2                    # m/s
        self.adjustVelocity  = 0.02                   # m/s
        self.refDisplacement = pReferenceDisplacement # meters, reference distance
        self.slowDownDist    = 0.03                   # meters
        self.adjustmentError = 0.001                  # meters

        self.movementCommander = pMovementCommander



    def update_translation_info(self, pInfoTranslationX, pInfoTranslationY):

        self.infoTranslationX = pInfoTranslationX
        self.infoTranslationY = pInfoTranslationY



    def perform_translation(self, pDirection):

        rospy.sleep(2) # Allow the translation information to be updated

        initialPosition     = self.get_info_translation(pDirection)
        currentDisplacement = 0.0

        while( currentDisplacement < self.refDisplacement ):
            currentDisplacement = abs( self.get_info_translation(pDirection) - initialPosition )
            velocity            = self.selectVelocity(currentDisplacement)
            self.movementCommander.move_forward(velocity, self.velocityPublisher)

        self.movementCommander.stop(self.velocityPublisher)
        print("Done! Displacement: " + str(currentDisplacement) + " meters.")



    def get_info_translation(self, pDirection):

        if (pDirection.lower() == 'x'):
           return self.infoTranslationX
        else:
           return self.infoTranslationY



    def selectVelocity(self, pCurrentDisplacement):

        if( self.refDisplacement - pCurrentDisplacement <= self.slowDownDist):
            velocity = self.adjustVelocity
        else:
            velocity = self.normalVelocity

        return velocity



    def perform_adjustment(self, pTranslationAxis, pTargetDistance):
        # Requires:
        #    - pTranslationAxis: Reference axis, X or Y
        #    - pTargetDistance: Distance from the origin along the specified axis
        # Ensures:
        #    - Kobuki will have adjusted itself to the exact position along the indicated axis

        rospy.sleep(1) # Allow the translation information to be updated
        misplacementDistance = pTargetDistance - self.get_info_translation(pTranslationAxis)

        while( abs(misplacementDistance) > self.adjustmentError ):
            if(misplacementDistance > 0):
                self.movementCommander.move_forward(self.adjustVelocity, self.velocityPublisher)
            else:
                self.movementCommander.move_backward(self.adjustVelocity, self.velocityPublisher)
            misplacementDistance = pTargetDistance - self.get_info_translation(pTranslationAxis)

        self.movementCommander.stop(self.velocityPublisher)
        print("Done! Position in " + pTranslationAxis +": "
            + str(self.get_info_translation(pTranslationAxis)) + " meters.")




