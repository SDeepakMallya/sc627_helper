#!/usr/bin/env python

from sc627_helper.msg import MoveXYActionGoal, MoveXYActionResult
import rospy

def callback_result(data):

    #Lines 4,5,6

    #write to ouptut_base.txt
    
    go_to = MoveXYActionGoal()
    go_to.goal.pose_dest.x = 1 + data.result.pose_final.x
    pub.publish(go_to)

rospy.init_node('test', anonymous= True)
pub = rospy.Publisher('/move_xy/goal', MoveXYActionGoal, queue_size= 10)
rospy.Subscriber('/move_xy/result', MoveXYActionResult, callback_result)


go_to = MoveXYActionGoal()
go_to.goal.pose_dest.x = 1
pub.publish(go_to)


while not rospy.is_shutdown():
    rospy.spin()