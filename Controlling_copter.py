from dronekit import connect, VehicleMode , LocationGlobalRelative , Command
from pymavlink import mavutil
from time import sleep
import tkinter as tk

#Connecting the vehicle to UDP port.
vehicle=connect("udp:127.0.0.1:14550",wait_ready=True)

#Establishing connection with the drone
def arm_and_takeoff():
    takeoff_alt=10
    #pre-flight check
    while not vehicle.is_armable:
        print("Waiting to initialize...")
        sleep(1)
    vehicle.mode=VehicleMode("GUIDED")
    vehicle.armed=True
    while not vehicle.armed:
        print("Waiting for vehicle to get armed")
        sleep(1)
    print("Vehicle armed...Ready for Take off")
    vehicle.simple_takeoff(takeoff_alt)
    while True:
            print("altitude: {val}".format(val=vehicle.location.global_relative_frame.alt))
            if vehicle.location.global_relative_frame.alt>=takeoff_alt*0.95:
                print("target altitude reached")
                break
            sleep(1)
#Generating MAVlink message which specifies speed components. 
def send_body_ned_velocity(velocity_x,velocity_y,velocity_z,duration):
    msg=vehicle.message_factory.set_position_target_local_ned_encode(
        0,       
        0, 0,    
        mavutil.mavlink.MAV_FRAME_BODY_NED, 
        0b0000111111000111, 
        0, 0, 0, 
        velocity_x, velocity_y, velocity_z, 
        0, 0, 0, 
        0, 0)
    for x in range(duration):
        vehicle.send_mavlink(msg)
        vehicle.flush()

#Binding keyboard with tkinter.
def key(event):
    ##keysym : A single-character string that is the key's code (only for keyboard events)
    ##char : A string that is the key's symbolic name (only for keyboard events)
    if event.char==event.keysym:  
        if event.keysym == 'r':
            vehicle.mode=VehicleMode("RTL") ##land the drone
    else:
        if event.keysym=='Up':
            send_body_ned_velocity(0,100,0,1)
        elif event.keysym=='Down':
            send_body_ned_velocity(0,-100,0,1)
        elif event.keysym=='Left':
            send_body_ned_velocity(-100,0,0,1)
        elif event.keysym=='Right':
            send_body_ned_velocity(100,0,0,1)


arm_and_takeoff()

#Reading the keyboard using tkinter
root=tk.Tk() ##opening the tkinter window
print("Control the drone using your arrow keys")
print("Press R for RTL mode")
root.bind_all("<Key>",key)
root.mainloop() #infinite while loop