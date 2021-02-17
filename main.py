import requests
import datetime
MY_LAT = 23.064740
MY_LNG = 70.129860

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json#")

    response.raise_for_status()

    data = response.json()


    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude= float(data["iss_position"]["latitude"])

    iss_position = (longitude,latitude)

    #your position is within +5 or -5 degrees of the ISS position

        if MY_LAT-5<= iss_latitude <= MY_LAT+5 and MY_LNG-5<=iss_longitude<=MY_LNG:
            return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)
time_now = datetime.now()

print(time_now)