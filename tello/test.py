from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

# tello.move_left(100)
tello.rotate_clockwise(360)
# tello.move_forward(100)

tello.land()



# tello.streamon()
# 
# while True:
#     pass