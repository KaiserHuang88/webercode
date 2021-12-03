import rospy
import time
import math
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight') # 'flight' is name of your ROS node

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

#Take off and Hover 1m above ground
navigate(x=0, y=0, z=1, speed=0.5, frame_id='body', auto_arm=True)
rospy.sleep(3)

navigate(x=0, y=0, z=1,yaw=float('nan'), frame_id='aruco_map')
rospy.sleep(5)
telemetry = get_telemetry(frame_id='aruco_map')
print (telemetry.x, telemetry.y, 'Height: ', telemetry.z,'m')
print ("Success")

navigate(x=1, y=0, z=1,yaw=float('nan'), frame_id='aruco_map')
rospy.sleep(5)
telemetry = get_telemetry(frame_id='aruco_map')
print (telemetry.x, telemetry.y, 'Height: ', telemetry.z,'m')
print ("Success")

navigate(x=1, y=1, z=1,yaw=float('nan'), frame_id='aruco_map')
rospy.sleep(5)
telemetry = get_telemetry(frame_id='aruco_map')
print (telemetry.x, telemetry.y, 'Height: ', telemetry.z,'m')
print ("Success")

navigate(x=0, y=1, z=1,yaw=float('nan'), frame_id='aruco_map')
rospy.sleep(5)
telemetry = get_telemetry(frame_id='aruco_map')
print (telemetry.x, telemetry.y, 'Height: ', telemetry.z,'m')
print ("Success")

navigate(x=0, y=0, z=1,yaw=float('nan'), frame_id='aruco_map')
rospy.sleep(6)
telemetry = get_telemetry(frame_id='aruco_map')
print (telemetry.x, telemetry.y, 'Height: ', telemetry.z,'m')
print ("Success")


navigate(x=0, y=0, z=0.15, speed=0.4,yaw=float('nan'), frame_id='aruco_map')
rospy.sleep(3)
telemetry = get_telemetry(frame_id='aruco_map')
print (telemetry.x, telemetry.y, 'Height: ', telemetry.z,'m')
print ("Success")

res = land()
if res.success:
        print 'drone has landed'
