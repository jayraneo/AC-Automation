import os
from dotenv import load_dotenv
from ACC import ACController

load_dotenv()

API_KEY = os.getenv("API_KEY")
PAT = os.getenv("PAT")
DEVICE_ID = os.getenv("DEVICE_ID")
COUNTRY = os.getenv("COUNTRY")

ac = ACController(API_KEY=API_KEY, PAT=PAT, DEVICE_ID=DEVICE_ID, COUNTRY=COUNTRY)
ac.turn_on()

# AIR_DRY, COOL, FAN, AUTO

# HIGH, AUTO, LOW, MID