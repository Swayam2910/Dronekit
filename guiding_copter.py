##POSITION CONTROL

import dronekit
import time
from dronekit import connect,VehicleMode,LocationGlobalRelative
from pymavlink import mavutil

vehicle=connect('127.0.0.1:14550',wait_ready=True)
# Set mode to guided - this is optional as the goto method will change the mode if needed.
vehicle.mode = VehicleMode("GUIDED")

# Set the target location in global-relative frame
a_location = LocationGlobalRelative(-34.364114, 149.166022, 30)
vehicle.simple_goto(a_location)

# Set airspeed using attribute
vehicle.airspeed = 5 #m/s

# Set groundspeed using attribute
vehicle.groundspeed = 7.5 #m/s

# Set groundspeed using `simple_goto()` parameter
vehicle.simple_goto(a_location, groundspeed=10)


##VELOCITY CONTROL

def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
    """
    Move vehicle in direction based on specified velocity vectors.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)


    # send command to vehicle on 1 Hz cycle
    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        time.sleep(1)