#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from navigation_system.Laboratory      import Laboratory
from navigation_system.Box             import Box
from navigation_system.PathPlanner     import PathPlanner
from navigation_system.MovementManager import MovementManager
from FlexmansysMsgHandler import FlexmansysMsgHandler
import cruiserconfig as config

class FlexmansysCruiser:
    # This class should implement the basic methods defined in the FlexmansysRosTransport interface

    def __init__(self):
        # Customizable features in config.py
        self.boxSize            = config.boxSize             # meters
        self.mapDirectory       = config.mapDir
        self.currentOrientation = config.initialOrientation
        # Cruiser default initialization
        self.initialize_ros_system()
        self.initialize_cruiser_position()
        self.initialize_cruiser_navigation_system()



    def initialize_ros_system(self):
        rospy.init_node('flexmansys_cruiser', anonymous=True)
        rospy.loginfo('\nFlexmansys  cruiser up and running!\n')
        rospy.Subscriber(config.topic, String, self.handle_instruction_callback)



    def initialize_cruiser_position(self):
        # Requitements:
        #   - The initial position should always be traversable.
        self.currentRow     = config.initialRow # int( input('\nInitial row position:\t') )
        self.currentCol     = config.initialCol # int( input('Initial column position:\t') )
        self.originPosition = (self.currentRow , self.currentCol)
        print('\n')



    def initialize_cruiser_navigation_system(self):
        self.labManager       = Laboratory(self.mapDirectory)
        self.pathPlanner      = PathPlanner()
        self.movementManager  = MovementManager(self.boxSize)
        # Get current orientation
        rospy.sleep(0.5)
        self.currentOrientation = self.movementManager.currentOrientationName




    def handle_instruction_callback(self, pInstruction):
        # Requires:
        #    - pInstruction: String  from std_msgs.msg, containing map positions.
        # Ensures:
        #    - Navigation to all the map-targets specified.

        msgHandler = FlexmansysMsgHandler()
        # Get an array of tuples indicating map positions: orders = [ (row1, col1), (row2, col2), ... ]
        orders     = msgHandler.prepare_transport_orders(pInstruction)
        if(orders):
            self.navigate_to_designated_coordinates(orders)
        else:
            print("\nNo valid set of orders has been specified, I'll stay put.\n")



    def navigate_to_designated_coordinates(self, pArrayOfCoordinates):
        # Requires:
        #    - pArrayOfCoordinates: Array of 2-dimensional tuples containing integers.
        # Ensures:
        #    - Navigation to all the map-targets specified, if they are valid.

        for target in pArrayOfCoordinates:
            self.navigate_to_target_position(target)
            rospy.sleep(1)

        print("\nNavigation plan completed! current position: ("
              + str(self.currentRow) + ", "
              + str(self.currentCol) +")\n")



    def navigate_to_target_position(self, pTarget):
        # Requires:
        #    - pTarget: 2-dimensional tuple containing integers
        # Ensures:
        #    - Kobuki will navigate to the specified target if the destination is valid.

        if( self.labManager.is_inside_matrix_boundaries( *pTarget ) ):
            movementSequence  = self.handle_path_to_target(pTarget)
            if(movementSequence):
                self.currentOrientation = self.movementManager.perform_movement(movementSequence)
                self.currentRow         = pTarget[0]
                self.currentCol         = pTarget[1]
                # print("Adjustin position at " + str(pTarget) + "...")
                # self.movementManager.adjust_position(self.originPosition, pTarget, self.boxSize)
                self.currentOrientation = self.movementManager.currentOrientationName
                print("Navigation to " + str(pTarget) + " completed!")
        else:
            print("The target is outside of the map boundaries, it will be ignored.")



    def handle_path_to_target(self, pTarget):
        # Requires:
        #    - pTarget: 2-dimensional tuple containing integers
        # Ensures:
        #    - Return sequence of movements required to reach the destination.

        movementSequence = []
        destBox          = Box(pTarget[0], pTarget[1], True)

        if(self.labManager.is_valid_box(destBox)):
            sourceBox        = Box(self.currentRow, self.currentCol, True)
            pathToTarget     = self.labManager.get_shortest_path_BFS(sourceBox, destBox)
            movementSequence = self.pathPlanner.get_movement_sequence(pathToTarget, self.currentOrientation)
        else:
            print("The target is not traversable, it will be ignored.")

        return movementSequence




if __name__ == '__main__':
    cruiser = FlexmansysCruiser()
    print("\nCruiser ready to get after it.\n")
    rospy.spin()