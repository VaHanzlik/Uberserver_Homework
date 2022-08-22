import requests
import os
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import datetime


security = HTTPBasic()
vip_api = FastAPI()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "vaclav")
    correct_password = secrets.compare_digest(credentials.password, "heslo")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )


@vip_api.get("/v1/now/")
async def datetime_now():

    return {"message": datetime.datetime.now().isoformat()}


@vip_api.get("/v1/VIP/{point_in_time}")
async def read_item(point_in_time: int = 2, _=Depends(get_current_username)):
    try:
        print(point_in_time)
        data_resp = requests.get(
            url=f"http://127.0.0.1:8088/v1/coords/{point_in_time}", timeout=4
        )
        message = {
            "source": "vip-db",
            "gpsCoords": {
                "lat": data_resp.json().get("latitude"),
                "long": data_resp.json().get("longitude"),
            },
        }
    except:
        raise HTTPException(status_code=408, detail="Timeout error")
    return {"message": message}
