# ISS Tracker
###### Live location tracker for the International Space Station.
**Note: Project requires private API keys to work, which are not included in the source code for obvious security reasons. To see the site in action, [click here](https://dcxpython.pythonanywhere.com/).**

![Image of site in action](screenprint.png)

This project started as a simple Python script, written to learn how to use pre-existing APIs by making HTTP requests, and dealing with JSON data to extract what I needed. The original file took data from two APIs, sent data to a third, and configured the resulting information to be printed on the console window.

I had a lot of fun with this project, so I thought it would be ideal for my first attempt to move away from the console window, and learn how to use Python with a proper UI. This lead to me learning Flask so I could present the data with a bit of style in a web browser.

## Features:
- Display current latitude and longitude.
- Convert and display coordinates as nearest approximate address, {country, area, town} etc, or show body of water name if not above land.
- Display altitude and velocity, converted to both imperial and metric.
- Show visibility status (if ISS is in daylight or night).
- Show [what3words](https://what3words.com/) values and link to view location on what3words website.
- Link to view current location on Google Maps.
- List of current crew with names, profile images, nationalities and short bios (manually updated).
- Links to crew Wikipedia entries.
- Links to further reading, including Wikipedia main ISS article and official NASA website.

## Known Bugs:
- Issue with geocoding API which causes an index error when ISS is located over the South China Sea. This may apply to other areas but so far no others have been found in testing.

## Possible Improvements:
- Update the DOM in realtime (with consideration to API request frequency limits).
- Present location on map rather than linking to Google Maps in a new window.
- Responsive image sizes to reduce loading times on smaller screens.
- Further reading links and more information on the current ISS mission.
- Improved CSS.

## Credits:
- ISS data by http://open-notify.org and https://wheretheiss.at
- Geocoding by https://opencagedata.com
- Crew data and images from the official [NASA website](https://www.nasa.gov/mission_pages/station/expeditions/expedition61/index.html) and [Wikipedia](https://wikipedia.org).
