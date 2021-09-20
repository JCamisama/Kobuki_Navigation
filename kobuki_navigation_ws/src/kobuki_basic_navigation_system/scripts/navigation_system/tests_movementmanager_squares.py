#!/usr/bin/env python
from MovementManager import MovementManager
import rospy




def do_test_perform_square_1():
    #test case 1: 0.36x0.36 m2 square, steps of 0.36 meters, counter clockwise

    linearDistance = 0.36
    commandList = [
                   'face_north',
                   'forward',
                   'face_west',
                   'forward',
                   'face_south',
                   'forward',
                   'face_east',
                   'forward',
                   'face_north'
                   ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_square_2():
    #test case 1: 0.36x0.36 m2 squares, steps of 0.36 meters, various paths

    linearDistance = 0.36
    commandList = [
                   'face_north',
                   'forward',
                   'face_west',
                   'forward',
                   'face_south',
                   'forward',
                   'face_east',
                   'forward',
                   'face_north',

                    'forward',
                    'face_east',
                    'forward',
                    'face_south',
                    'forward',
                    'face_west',
                    'forward',
                    'face_north',

                    'face_south',
                    'forward',
                    'face_west',
                    'forward',
                    'face_north',
                    'forward',
                    'face_east',
                    'forward',
                    'face_north',

                    'face_south',
                    'forward',
                    'face_east',
                    'forward',
                    'face_north',
                    'forward',
                    'face_west',
                    'forward',
                    'face_north',
                   ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_square_3():
    #test case 1: 1x1 m2 square, steps of 1 meter

    linearDistance = 1
    commandList = [
                   'face_north',
                   'forward',
                   'face_west',
                   'forward',
                   'face_south',
                   'forward',
                   'face_east',
                   'forward',
                   'face_north'
                   ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_square_4():
    #test case 1: 1x1 m2 square, steps of 0.2 meters

    linearDistance = 0.2
    commandList = [
                    'face_north',
                    'forward',
                    'forward',
                    'forward',
                    'forward',
                    'forward',
                    'face_west',
                    'forward',
                    'forward',
                    'forward',
                    'forward',
                    'forward',
                    'face_south',
                    'forward',
                    'forward',
                    'forward',
                    'forward',
                    'forward',
                    'face_east',
                    'forward',
                    'forward',
                    'forward',
                    'forward',
                    'forward',
                    'face_north'
                   ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



if __name__ == '__main__':

    rospy.sleep(1)
    rospy.init_node('movement_manager', anonymous=True)
    do_test_perform_square_1()
    # do_test_perform_square_2()
    # do_test_perform_square_3()
    # do_test_perform_square_4()