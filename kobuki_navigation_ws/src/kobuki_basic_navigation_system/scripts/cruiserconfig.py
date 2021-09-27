#!/usr/bin/env python
import os
pathToFile = os.path.dirname(os.path.abspath(__file__))

mapDir     = pathToFile + "/maps/initial_tests/test_4_fully_traversable.txt"
boxSize    = 0.2  # meters
initialRow = 5
initialCol = 5
initialOrientation = 'North'
topic = 'order'