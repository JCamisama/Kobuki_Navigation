#!/usr/bin/env python
from MovementManager import MovementManager
import rospy



def do_test_perform_rotation_1():
    #test case 1: 0 - 90 - 180 - 270 - 0 ---> Always rotate to the left

    linearDistance = 0.36
    commandList = [
                   'face_north',
                   'face_west',
                   'face_south',
                   'face_east',
                   'face_north'
                   ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_rotation_2():
    #test case 2: 0- 270 - 180 - 90 - 0 ---> Always rotate to the right

    linearDistance = 0.36
    commandList = [
        'face_north',
        'face_east',
        'face_south',
        'face_west',
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_rotation_3():
    #test case 3: 0 - 180 - 0 - 270 - 90 - 270 -0

    linearDistance = 0.36
    commandList = [
        'face_north',
        'face_south',
        'face_north',
        'face_east',
        'face_west',
        'face_east',
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_rotation_4():
    #test case 4: From North to every  orientation

    linearDistance = 0.36
    commandList = [
        'face_north',
        'face_north', # 4.1: North to North: stand still
        'face_north',
        'face_south', # 4.2: North to South: turn left
        'face_north',
        'face_east',  # 4.3: North to East: turn right
        'face_north',
        'face_west',  # 4.4: North to West: turn left
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_rotation_5():
    #test case 5: From East to every  orientation

    linearDistance = 0.36
    commandList = [
        'face_east',
        'face_north',  # 5.1: East to North: turn  left
        'face_east',
        'face_south',  # 5.2: East to South: turn right
        'face_east',
        'face_east',   # 5.3: East to East: stand still
        'face_east',
        'face_west',   # 5.4: East to West: turn right
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_rotation_6():
    #test case 6: From South to every  orientation

    linearDistance = 0.36
    commandList = [
        'face_south',
        'face_north',  # 6.1: South to North: turn  right
        'face_south',
        'face_south',  # 6.2: South to South: stand still
        'face_south',
        'face_east',   # 6.3: South to East: turn left
        'face_south',
        'face_west',   # 6.4: South to West: turn right
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



def do_test_perform_rotation_7():
    #test case 7: From West to every  orientation

    linearDistance = 0.36
    commandList = [
        'face_west',
        'face_north',  # 7.1: West to North: turn  right
        'face_west',
        'face_south',  # 7.2: West to South: turn left
        'face_west',
        'face_east',   # 7.3: West to East: turn left
        'face_west',
        'face_west',   # 7.4: West to West: stand still
        'face_north'
    ]

    movementManager = MovementManager(linearDistance)
    movementManager.perform_movement(commandList)



if __name__ == '__main__':

    rospy.sleep(1)
    rospy.init_node('movement_manager', anonymous=True)
    do_test_perform_rotation_1()
    # do_test_perform_rotation_2()
    # do_test_perform_rotation_3()
    # do_test_perform_rotation_4()
    # do_test_perform_rotation_5()
    # do_test_perform_rotation_6()
    # do_test_perform_rotation_7()
