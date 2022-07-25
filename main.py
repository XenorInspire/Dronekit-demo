from dronekit import connect, LocationGlobalRelative, VehicleMode
import time
import random

LOCATION = [
    {'lat': 37.22863301,
     'lng': -115.81035209},
    {'lat': 37.22919065,
     'lng': -115.81361144},
    {'lat': 37.23096966,
     'lng': -115.81555658},
    {'lat': 37.2321988,
     'lng': -115.81657843},
    {'lat': 37.23435757,
     'lng': -115.81394365},
    {'lat': 37.23868995,
     'lng': -115.81725158},
    {'lat': 37.24019222,
     'lng': -115.81470943},
    {'lat': 37.24326259,
     'lng': -115.813226},
]


def arm_and_takeoff(aTargetAltitude, vehicle):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print("Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude*0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


def guard_spawning(vehicle, i):
    print("!!!!! [GUARD DETECTED! ROTATING!] !!!!!")
    new_location = LocationGlobalRelative(
        float(LOCATION[i]['lat']), float(LOCATION[i]['lng']), 10)
    vehicle.simple_goto(new_location)
    while round(vehicle.location.global_frame.lat, 4) != round(LOCATION[i]['lat'], 4) and round(vehicle.location.global_frame.lon, 4) != round(LOCATION[i]['lng'], 4):
        print('Progress....')
        time.sleep(1)


def shooting_down(vehicle):
    print("!!!!! [GUARD IS SHOOTING DOWN THE DRONE!] !!!!!")
    vehicle.mode = VehicleMode("LAND")
    print["CONNEC...TION... LOS...."]
    exit()


def go_to_next_location(vehicle, i):
    print("--- [GO TO NEXT LOCATION] ---")
    print('LAT : ' + str(LOCATION[i]['lat']))
    print('LNG : ' + str(LOCATION[i]['lng']))
    new_location = LocationGlobalRelative(
        float(LOCATION[i]['lat']), float(LOCATION[i]['lng']), 10)
    vehicle.simple_goto(new_location)
    while round(vehicle.location.global_frame.lat, 4) != round(LOCATION[i]['lat'], 4) and round(vehicle.location.global_frame.lon, 4) != round(LOCATION[i]['lng'], 4):
        print('Progress....')
        time.sleep(1)


vehicle = connect('127.0.0.1:14550', wait_ready=True)
choice = ''
arm_and_takeoff(10, vehicle)
i = 0
while choice.lower() != 'quit':
    if i + 1 == len(LOCATION):
        i = 0
    print("1) NEXT LOCATION")
    print("QUIT) EXIT")
    choice = input('Select your action')

    if choice == '1':
        go_to_next_location(vehicle, i)

        i += 1
        a = random.randint(1, 4)
        time.sleep(3)
        if a == 1:
            guard_spawning(vehicle, i)
        
        if a == 2:
            shooting_down(vehicle)


vehicle.mode = VehicleMode("RTL")
vehicle.mode = VehicleMode("LAND")
vehicle.close()