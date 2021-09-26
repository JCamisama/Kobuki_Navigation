from MapPositionCalculator import MapPositionCalculator

# Global assumptions:
#   - A positive step in x will be upward, a negative one will be downward
#   - A positive step in y will be leftward, a negative one will be rightward
#   - (0, 0) = The upper left corner of the map
#   - (n, n) = The lower right corner of the map, where n = boxSideSize - 1
#   - Each box is a square

def test_1_get_position_in_map():
    # Test case  1: Origin and Target positions are equal, return  tuple (0, 0), in meters
    positionCalculator = MapPositionCalculator()
    boxSideSize            = 0.36  # meters
    #   1.1. Origin = (0, 0)
    originPosition     = (0, 0)
    targetPosition     = (0, 0)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0, 0)
    #   1.2. Origin = (5, 5)
    originPosition     = (5, 5)
    targetPosition     = (5, 5)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0, 0)
    #   1.3. Origin = (3, 45)
    originPosition     = (3, 45)
    targetPosition     = (3, 45)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0, 0)


def test_2_get_position_in_map():
    # Test case  2: Origin and Target positions are different, return  tuple (x, y), in meters
    positionCalculator = MapPositionCalculator()
    boxSideSize            = 0.36  # meters
    #   2.1. Origin = (0, 0); Target = (0, 1) ---> (0, -0.36)
    originPosition     = (0, 0)
    targetPosition     = (0, 1)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0, -0.36)
    #   2.2. Origin = (0, 0); Target = (1, 0) ---> (-0.36, 0)
    originPosition     = (0, 0)
    targetPosition     = (1, 0)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (-0.36, 0)
    #   2.3. Origin = (0, 0); Target = (1, 1) ---> (-0.36, -0.36)
    originPosition     = (0, 0)
    targetPosition     = (1, 1)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (-0.36, -0.36)
    #   2.4. Origin = (1, 1); Target = (1, 0) ---> (0, 0.36)
    originPosition     = (1, 1)
    targetPosition     = (1, 0)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0, 0.36)
    #   2.5. Origin = (1, 1); Target = (0, 1) ---> (0.36, 0)
    originPosition     = (1, 1)
    targetPosition     = (0, 1)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0.36, 0)
    #   2.6. Origin = (1, 1); Target = (0, 0) ---> (0.36, 0.36)
    originPosition     = (1, 1)
    targetPosition     = (0, 0)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0.36, 0.36)
    #   2.7. Origin = (5, 5); Target = (0, 0) ---> (0.36 * 5, 0.36 * 5)
    originPosition     = (5, 5)
    targetPosition     = (0, 0)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0.36 * 5, 0.36 * 5)
    #   2.8. Origin = (5, 5); Target = (1, 3) ---> (0.36 * 4, 0.36 * 2)
    originPosition     = (5, 5)
    targetPosition     = (1, 3)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0.36 * 4, 0.36 * 2)
    #   2.9. Origin = (0, 0); Target = (5, 5) ---> (-0.36 * 5, -0.36 * 5)
    originPosition     = (0, 0)
    targetPosition     = (5, 5)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (-0.36 * 5, -0.36 * 5)
    #   2.10. Origin = (0, 0); Target = (4, 2) ---> (-0.36 * 4, -0.36 * 2)
    originPosition     = (0, 0)
    targetPosition     = (4, 2)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (-0.36 * 4, -0.36 * 2)
    #   2.11. Origin = (50, 50); Target = (100, 100) ---> (-0.36 * 50, -0.36 * 50)
    originPosition     = (50, 50)
    targetPosition     = (100, 100)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (-0.36 * 50, -0.36 * 50)
    #   2.12. Origin = (50, 50); Target = (0, 0) ---> (0.36 * 50, 0.36 * 50)
    originPosition     = (50, 50)
    targetPosition     = (0, 0)
    positionInMap      = positionCalculator.getPositionInMap(boxSideSize, originPosition, targetPosition)
    assert positionInMap == (0.36 * 50, 0.36 * 50)