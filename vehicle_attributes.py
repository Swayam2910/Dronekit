print("Start simulator (SITL)")
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()


from dronekit import connect,VehicleMode

vehicle=connect(connection_string,wait_ready=True)

#some attributes of vehicle.
print ("Global Location: %s" % (vehicle.location.global_frame))
print ("Global Location (relative altitude): %s" % (vehicle.location.global_relative_frame))
print ("Local Location: %s" % (vehicle.location.local_frame))   
print ("Attitude: %s" % (vehicle.attitude))
print ("Velocity: %s" % (vehicle.velocity))
print ("Groundspeed: %s" % (vehicle.groundspeed))
print ("Airspeed: %s" % (vehicle.airspeed))
print ("Gimbal status: %s" % (vehicle.gimbal))
print("Armed? %s" %(vehicle.armed))

vehicle.close()

sitl.stop()