import time
from drone_api import DroneApi

API_PORT = 3000


if __name__ == "__main__":
    drone_api = DroneApi(API_PORT)
    drone_api.arm()
    time.sleep(1)
    drone_api.takeoff()
    time.sleep(5)
    drone_api.go_to(51.478, 5.343, 5)
    time.sleep(5)
    
    # Do magic here
    
    print('done')
