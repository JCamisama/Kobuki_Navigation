#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import cruiserconfig as config


squarePath    = "[A5, A0, F0, F5]"
testRidePath  = "[Z9, D3, A4, E4, E5, E0, A0, F5]"

def talker(pOrders):
    pub = rospy.Publisher(config.topic, String, queue_size=10)
    rospy.init_node('instructorMockup', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # while not rospy.is_shutdown():
    #     orders = "[A0, F5]"
    #     rospy.loginfo(orders)
    #     pub.publish(orders)
    #     rate.sleep()

    rospy.loginfo(pOrders)
    pub.publish(pOrders)
    rate.sleep()
    print("Order Sent!")



def sequential_orders():
    pub = rospy.Publisher(config.topic, String, queue_size=10)
    rospy.init_node('instructorMockup', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    # while not rospy.is_shutdown():
    #     orders = "[A0, F5]"
    #     rospy.loginfo(orders)
    #     pub.publish(orders)
    #     rate.sleep()

    command = ''
    while (command != '-1'):
        command = raw_input('Please, enter a new position (A-F 0-5): ' )
        newOrder = '['+command+']'
        rospy.loginfo(newOrder)
        pub.publish(newOrder)
        rate.sleep()
    print("Bye bye!")




if __name__ == '__main__':

    print('Please, choose the demo type: \n 1. Provide commands through CLI \n 2. Square path demo\n\n')
    option = int( input('Your choice: ') )
    print('\n\n')
    try:
        if(option == 1):
            sequential_orders()
        elif( option == 2):
            orders = squarePath
            # orders = testRidePath
            talker(orders)
        else:
            print('Closing the tester...\n\n')


    except rospy.ROSInterruptException:
        pass