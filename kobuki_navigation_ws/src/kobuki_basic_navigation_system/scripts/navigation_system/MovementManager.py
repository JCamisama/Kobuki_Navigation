#!/usr/bin/env python

import rospy

from BasicCommandsMobileBase import BasicCommandsMobileBase
from RotationManager import RotationManager
from TranslationManager import TranslationManager
from MapPositionCalculator import MapPositionCalculator

from nav_msgs.msg import Odometry
from sensor_msgs.msg    import Imu
from geometry_msgs.msg  import Twist

from math               import degrees
from tf.transformations import euler_from_quaternion



class MovementManager:

    def __init__(self, pLinearDistance):

        self.initialize_ros_attributes()
        self.initialize_managers(pLinearDistance)
        self.initialize_positional_attributes()



    def initialize_ros_attributes(self):

        # self.rosNode = rospy.init_node('movement_manager', anonymous=True)
        self.velocityPublisher = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
        self.odomSubscriber    = rospy.Subscriber('odom', Odometry, self.odometry_info_callback)
        self.imuSubscriber     = rospy.Subscriber('/mobile_base/sensors/imu_data', Imu, self.orientation_callback)



    def initialize_managers(self, pLinearDistance):
        self.movementCommander = BasicCommandsMobileBase()
        self.rotationMan       = RotationManager(self.velocityPublisher, self.movementCommander)
        self.translationMan    = TranslationManager(pLinearDistance, self.velocityPublisher, self.movementCommander)



    def initialize_positional_attributes(self):

        self.infoTranslationX       = 0.0
        self.infoTranslationY       = 0.0
        self.currentOrientation     = 0.0
        self.orientationReference   = 0.0
        self.currentOrientationName = 'North'




    def odometry_info_callback(self, pOdomData):

        self.infoTranslationX  = pOdomData.pose.pose.position.x
        self.infoTranslationY  = pOdomData.pose.pose.position.y

        self.translationMan.update_translation_info(self.infoTranslationX, self.infoTranslationY)



    def orientation_callback(self, pImuData):

        quat = pImuData.orientation
        q    = [quat.x, quat.y, quat.z, quat.w]

        _, _, yaw = euler_from_quaternion(q)
        self.currentOrientation = degrees(yaw)

        # Making sure infoOrientationGlobal goes from 0 to 360 degrees
        if(self.currentOrientation < 0):
            self.currentOrientation += 360

        self.rotationMan.update_orientation_info(self.currentOrientation)
        self.update_orientation_reference()



    def perform_movement(self, pCommandList):

        for command in pCommandList:
            if(command == 'forward'):
                self.rotationMan.perform_adjustment(self.orientationReference)
                translationAxis = self.get_direction_axis()
                self.translationMan.perform_translation(translationAxis)
            else:
                self.rotationMan.perform_rotation(command)

            print(command + ' performed! \n')

        return self.currentOrientationName



    def get_direction_axis(self):

        if (self.orientationReference == 90.00 or self.orientationReference == 270.00):
           directionAxis = 'y'
        else:
           directionAxis = 'x'

        return directionAxis



    def update_orientation_reference(self):

        if(self.currentOrientation < 95.00 and self.currentOrientation > 85.00):
            self.orientationReference   = 90.0
            self.currentOrientationName = 'West'

        elif(self.currentOrientation < 185.00 and self.currentOrientation > 175.00):
            self.orientationReference   = 180.0
            self.currentOrientationName = 'South'

        elif (self.currentOrientation < 275.00 and self.currentOrientation > 265.00):
            self.orientationReference   = 270.0
            self.currentOrientationName = 'East'

        else:
            self.orientationReference   = 0.0
            self.currentOrientationName = 'North'



    def adjust_position(self, pOriginPosition, pTargetPosition, pBoxSideSize):
        # Requires:
        #    - pOriginPosition: 2-dimensional tuple containing integers ---> (int, int)
        #    - pTargetPosition: 2-dimensional tuple containing integers ---> (int, int)
        #    - pBoxSideSize: Size of the side of a square box, in meters
        #    - Both positions must be traversable
        # Ensures:
        #    - Kobuki will have adjusted itself to the exact position designated in the map

        positionCalculator = MapPositionCalculator()
        targetDistance     = positionCalculator.getPositionInMap(pBoxSideSize, pOriginPosition, pTargetPosition)
        # Row adjustment
        self.rotationMan.perform_rotation('face_north')
        translationAxis = self.get_direction_axis()
        self.translationMan.perform_adjustment(translationAxis, targetDistance[0])
        # Column adjustment
        self.rotationMan.perform_rotation('face_west')
        translationAxis = self.get_direction_axis()
        self.translationMan.perform_adjustment(translationAxis, targetDistance[1])






