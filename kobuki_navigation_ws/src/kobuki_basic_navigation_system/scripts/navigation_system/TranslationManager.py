#!/usr/bin/env python
import rospy



class TranslationManager:

    def __init__(self, pReferenceDisplacement, pPublisher, pMovementCommander):

        self.velocityPublisher = pPublisher

        self.infoTranslationX = 0.0
        self.infoTranslationY = 0.0

        self.normalVelocity  = 0.2  # m/s
        self.adjustVelocity  = 0.02 # m/s
        self.refDisplacement = pReferenceDisplacement # meters, reference distance
        self.slowDownDist    = 0.03 # meters

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


