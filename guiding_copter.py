import dronekit
import time
from dronekit import connect,VehicleMode,LocationGlobalRelative
from pymavlink import mavutil

vehicle=connect('127.0.0.1:14550',wait_ready=True)
#Guided mode is more preferred.
vehicle.mode = VehicleMode("GUIDED")

# Set the target location with respect to home location.
a_location = LocationGlobalRelative(-34.364114, 149.166022, 30)
vehicle.simple_goto(a_location)

# Set airspeed 
vehicle.airspeed = 5 #m/s

# Set groundspeed 
vehicle.groundspeed = 7.5 #m/s

#Going to specific location using specified velocity.
vehicle.simple_goto(a_location, groundspeed=10)


#The function specifies speed component of vehicle in global relative frame.

def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
    """
    Move vehicle in direction based on specified velocity vectors.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       
        0, 0,    t
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, 
        0, 0, 0, 
        velocity_x, velocity_y, velocity_z,
        0, 0, 0, 
        0, 0)    


 
    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        time.sleep(1)
