import sys
from collections import deque
from MatrixCreator import BoxMatrixCreator
from Box import Box



class Laboratory:



    def __init__(self, pPath):

        matrixCreator = BoxMatrixCreator()
        self.matrix   = matrixCreator.create_matrix_of_boxes_from_txt(pPath)

        self.rowMax = len(self.matrix)
        self.colMax = len(self.matrix[0])




    def is_inside_matrix_boundaries(self, pRow, pCol):
        # pRow: int, pCol: int

        validRowNumber = (pRow >= 0) and (pRow < self.rowMax)
        validColNumber = (pCol >= 0) and (pCol < self.colMax)

        return validRowNumber and validColNumber



    def is_valid_box(self, pBox):

        isValid = False

        if  pBox != None:

            boxInMatrix = self.matrix[pBox.row][pBox.column]
            isValid     = boxInMatrix.traversable

        return isValid



    def get_shortest_path_BFS(self, pSourceBox, pDestinationBox):

        shortestPath = []

        if self.is_valid_box(pSourceBox) and self.is_valid_box(pDestinationBox):
            startBox      = self.matrix[pSourceBox.row][pSourceBox.column]
            endBox        = self.matrix[pDestinationBox.row][pDestinationBox.column]
            shortestPath  = self.perform_bfs(startBox, endBox)

        return shortestPath



    def are_the_same_box(self, pBox, pTargetBox):

        return pBox.row == pTargetBox.row and pBox.column == pTargetBox.column



    def perform_bfs(self, pStartBox, pEndBox):

        shortestPath = []
        visited      = {pStartBox: None}                 #Key = current box ; Value = previous box
        candidates   = deque()
        dest_found   = False
        candidates.append(pStartBox)

        while candidates and not dest_found:

            currentCandidate = candidates.popleft()
            if currentCandidate.equals(pEndBox):
                dest_found = True
            else:
                visited = self.process_adjacent_boxes(currentCandidate, candidates, visited)

        if dest_found:
            shortestPath = self.construct_path(visited, pEndBox)

        return shortestPath



    def process_adjacent_boxes(self, pBox, pCandidates, pVisited):

        #Processing clockwise: up, right, down, left
        rowNeighbourNum = [-1, 0, 1, 0]
        colNeighbourNum = [0, 1, 0, -1]

        for i in range(len(rowNeighbourNum)):

            row         = pBox.row + rowNeighbourNum[i]
            column      = pBox.column + colNeighbourNum[i]

            if self.is_a_candidate(row, column, pVisited):
                boxInMatrix           = self.matrix[row][column]
                pVisited[boxInMatrix] = pBox
                pCandidates.append(boxInMatrix)

        return pVisited




    def construct_path(self, pVisitedDictionary, pEndBox):

        boxStack = deque()

        boxStack.append(pEndBox)
        currentBox  = pEndBox
        previousBox = pVisitedDictionary[currentBox]

        while previousBox:
            currentBox = previousBox
            boxStack.append(currentBox)
            previousBox = pVisitedDictionary[currentBox]

        pathList = self.create_list_from_stack_of_boxes(boxStack)

        return pathList




    def create_list_from_stack_of_boxes(self, pBoxStack):

        list = []
        while pBoxStack:
            list.append(pBoxStack.pop())

        return list



    def is_a_candidate(self, pRow, pColumn, pVisited):

        #Requires: pBox cannot be None

        isCandidate = False

        if self.is_inside_matrix_boundaries(pRow, pColumn):
            boxInMatrix              = self.matrix[pRow][pColumn]
            isTraversableBox         = boxInMatrix.traversable
            hasNotBeenVisited        = not boxInMatrix in pVisited.keys()
            isCandidate              = isTraversableBox and hasNotBeenVisited

        return isCandidate











if __name__ == '__main__':

    pass

