#!/usr/bin/env python


import rospy
from std_msgs.msg import Float64
from ar_week5_test.msg import cubic_traj_coeffs


def callback(data):
    rospy.loginfo("Plotter heard a0=%f",data.a0)
    rospy.loginfo("Plotter heard a1=%f",data.a1)
    rospy.loginfo("Plotter heard a2=%f",data.a2)
    rospy.loginfo("Plotter heard a3=%f",data.a3)
    rospy.loginfo("Plotter heard t0=%f",data.t0)
    rospy.loginfo("Plotter heard tf=%f",data.tf)
    

    while not rospy.is_shutdown() and data.t0 < data.tf:
        # calculate the position_trajectory,velocity_trajectory and acceleration_trajectory
	data.t0 +=0.1
	position_trajectory = data.a0 + data.a1*data.t0 + data.a2*data.t0**2 +  data.a3*data.t0**3
	velocity_trajectory = data.a1 + 2*data.a2 +3*data.a3*data.t0**2
	acceleration_trajectory = 2*data.a2 + 3*data.a3*data.t0**2


        # Publish to 'trajPos','trajVel' and 'trajAcc' topic 
	pub_p = rospy.Publisher('trajPos', Float64 , queue_size=10)
	pub_v = rospy.Publisher('trajVel', Float64, queue_size=10)
	pub_a = rospy.Publisher('trajAcc', Float64, queue_size=10)
	rate = rospy.Rate(10)

	rospy.loginfo("position_trajectory=%f",position_trajectory)
	rospy.loginfo("velocity_trajectory=%f",velocity_trajectory)
	rospy.loginfo("acceleration_trajectory=%f",acceleration_trajectory)
       
        pub_p.publish(position_trajectory)
        pub_v.publish(velocity_trajectory)
        pub_a.publish(acceleration_trajectory)
        
        rate.sleep()
def ploter():
    # This declares that the node subscribes to the "coeffs" topic
    rospy.init_node('plotter', anonymous=True)
    rospy.Subscriber('coeffs', cubic_traj_coeffs, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    ploter()

