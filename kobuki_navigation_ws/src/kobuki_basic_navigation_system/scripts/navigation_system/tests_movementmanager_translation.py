#!/usr/bin/env python
from MovementManager import MovementManager
import rospy



def do_test_perform_translation_1():

    #test case 1: 0.36 meters in steps of 0.36 meters (Default Box size)

    linearDistance = 0.36
    commandList = [
        'face_north',
        'forward',
        'face_south',
        'forward',
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_translation_2():

    #test case 2: 1 meter in steps of 0.2 meters

    linearDistance = 0.2
    commandList = [
        'face_north',
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
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_translation_3():

    #test case 3: 1 meter in steps of 1 meter

    linearDistance = 1
    commandList = [
        'face_north',
        'forward',
        'face_south',
        'forward',
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_translation_4():

    #test case 4: 2 meters in steps of 1 meter

    linearDistance = 1
    commandList = [
        'face_north',
        'forward',
        'forward',
        'face_south',
        'forward',
        'forward',
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



if __name__ == '__main__':

    rospy.sleep(1)
    rospy.init_node('movement_manager', anonymous=True)
    do_test_perform_translation_1()
    # do_test_perform_translation_2()
    # do_test_perform_translation_3()
    # do_test_perform_translation_4()

