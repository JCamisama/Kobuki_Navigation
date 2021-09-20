#!/usr/bin/env python
from MatrixCreator import BoxMatrixCreator
from Box import Box


def test_1_matrix_of_boxes_creation():

    matrixTxtPath = "./maps/test_matrix_8x8.txt"
    matrixCreator = BoxMatrixCreator()
    boxMatrix     = matrixCreator.create_matrix_of_boxes_from_txt(matrixTxtPath)

    for rowOfBoxes in boxMatrix:
        for box in rowOfBoxes:
            box.print_coordinates()

        print("")



def test_2_matrix_size():

    matrixTxtPath = "./maps/test_matrix_8x8.txt"
    matrixCreator = BoxMatrixCreator()
    boxMatrix     = matrixCreator.create_matrix_of_boxes_from_txt(matrixTxtPath)

    assert len(boxMatrix) == 8
    assert len(boxMatrix[0]) == 8



def test_3_box_equality():

    referenceBox = Box(0, 0)
    equalBox     = Box (0, 0)
    diffBox1     = Box(0, 1)
    diffBox2     = Box(5, 0)
    diffBox3     = Box(45, 23)

    #Equal boxes
    assert referenceBox.equals(equalBox)

    #Different boxes
    assert not referenceBox.equals(diffBox1)
    assert not referenceBox.equals(diffBox2)
    assert not referenceBox.equals(diffBox3)





