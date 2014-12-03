#!/usr/bin/env python

import sys
sys.path.append('/home/akarbarc/ws_irp6/underlay/src/irp6_robot/irp6_bringup/scripts/IRPOS')

from IRPOS import *
from test_pkg.msg import Checker

class CheckersIRPOS(IRPOS):
	
	def __init__(self, nodeName, robotName, robotJointNumbers):
		IRPOS.__init__(self, nodeName, robotName, robotJointNumbers)
	
	def prepare_to_game(self):
		IRPOS.move_to_joint_position(self, [0, -1.4791420483915523, -0.16173032244035423, 0.07007528019972864, 4.712388138719054, -1.5707949127454675], 6.00)
		IRPOS.move_to_cartesian_pose(self, 3.00, Pose(Point(0.9, 0, 1.21), Quaternion(0, 1, 0, 0)))
	
	def temp_podnies_pionek_bez_wizji(self):
		IRPOS.tfg_to_joint_position(self, 0.078, 10.00)
		IRPOS.move_rel_to_cartesian_pose_with_contact(self, 20.00, Pose(Point(0, 0, -0.20), Quaternion(0, 0, 0, 0)), Wrench(Vector3(0.0, 0.0, 2.0), Vector3(0.0, 0.0, 0.0)))
		IRPOS.move_rel_to_cartesian_pose(self, 10.00, Pose(Point(0, 0, 0.005), Quaternion(0, 0, 0, 0)))
		IRPOS.tfg_to_joint_position(self, 0.063, 10.00)
		IRPOS.move_rel_to_cartesian_pose(self, 10.00, Pose(Point(0, 0, 0.1), Quaternion(0, 0, 0, 0)))
	

def callback(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %d %d %d",data.type,data.x,data.y)

def listener():

    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The 
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaenously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("from_discode", Checker, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	listener()
	#irpos = CheckersIRPOS("IRpOS", "Irp6p", 6)
	#irpos.move_to_synchro_position(10.0)
	#irpos.prepare_to_game()
	#irpos.temp_podnies_pionek_bez_wizji()
	