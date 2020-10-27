import os, socket
from fastapi import FastAPI

app = FastAPI()

APP_NAME = os.getenv('APP_NAME', 'MY API')
  
def get_Host_name_IP(): 
    """
    Function to display hostname and IP address 
    ref: https://www.geeksforgeeks.org/display-hostname-ip-address-python/
    """
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        return {
            "Hostname" : host_name,
            "IP" : host_ip,
        }
    except: 
        return "Unable to get Hostname and IP"

@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "APP_NAME" : APP_NAME,
        'host_info': get_Host_name_IP(),
    }
