#!/usr/bin/env python
from std_msgs.msg import String


class FlexmansysMsgHandler:
    # This class can handle all kinds of ROS messages delivered by FlexMansys.

    def __init__(self):
        print("Ready to handle Flexmansys messages!")


    def prepare_transport_orders(self, pInstructions):
        # Requires: String containing positions in the map  ---> '[pos1,pos2,...]'
        # Ensures:  Return an array of 2-dimensional tuples ---> (int, int)
        orderSequence       = []
        noBracketsOrders    = pInstructions.data[1:-1]
        orderSequenceString = noBracketsOrders.replace(' ', '').split(',') #

        for orderString in orderSequenceString:
            if(orderString[0] != '-'):
                newOrder = self.process_order_letterinteger_format(orderString)
                if newOrder: orderSequence.append(newOrder)

        return orderSequence



    def process_order_letterinteger_format(self, pOrderString):
        # Requires: String formatted as 'LetterNumber'       ---> 'A2'
        # Ensures:  Return a 2-dimensional tuple of integers ---> (0, 0)
        order       = None

        if(pOrderString):
            alphabet    = 'abcdefghijklmnopqrstuvwxyz'
            charMapping = {}
            for i in range(0, len(alphabet)):
                charMapping[alphabet[i]] = i

            row           = charMapping[ pOrderString.lower()[0:1] ]
            column        = int( pOrderString[1:] )
            order         = (row, column)

        return order





if __name__ == '__main__':
    flex = FlexmansysMsgHandler()
    msg = String()
    msg.data = '[C4, G9]'
    flex.prepare_transport_orders(msg)