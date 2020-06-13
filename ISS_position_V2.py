#Real time ISS tracker - www.101computing.net/real-time-ISS-tracker/

import json, turtle, urllib.request, time


#A first JSON request to retrieve the name of all the astronauts currently in space.
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("There are currently " + str(result["number"]) + " astronauts in space:")
print("")

people = result["people"]

for p in people:
  print(p["name"] + " on board of " + p["craft"])


#Display information on world map using Python Turtle
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
#Load the world map picture
screen.bgpic("world-map.gif")
  
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
  #A JSON request to retrieve the current longitude and latitude of the IIS space station (real time)  
  url = "http://api.open-notify.org/iss-now.json"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
    
  #Let's extract the required information
  location =result["iss_position"]
  lat = float(location["latitude"])
  lon = float(location["longitude"])
    
  #Output informationon screen
  print("\nLatitude: " + str(lat))
  print("Longitude: " + str(lon))
  
  #Plot the ISS on the map  
  iss.goto(lon, lat)
  #refresh position every 5 seconds
  time.sleep(5)
