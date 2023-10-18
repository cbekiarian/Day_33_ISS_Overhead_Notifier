import requests
from datetime import datetime
import smtplib
MY_LAT = 40.519218 # Your latitude
MY_LONG = 21.268169 # Your longitude
import time

def check_ISS():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT > iss_latitude +5 or MY_LAT < iss_latitude -5 or MY_LONG > iss_longitude+5 or MY_LONG < iss_longitude -5:
        return False
    else:
        return True
    #Your position is within +5 or -5 degrees of the ISS position.

def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour
    if hour_now > sunrise and hour_now< sunset:
        return False
    else:
        return True

while(True):
    if check_ISS() and is_dark():
        my_email = "xristakos167@gmail.com"
        password = "sqpl gruy raxn hyyh"
        to_email= "cbekiarian@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:ISS Above \n\n The ISS is in viewin distance and its dark. go out and see")
    time.sleep(60)
    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.



