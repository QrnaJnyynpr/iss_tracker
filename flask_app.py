import requests
import datetime
from flask import Flask, render_template, url_for
from keys import private_key # File included in .gitignore for security
from crew_data import crew_data

app = Flask(__name__)

@app.route("/")
def root():
	# Time of data request
	x = datetime.datetime.now()
	time = f"Updated on: {x.date()} at {x.strftime('%X')}\n"

	# API for coordinates
	iss_url = "http://api.open-notify.org/iss-now.json"
	iss_data = requests.get(iss_url, headers={"Accept": "application/json"}).json()
	latitude = iss_data["iss_position"]["latitude"]
	longitude = iss_data["iss_position"]["longitude"]

	# # Convert lat/long to approximate address
	# location_url = "https://api.opencagedata.com/geocode/v1/json"

	# API to convert coordinates to real location data
	location_data = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={latitude}%2C%20{longitude}&key={private_key}&language=en&pretty=1").json()

	# Country information not available when ISS is over ocean
	if "country" in location_data["results"][0]["components"]:
		continent = location_data["results"][0]["components"]["continent"]
		location = f'{location_data["results"][0]["formatted"]}, {continent}'
	else:
		location = location_data["results"][0]["components"]["body_of_water"]

	# Second API to pull additional data
	iss_second = requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()

	visibility = iss_second["visibility"]
	altitude_km = round(iss_second["altitude"], 2)
	altitude_mi = round(altitude_km/1.609, 2)

	velocity_kph = round(iss_second["velocity"], 2)
	velocity_mph = round(velocity_kph/1.609 , 2)

	# Request what3words data
	w3w = location_data["results"][0]["annotations"]["what3words"]["words"]

	return render_template('index.html', 
	time=time,
	visibility=visibility,
	altitude_km=altitude_km,
	altitude_mi=altitude_mi,
	location=location,
	velocity_kph=velocity_kph,
	velocity_mph=velocity_mph,
	w3w=w3w,
	crew_data=crew_data,
	latitude=latitude,
	longitude=longitude
)

if __name__ == '__main__':
    app.run()