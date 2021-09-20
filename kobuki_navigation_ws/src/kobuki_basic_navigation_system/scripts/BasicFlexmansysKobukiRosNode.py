import rospy
from navigation_system.Laboratory import Laboratory
from navigation_system.Box import Box
from navigation_system.PathPlanner import PathPlanner
from navigation_system.MovementManager import MovementManager


def handle_kobuki(pSourcePos, pDestinationPor, pMapDirectory, pLinearDisplacement):
    rospy.init_node('kobuki_handler', anonymous=True)
    rospy.loginfo('\nKobuki handler up and running!\n')
    reset_orientation_to_north()

    ################# Getting an array of boxes #################
    matrixTxtPath = pMapDirectory
    laboratoryMap = Laboratory(matrixTxtPath)

    sourceBox    = Box(pSourcePos[0], pSourcePos[1], True)
    destBox      = Box(pDestinationPor[0], pDestinationPor[1], True)

    shortestPath = laboratoryMap.get_shortest_path_BFS(sourceBox, destBox)

    for box in shortestPath:
        box.print_coordinates()
        print("")
    #############################################################

    ################# Getting an array of movement instructions #################
    initialOrientation = 'North'
    pathPlanner        = PathPlanner()
    movementSequence  = pathPlanner.get_movement_sequence(shortestPath, initialOrientation)
    print("\n")
    print(movementSequence)
    print("\n")
    #############################################################

    ################# Making the robot move #################
    movementManager = MovementManager(pLinearDisplacement)
    movementManager.perform_movement(movementSequence)
    #############################################################

def reset_orientation_to_north():
    #Quick fix to reset the orientation to north and make the tests work fine
    movementManager = MovementManager(0)
    movementManager.perform_movement(["face_north"])


def all_together_test(pMapDir):
    unitLinearDisplacemente = 1
    originPos = (5, 5)
    targetPos = (0, 0)
    handle_kobuki(originPos, targetPos, pMapDir, unitLinearDisplacemente)
    handle_kobuki(targetPos, originPos, pMapDir, unitLinearDisplacemente)




if __name__ == '__main__':
    try:
        # mapDir = "./maps/initial_tests/test_1_L_path.txt"
        mapDir = "./maps/initial_tests/test_2_Snake_path.txt"
        # mapDir = "./maps/initial_tests/test_3_Snake_vs_L_path.txt"
        all_together_test(mapDir)

    except rospy.ROSInternalException:
        rospy.loginfo('Something went wrong in FlexmansysKobukiRosNode!!!')

