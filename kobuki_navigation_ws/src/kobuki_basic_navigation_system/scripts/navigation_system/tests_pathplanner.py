from PathPlanner import PathPlanner
from Box import Box


def test_get_movement_sequence_1():
    #Test case 1: The received list of boxes is empty  --> Return empty list
    listOfOrderedBoxes = []

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'North')

    assert (not movementeSequence)       #assert the resulting array is empty



def test_get_movement_sequence_2():
    #Test case 2: The received list of boxes contains one box --> Return empty list
    listOfOrderedBoxes = [Box(0, 0, True)]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'North')

    assert (not movementeSequence)       #assert the resulting array is empty



def test_get_movement_sequence_3():
    #Test case 3.1: The received list contains two boxes, in the same row
    listOfOrderedBoxes = [Box(0, 0, True),
                          Box(0, 1, True)]
    pathPlanner        = PathPlanner()
    #   3.1.1: Facing North
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'North')
    assert  (len(movementeSequence) == 2)
    assert  (movementeSequence[0]   == 'face_east')
    assert  (movementeSequence[1]   == 'forward')
    #   3.1.2: Facing East
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'East')
    assert  (len(movementeSequence) == 1)
    assert  (movementeSequence[0]   == 'forward')
    #   3.1.3: Facing South
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'South')
    assert  (len(movementeSequence) == 2)
    assert  (movementeSequence[0]   == 'face_east')
    assert  (movementeSequence[1]   == 'forward')
    #   3.1.4: Facing West
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'West')
    assert  (len(movementeSequence) == 2)
    assert  (movementeSequence[0]   == 'face_east')
    assert  (movementeSequence[1]   == 'forward')


    #Test case 3.2: The received list contains two boxes, in the same column
    listOfOrderedBoxes = [Box(1, 0, True),
                          Box(0, 0, True)]
    pathPlanner        = PathPlanner()
    #   3.2.1: Facing North
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'North')
    assert  (len(movementeSequence) == 1)
    assert  (movementeSequence[0]   == 'forward')
    #   3.2.2: Facing East
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'East')
    assert  (len(movementeSequence) == 2)
    assert  (movementeSequence[0]   == 'face_north')
    assert  (movementeSequence[1]   == 'forward')
    #   3.2.3: Facing South
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'South')
    assert  (len(movementeSequence) == 2)
    assert  (movementeSequence[0]   == 'face_north')
    assert  (movementeSequence[1]   == 'forward')
    #   3.2.4: Facing West
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, 'West')
    assert  (len(movementeSequence) == 2)
    assert  (movementeSequence[0]   == 'face_north')
    assert  (movementeSequence[1]   == 'forward')



def test_get_movement_sequence_4():

    #Predefined circuit 1
    listOfOrderedBoxes     = [ Box(7, 0, True),
                               Box(6, 0, True),
                               Box(6, 1, True),
                             ]
    initialOrientation     = 'North'
    expectedResultSequence = [ 'forward', 'face_east', 'forward' ]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, initialOrientation)

    isCorrectPath = True
    i = 0

    while(isCorrectPath and i < len(movementeSequence) ):
        isCorrectPath = (movementeSequence[i] == expectedResultSequence[i])
        i += 1

    assert isCorrectPath



def test_get_movement_sequence_5():

    #Predefined circuit 2
    listOfOrderedBoxes     = [ Box(7, 7, True),
                               Box(6, 7, True),
                               Box(6, 6, True),
                             ]
    initialOrientation     = 'North'
    expectedResultSequence = [ 'forward', 'face_west', 'forward' ]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, initialOrientation)

    isCorrectPath = True
    i = 0

    while (isCorrectPath and i < len(movementeSequence)):
        isCorrectPath = (movementeSequence[i] == expectedResultSequence[i])
        i += 1

    assert isCorrectPath



def test_get_movement_sequence_6():

    #Predefined circuit 3
    listOfOrderedBoxes     = [ Box(0, 0, True),
                               Box(1, 0, True),
                               Box(1, 1, True),
                             ]
    initialOrientation     = 'South'
    expectedResultSequence = [ 'forward', 'face_east', 'forward' ]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, initialOrientation)

    isCorrectPath = True
    i = 0

    while (isCorrectPath and i < len(movementeSequence)):
        isCorrectPath = (movementeSequence[i] == expectedResultSequence[i])
        i += 1

    assert isCorrectPath



def test_get_movement_sequence_7():

    #Predefined circuit 4
    listOfOrderedBoxes     = [ Box(0, 7, True),
                               Box(1, 7, True),
                               Box(1, 6, True),
                             ]
    initialOrientation     = 'South'
    expectedResultSequence = [ 'forward', 'face_west', 'forward' ]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, initialOrientation)

    isCorrectPath = True
    i = 0

    while (isCorrectPath and i < len(movementeSequence)):
        isCorrectPath = (movementeSequence[i] == expectedResultSequence[i])
        i += 1

    assert isCorrectPath



def test_get_movement_sequence_8():

    #Predefined circuit 5
    listOfOrderedBoxes     = [ Box(5, 5, True),
                               Box(5, 6, True),
                               Box(6, 6, True),
                             ]
    initialOrientation     = 'East'
    expectedResultSequence = [ 'forward', 'face_south', 'forward' ]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, initialOrientation)

    isCorrectPath = True
    i = 0

    while (isCorrectPath and i < len(movementeSequence)):
        isCorrectPath = (movementeSequence[i] == expectedResultSequence[i])
        i += 1

    assert isCorrectPath



def test_get_movement_sequence_9():

    #Predefined circuit 6
    listOfOrderedBoxes     = [ Box(5, 5, True),
                               Box(5, 6, True),
                               Box(4, 6, True),
                             ]
    initialOrientation     = 'East'
    expectedResultSequence = [ 'forward', 'face_north', 'forward' ]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, initialOrientation)

    isCorrectPath = True
    i = 0

    while (isCorrectPath and i < len(movementeSequence)):
        isCorrectPath = (movementeSequence[i] == expectedResultSequence[i])
        i += 1

    assert isCorrectPath



def test_get_movement_sequence_10():

    #Predefined circuit 7
    listOfOrderedBoxes     = [ Box(5, 5, True),
                               Box(5, 4, True),
                               Box(6, 4, True),
                             ]
    initialOrientation     = 'West'
    expectedResultSequence = [ 'forward', 'face_south', 'forward' ]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, initialOrientation)

    isCorrectPath = True
    i = 0

    while (isCorrectPath and i < len(movementeSequence)):
        isCorrectPath = (movementeSequence[i] == expectedResultSequence[i])
        i += 1

    assert isCorrectPath



def test_get_movement_sequence_11():

    #Predefined circuit 7
    listOfOrderedBoxes     = [ Box(5, 5, True),
                               Box(5, 4, True),
                               Box(4, 4, True),
                             ]
    initialOrientation     = 'West'
    expectedResultSequence = [ 'forward', 'face_north', 'forward' ]

    pathPlanner       = PathPlanner()
    movementeSequence = pathPlanner.get_movement_sequence(listOfOrderedBoxes, initialOrientation)

    isCorrectPath = True
    i = 0

    while (isCorrectPath and i < len(movementeSequence)):
        isCorrectPath = (movementeSequence[i] == expectedResultSequence[i])
        i += 1

    assert isCorrectPath








def test_get_move_1():
    #case 1: vertical displacement upward
    currentBox  = Box(2, 3)
    nextBox     = Box(1, 3)
    pathPlanner = PathPlanner()

    #case 1.1: initially facing North ----> forward
    orientation = 'North'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'forward'

    #case 1.2: initially facing South ----> forward
    orientation = 'South'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_north'

    #case 1.3: initially facing East ----> forward
    orientation = 'East'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_north'

    #case 1.4: initially facing West ----> forward
    orientation = 'West'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_north'



def test_get_move_2():
    #case 2: vertical displacement downward
    currentBox  = Box(2, 3)
    nextBox     = Box(3, 3)
    pathPlanner = PathPlanner()

    #case 2.1: initially facing North ----> face_south
    orientation = 'North'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_south'

    #case 2.2: initially facing South ----> forward
    orientation = 'South'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'forward'

    #case 2.3: initially facing East ----> face_south
    orientation = 'East'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_south'

    #case 2.4: initially facing West ----> face_south
    orientation = 'West'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_south'



def test_get_move_3():
    #case 3: horizontal displacement left
    currentBox  = Box(2, 3)
    nextBox     = Box(2, 2)
    pathPlanner = PathPlanner()

    #case 3.1: initially facing North ----> face_west
    orientation = 'North'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_west'

    #case 3.2: initially facing South ----> face_west
    orientation = 'South'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_west'

    #case 3.3: initially facing East ----> face_west
    orientation = 'East'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_west'

    #case 3.4: initially facing West ----> forward
    orientation = 'West'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'forward'



def test_get_move_4():
    #case 4: horizontal displacement right
    currentBox  = Box(2, 3)
    nextBox     = Box(2, 4)
    pathPlanner = PathPlanner()

    #case 3.1: initially facing North ----> face_east
    orientation = 'North'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_east'

    #case 3.2: initially facing South ----> face_east
    orientation = 'South'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_east'

    #case 3.3: initially facing East ----> forward
    orientation = 'East'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'forward'

    #case 3.4: initially facing West ----> face_east
    orientation = 'West'
    nextMove    = pathPlanner.get_next_move(currentBox, nextBox, orientation)
    assert  nextMove == 'face_east'



def test_define_next_move_1():
    #case 1: Required Orientation = 'north'

    pathPlanner = PathPlanner()

    #case 1.1: Current Orientation = 'North' ---> 'forward'
    nextMove = pathPlanner.define_next_move('north', 'North')
    assert ( nextMove == 'forward' )

    # case 1.2: Current Orientation = 'South' ---> 'face_north'
    nextMove = pathPlanner.define_next_move('north', 'South')
    assert (nextMove == 'face_north')

    # case 1.3: Current Orientation = 'East' ---> 'face_north'
    nextMove = pathPlanner.define_next_move('north', 'East')
    assert (nextMove == 'face_north')

    # case 1.4: Current Orientation = 'West' ---> 'face_north'
    nextMove = pathPlanner.define_next_move('north', 'West')
    assert (nextMove == 'face_north')



def test_define_next_move_2():
    #case 2: Required Orientation = 'south'

    pathPlanner = PathPlanner()

    #case 2.1: Current Orientation = 'North' ---> 'face_south'
    nextMove = pathPlanner.define_next_move('south', 'North')
    assert ( nextMove == 'face_south' )

    # case 2.2: Current Orientation = 'South' ---> 'forward'
    nextMove = pathPlanner.define_next_move('south', 'South')
    assert (nextMove == 'forward')

    # case 2.3: Current Orientation = 'East' ---> 'face_south'
    nextMove = pathPlanner.define_next_move('south', 'East')
    assert (nextMove == 'face_south')

    # case 2.4: Current Orientation = 'West' ---> 'face_south'
    nextMove = pathPlanner.define_next_move('south', 'West')
    assert (nextMove == 'face_south')



def test_define_next_move_3():
    #case 3: Required Orientation = 'east'

    pathPlanner = PathPlanner()

    #case 3.1: Current Orientation = 'North' ---> 'face_east'
    nextMove = pathPlanner.define_next_move('east', 'North')
    assert ( nextMove == 'face_east' )

    # case 3.2: Current Orientation = 'South' ---> 'face_east'
    nextMove = pathPlanner.define_next_move('east', 'South')
    assert (nextMove == 'face_east')

    # case 3.3: Current Orientation = 'East' ---> 'forward'
    nextMove = pathPlanner.define_next_move('east', 'East')
    assert (nextMove == 'forward')

    # case 3.4: Current Orientation = 'West' ---> 'face_east'
    nextMove = pathPlanner.define_next_move('east', 'West')
    assert (nextMove == 'face_east')



def test_define_next_move_4():
    #case 4: Required Orientation = 'west'

    pathPlanner = PathPlanner()

    #case 4.1: Current Orientation = 'North' ---> 'face_west'
    nextMove = pathPlanner.define_next_move('west', 'North')
    assert ( nextMove == 'face_west' )

    # case 4.2: Current Orientation = 'South' ---> 'face_west'
    nextMove = pathPlanner.define_next_move('west', 'South')
    assert (nextMove == 'face_west')

    # case 4.3: Current Orientation = 'East' ---> 'face_west'
    nextMove = pathPlanner.define_next_move('west', 'East')
    assert (nextMove == 'face_west')

    # case 4.4: Current Orientation = 'West' ---> 'forward'
    nextMove = pathPlanner.define_next_move('west', 'West')
    assert (nextMove == 'forward')