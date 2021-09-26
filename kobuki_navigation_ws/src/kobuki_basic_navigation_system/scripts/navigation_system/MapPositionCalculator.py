

# Global assumptions:
#   - A positive step in x will be upward, a negative one will be downward
#   - A positive step in y will be leftward, a negative one will be rightward
#   - (0, 0) = The upper left corner of the map
#   - (n, n) = The lower right corner of the map, where n = boxSideSize - 1
#   - Each box is a square

class MapPositionCalculator:

    def __init__(self):
        print("\nMap position calculator ready to get after it\n")

    def getPositionInMap(selfs, pBoxSideSize, pOriginPosition, pTargetPosition):
        # Requires:
        #   - pBoxSideSize: Size of the side of a square box, in meters
        #   - pOriginPosition: 2D tuple of integers --> (int, int)
        #   - pTargetPosition: 2D tuple of integers --> (int, int)
        #   - pOriginPosition and pTargetPosition are inside the map boundaries
        #   - pOriginPosition and pTargetPosition are traversable in the map
        # Ensures:
        #   - Return 2D tuple of floats, indicating exact x and y positions
        rowPosition = - (pTargetPosition[0] - pOriginPosition[0]) * pBoxSideSize
        colPosition = - (pTargetPosition[1] - pOriginPosition[1]) * pBoxSideSize
        return (rowPosition, colPosition)

