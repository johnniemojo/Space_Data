#import urllib2
import urllib.request
import json
from datetime import datetime
import geocoder

NumPasses = 15

#where am I?
#Can I get location usinf python
g = geocoder.ip('me')
#print(g.latlng)
#print(type(g.latlng))
latitude = str(g.latlng[0])
longitude = str(g.latlng[1])
#print(str(latitude))
#print(str(longitude))

req = urllib.request.Request("http://api.open-notify.org/iss-pass.json?lat="+latitude + "&lon=" +longitude + "&n="+ str(NumPasses))


response = urllib.request.urlopen(req)
the_page = response.read()

json_dump = json.loads(the_page)

#If the Api returned data successfully
if json_dump['message'] == "success":
    #print(json_dump.keys())
    #print(json_dump.values())
    for key in json_dump:
        #if (type(json_dump[key])) is dict:
        if type(json_dump[key]) is dict:
            print("As at:" , str(datetime.fromtimestamp(json_dump[key]["datetime"])) + " the next " + str(NumPasses) + " ISS passes over your location is:")
        if type(json_dump[key]) is list:
            for passes in range (0,len(json_dump[key])):
                overhead = json_dump['response'][passes]['risetime']
                DurationSecs = json_dump['response'][passes]['duration']
                print(str(passes+1) + "th ISS pass is at : " + str(datetime.fromtimestamp(overhead)) + " and lasts " + str(DurationSecs) + " secs")
else:
    print("NO ISS positional signal received") 
# Example prints:
