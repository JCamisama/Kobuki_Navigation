from Box import Box


class BoxMatrixCreator:

    def create_matrix_of_boxes_from_txt(self, pMatrixMapPath):

        mapDoc      = open(pMatrixMapPath)
        allTheLines = mapDoc.readlines()
        boxMatrix   = self.initialize_matrix_of_boxes(allTheLines)

        return boxMatrix



    def initialize_matrix_of_boxes(self, pArrayOfRows):

        boxMatrix = []

        rowIndex = 0
        for row in pArrayOfRows:

            rowWithoutLineJump = row[:-1]
            columnsInThisRow   = row.split(",")
            rowOfBoxes         = self.create_row_of_boxes(columnsInThisRow, rowIndex)
            boxMatrix.append(rowOfBoxes)
            rowIndex           += 1

        return boxMatrix



    def create_row_of_boxes(self, pListOfColumnsInRow, pRowIndex):

        rowOfBoxes       = []
        columnIndex      = 0

        for column in pListOfColumnsInRow:
            isTraversable = bool(int(column)) # 0=False, 1=True
            newBox        = Box(pRowIndex, columnIndex, isTraversable)
            rowOfBoxes.append(newBox)
            columnIndex   += 1

        return rowOfBoxes




