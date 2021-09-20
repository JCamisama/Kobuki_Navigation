
'''
The goal of this class is to create a set of sequential movement instructions associated to a given
list of coordinates, represented by objects of the class "Box", and an orientation (North, East, South, West).
'''



class PathPlanner:

    def __init__(self):
        self.possibleOrientations = {
            (-1, 0) : "north",
            (1, 0)  : "south",
            (0, -1) : "west",
            (0, 1)  : "east"
        }

    def get_movement_sequence(self, pListOfOrderedBoxes, pOrientation):
        #Requires: - pListOfOrderedBoxes not None
        #          - pOrientation in ['North', 'East', 'South', 'West']

        movementSequence = []
        if len(pListOfOrderedBoxes) > 1:
            self.process_movement_sequence(pListOfOrderedBoxes, pOrientation, movementSequence)

        return movementSequence



    def get_next_move(self, pCurrentBox, pNextBox, pOrientation):

        displacepentTuple   = (pNextBox.row - pCurrentBox.row, pNextBox.column - pCurrentBox.column)
        requiredOrientation = self.possibleOrientations[displacepentTuple]
        nextMove            = self.define_next_move(requiredOrientation, pOrientation)

        return nextMove



    def define_next_move(self, pRequiredOrientation, pCurrentOrientation):

        nextMove   = 'forward'
        currentOr  = pCurrentOrientation.lower()
        requiredOr = pRequiredOrientation.lower()

        if(requiredOr != currentOr):
            nextMove = 'face_' + requiredOr

        return nextMove



    def process_movement_sequence(self, pListOfOrderedBoxes, pOrientation, pMovementSequence):

        currenBox    = pListOfOrderedBoxes[0]
        nextBox      = pListOfOrderedBoxes[1]
        nextMove     = ''
        currentOr    = pOrientation
        listPosition = 1

        while( listPosition < len(pListOfOrderedBoxes) ):
            nextMove = self.get_next_move(currenBox, nextBox, currentOr)
            pMovementSequence.append(nextMove)
            if(nextMove == 'forward'):
                listPosition += 1
            else:
                currentOr = nextMove.split('_')[1]         # 'face_orientation'.split('_') ---> [0]=face; [1]=orientation

            if(listPosition < len(pListOfOrderedBoxes)):
                currenBox     = pListOfOrderedBoxes[listPosition - 1]
                nextBox       = pListOfOrderedBoxes[listPosition]



