from dronekit import connect,VehicleMode

vehicle=connect('127.0.0.1:14550',wait_ready=True)

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
