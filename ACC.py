import requests
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

class ACController:
    BASE_URL = os.getenv('API_LINK')
    res_status = {}

    def __init__(self, API_KEY, PAT, DEVICE_ID, COUNTRY):
        self.api_key = API_KEY
        self.pat = PAT
        self.device_id = DEVICE_ID
        self.country = COUNTRY

        self.header = {
            "Authorization": f"Bearer {self.pat}",
            "x-api-key": (self.api_key),
            "Content-Type": "application/json",
            "x-client-id":'JAY0066',
            "x-country": str(self.country),
            "x-message-id": str(uuid.uuid4())
        }

    def get_status(self):
        url = f"{self.BASE_URL}/devices/{self.device_id}/state"
        res = requests.get(url, headers=self.header)
        print("STATUS CODE:", res.status_code)
        print("RAW RESPONSE:", res.text)
        self.res_status = res.json()

        try:
            return res.json()
        except Exception as e:
            return {"error": "Response not JSON", "details": res.text, "status_code": res.status_code}
        
    def turn_on(self):
        url = f"{self.BASE_URL}/devices/{self.device_id}/control"
        data={
            "operation": {
                "airConOperationMode": "POWER_ON"
            }
        }
        res = requests.post(url,headers=self.header ,json=data)
        print("STATUS CODE:", res.status_code)
        print("RAW RESPONSE:", res.text)
    
    def turn_off(self):
        url = f"{self.BASE_URL}/devices/{self.device_id}/control"
        data={
            "operation": {
                "airConOperationMode": "POWER_OFF"
            }
        }
        res = requests.post(url, headers=self.header, json=data)
        print("STATUS CODE:", res.status_code)
        print("RAW RESPONSE:", res.text)

    def set_temperature(self, temp: int):
        url = f"{self.BASE_URL}/devices/{self.device_id}/control"
        data={
            "temperature": {
                "targetTemperature": f"{temp}",
                "unit": "C"
            },
        }
        res = requests.post(url, headers=self.header, json=data)
        print("STATUS CODE:", res.status_code)
        print("RAW RESPONSE:", res.text)
    
    def set_mode(self, mode: str):
        url = f"{self.BASE_URL}/devices/{self.device_id}/control"
        data={
            "airConJobMode": {
                "currentJobMode": f"{mode}"
            },
        }
        res = requests.post(url, headers=self.header, json=data)
        print("STATUS CODE:", res.status_code)
        print("RAW RESPONSE:", res.text)

    def set_fan_speed(self, speed: str):
        url = f"{self.BASE_URL}/devices/{self.device_id}/control"
        data={
            "airFlow":{
                "windStrength": f"{speed}"
            }
        }
        res = requests.post(url, headers=self.header, json=data)
        print("STATUS CODE:", res.status_code)
        print("RAW RESPONSE:", res.text)