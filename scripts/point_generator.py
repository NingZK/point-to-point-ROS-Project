#!/usr/bin/env python
import random
import rospy
from ar_week5_test.msg import cubic_traj_params 


def talker():
    # Publish to "params" topic and set rate
    pub = rospy.Publisher('params', cubic_traj_params , queue_size=10)
    rospy.init_node('generator', anonymous=True)
    rate = rospy.Rate(0.05) 
    # Generate the 6 different random values 
    while not rospy.is_shutdown():
        CTP = cubic_traj_params()
        CTP.p0 = random.uniform(-10,10)
        CTP.pf = random.uniform(-10,10)
        CTP.v0 = random.uniform(-10,10)
        CTP.vf = random.uniform(-10,10)
        CTP.t0 = 0
        dt = random.uniform(5,10)
        CTP.tf = CTP.t0 + dt
        # Print the message
        rospy.loginfo("p0=%f",CTP.p0)
        rospy.loginfo("pf=%f",CTP.pf)
        rospy.loginfo("v0=%f",CTP.v0)
        rospy.loginfo("vf=%f",CTP.vf)
        rospy.loginfo("t0=%f",CTP.t0)
        rospy.loginfo("tf=%f",CTP.tf)
        # Publish to the topic
        pub.publish(CTP)
         
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
