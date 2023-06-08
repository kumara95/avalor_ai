import json
from config import API_URL
from util import get, post


class DroneApi:
    def __init__(self, port):
        self.port = port
        self.url = f"{API_URL}:{port}"

    def arm(self):
        arm_url = f"{self.url}/arm"
        post(arm_url)

    def takeoff(self):
        take_off_url = f"{self.url}/takeoff"
        post(take_off_url)

    def go_to(self, lat, lon, alt,angle):
        data = {
            "lat": lat,
            "lon": lon,
            "alt": alt
            "angle":angle
        }
        post(f"{self.url}/waypoint", data)

    def get_speed(self):
        speed_url = f"{self.url}/speed"
        speed = get(speed_url)
        if speed == False:
            return 0
        json_data = json.loads(speed)
        return float(json_data['speed'])
    
    def get_position(self):
        pos_url = f"{self.url}/position"
        pos = get(pos_url)
        if pos == False:
            return {}
        return json.loads(pos)
    def get_heading(self,angle):
        data = {
            "angle": angle,
        }
        post(f"{self.url}/heading",data)
    
    # Todo: Add more functions here