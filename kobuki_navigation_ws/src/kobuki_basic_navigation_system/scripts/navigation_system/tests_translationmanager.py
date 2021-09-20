#!/usr/bin/env python
from TranslationManager import TranslationManager
import rospy


def do_test_perform_translation_1():
    #test case 1: 0.36 meters

    linearDistance     = 0.36 #meters
    translationManager = TranslationManager(linearDistance)
    rospy.sleep(1)

    translationManager.perform_translation()





if __name__ == '__main__':
    rospy.init_node('translation_manager', anonymous=True)
    do_test_perform_translation_1()