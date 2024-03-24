#!/usr/bin/env python

import rospy
import numpy as np
from point_to_point.srv import compute_cubic_traj,compute_cubic_trajResponse


def handle_compute_four_values(data):
    CCTR = compute_cubic_trajResponse()

    # Using matrix operation to solve a0,a1,a2,a3
    A = np.array([[1,data.t0,np.square(data.t0),np.power(data.t0,3)],
                  [0,1,2*data.t0,3*np.square(data.t0)],
                  [1,data.tf,np.square(data.tf),np.power(data.tf,3)],
                  [0,1,2*data.tf,3*np.square(data.tf)]])
    B = np.array([data.p0,data.v0,data.pf,data.vf])
    X = np.linalg.inv(A).dot(B)

    CCTR.a0 = X[0]
    CCTR.a1 = X[1]
    CCTR.a2 = X[2]
    CCTR.a3 = X[3]

    rospy.loginfo("a0=%f",CCTR.a0)
    rospy.loginfo("a1=%f",CCTR.a1)
    rospy.loginfo("a2=%f",CCTR.a2)
    rospy.loginfo("a3=%f",CCTR.a3)

    return CCTR

def compute_four_values_server():
    # Declare the node and service
    rospy.init_node('compute_cubic_coeffs')
    s = rospy.Service('compute_cubic_traj', compute_cubic_traj, handle_compute_four_values)
    rospy.spin()

if __name__ == "__main__":
    compute_four_values_server()



