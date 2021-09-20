

class Box:

    def __init__(self, pRow, pColumn, pIsTraversable=False):
        #x: int = row, y: int = column
        self.row           = pRow
        self.column        = pColumn
        self.traversable = pIsTraversable



    def equals(self, pOtherBox):

        areEqual = False
        if isinstance(pOtherBox, Box):
            return self.row == pOtherBox.row and self.column == pOtherBox.column



    def print_coordinates(self):
        print "(" + str(self.row) + ", " + str(self.column) + ", " + str(self.traversable) + ")\t", #Print without skipline in python 2.x


