from dronekit import connect, VehicleMode

# sitl = dronekit_sitl.start_default()
# connection_string = sitl.connection_string()

# Import DroneKit-Python

connection_string = "127.0.0.1:14550"
# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

# Get some vehicle attributes (state)
print("Get some vehicle attribute values:")
print("GPS: " + str(vehicle.gps_0))
print("Battery: " + str(vehicle.battery))
print("Last Heartbeat: " + str(vehicle.last_heartbeat))
print("Is Armable?: " + str(vehicle.is_armable))
print("System status: " + str(vehicle.system_status.state))
print("Mode: " + str(vehicle.mode.name))  # settable

# vehicle.simple_takeoff(100)

# vehicle.mode = VehicleMode("LAND")

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
# sitl.stop()
print("Completed")
