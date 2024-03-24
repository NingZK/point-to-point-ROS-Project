#!/usr/bin/env python


import rospy
from point_to_point.msg import cubic_traj_params,cubic_traj_coeffs
from point_to_point.srv import compute_cubic_traj,compute_cubic_trajRequest


def callback(data):
    # Print the message
    rospy.loginfo("Planner heard p0=%f",data.p0)
    rospy.loginfo("Planner heard pf=%f",data.pf)
    rospy.loginfo("Planner heard v0=%f",data.v0)
    rospy.loginfo("Planner heard vf=%f",data.vf)
    rospy.loginfo("Planner heard t0=%f",data.t0)
    rospy.loginfo("Planner heard tf=%f",data.tf)


   # A method that blocks until the service named compute_cubic_traj is available. 
    rospy.wait_for_service('compute_cubic_traj')
    try:
   # Create a handle for calling the service
       compute = rospy.ServiceProxy('compute_cubic_traj', compute_cubic_traj)      
       req = compute_cubic_trajRequest()
       req.p0 = data.p0
       req.pf = data.pf
       req.v0 = data.v0
       req.vf = data.vf
       req.t0 = data.t0
       req.tf = data.tf
       resp1 = compute.call(req)

       ctc = cubic_traj_coeffs()
       ctc.a0 = resp1.a0
       ctc.a1 = resp1.a1
       ctc.a2 = resp1.a2
       ctc.a3 = resp1.a3
       ctc.t0 = req.t0
       ctc.tf = req.tf  

       # Print a0,a1,a2,a3 to the screen
       rospy.loginfo("a0=%f",ctc.a0)
       rospy.loginfo("a1=%f",ctc.a1)
       rospy.loginfo("a2=%f",ctc.a2)
       rospy.loginfo("a3=%f",ctc.a3)

    except rospy.ServiceException as e:
       print("Service call failed: %s"%e)

    # Publish to "coeffs" topic 
    pub = rospy.Publisher('coeffs', cubic_traj_coeffs , queue_size=10)
    pub.publish(ctc)

def planner():
    #This declares that the node subscribes to the "params" topic
    rospy.init_node('planner', anonymous=True)
    rospy.Subscriber('params', cubic_traj_params, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    planner()

