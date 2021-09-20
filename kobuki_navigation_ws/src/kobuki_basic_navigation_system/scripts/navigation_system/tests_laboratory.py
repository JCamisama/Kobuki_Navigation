#!/usr/bin/env python
from Laboratory import Laboratory
from Box import Box




def test_1_matrix_initialization():

    matrixTxtPath = "./maps/test_matrix_8x8.txt"
    laboratoryMap = Laboratory(matrixTxtPath)

    for rowOfBoxes in laboratoryMap.matrix:
        for box in rowOfBoxes:
            box.print_coordinates()

        print("")



def test_2_is_valid_box():

    matrixTxtPath = "./maps/test_matrix_8x8.txt"
    laboratoryMap = Laboratory(matrixTxtPath)

    # Invalid box
    nullBox = None
    assert not laboratoryMap.is_valid_box(nullBox)

    #Invalid box
    nonTraversableBox = Box(0, 0)
    assert not laboratoryMap.is_valid_box(nonTraversableBox)

    #Valid box
    traversableBox = Box(7, 0)
    assert laboratoryMap.is_valid_box(traversableBox)



def test_3_is_a_candidate():

    matrixTxtPath = "./maps/test_matrix_8x8.txt"
    laboratoryMap = Laboratory(matrixTxtPath)


    visitedBoxes = {laboratoryMap.matrix[7][0]: None,
                    laboratoryMap.matrix[7][1]: None,
                    laboratoryMap.matrix[7][2]: None
                    }

    # Box out of matrix boundaries
    assert not laboratoryMap.is_a_candidate(-2, -5, visitedBoxes)

    # Non-traversable box
    assert not laboratoryMap.is_a_candidate(0, 0, visitedBoxes)

    # visited box
    assert not laboratoryMap.is_a_candidate(7, 2, visitedBoxes)

    # visited box
    assert  laboratoryMap.is_a_candidate(7, 4, visitedBoxes)



def test_4_get_get_shortest_path_BFS():

    matrixTxtPath = "./maps/test_matrix_short_paths.txt"
    laboratoryMap = Laboratory(matrixTxtPath)

    sourceBox    = Box(7, 0, True)
    destBox      = Box(0, 7, True)
    shortestPath = laboratoryMap.get_shortest_path_BFS(sourceBox, destBox)

    for box in shortestPath:
        box.print_coordinates()
        print("")




