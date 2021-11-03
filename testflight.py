# Information: https://clover.coex.tech/programming

import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

node_list = [90, 94, 99, 49, 9, 4, 0, 40, 44]

print('Take off and hover 4 m above the ground')
navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)
rospy.sleep(5)

print('Fly to Marker 90')
navigate(frame_id='aruco_90', x=0, y=0, z=1)
rospy.sleep(5)

print('Fly to Marker 94')
navigate(x=4, y=0, z=0, frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate(frame_id='aruco_94', x=0, y=0, z=1)
rospy.sleep(5)

print('Fly to Marker 99')
navigate(x=5, y=0, z=0, frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate(frame_id='aruco_99', x=0, y=0, z=1)
rospy.sleep(5)

print('Fly to Marker 49')
navigate(x=0, y=5, z=0, frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate(frame_id='aruco_49', x=0, y=0, z=1)
rospy.sleep(5)

print('Fly to Marker 9')
navigate(x=0, y=4, z=0, frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate(frame_id='aruco_9', x=0, y=0, z=1)
rospy.sleep(5)

print('Fly to Marker 4')
navigate(x=-5, y=0, z=0, frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate(frame_id='aruco_4', x=0, y=0, z=1)
rospy.sleep(5)

print('Fly to Marker 0')
navigate(x=-4, y=0, z=0, frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate(frame_id='aruco_0', x=0, y=0, z=1)
rospy.sleep(5)

print('Fly to Marker 40')
navigate(x=0, y=-4, z=0, frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate(frame_id='aruco_40', x=0, y=0, z=1)
rospy.sleep(5)

print('Fly to Marker 44')
navigate(x=4, y=0, z=0, frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate(frame_id='aruco_44', x=0, y=0, z=1)
rospy.sleep(5)

navigate(x=0, y=0, z=0, yaw=float('nan'), yaw_rate=1.0, frame_id='body')
rospy.sleep(10)


print('Perform landing')
land()

