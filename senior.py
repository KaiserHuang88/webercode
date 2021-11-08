import rospy
import time
import math
from clover import srv
from std_srvs.srv import Trigger
from aruco_pose.msg import MarkerArray

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
land = rospy.ServiceProxy('land', Trigger)

aruco_id = 'aruco_90'

def markers_callback(msg):
    for marker in msg.markers:
        aruco_id = 'aruco_' + str(msg.markers[0].id)

rospy.Subscriber('aruco_detect/markers', MarkerArray, markers_callback)

def navigate_wait(x=0, y=0, z=0, yaw=float('nan'), speed=0.5, frame_id='', auto_arm=False, tolerance=0.1):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

navigate_wait(x=0, y=0, z=0.5, speed=1.0, frame_id='body', auto_arm=True)

count = 1

while (count <= 3):
    navigate_wait(x=0, y=0, z=count, speed=0.5, frame_id=aruco_id)

    rospy.sleep(5.0)
    telemetry = get_telemetry(frame_id=aruco_id)
    print("Height: ", telemetry.z, 'm')
    print("Success")

    navigate(x=0, y=0, z=count, yaw=float('nan'), yaw_rate=0.5, frame_id=aruco_id)
    rospy.sleep(12.56)
    telemetry = get_telemetry(frame_id=aruco_id)
    print("Yaw Rate: ", telemetry.yaw_rate, "rad/sec")
    print("Success")
    navigate(yaw=float('nan'), yaw_rate=0.0, frame_id='body')

    count = count + 1

rospy.sleep(5.0)

navigate_wait(frame_id=aruco_id, x=0, y=0, z=0.4, speed=1.0)
print("Landing on: ", aruco_id)
res = land()
if res.success:
    print("Drone has landed")


