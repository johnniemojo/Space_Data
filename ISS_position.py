#import urllib2
import urllib.request
import json
from datetime import datetime

req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen(req)
the_page = response.read()

json_dump = json.loads(the_page)

#If the Api returned data successfully
if json_dump['message'] ==githib "success":
    Nowtime = datetime.fromtimestamp(json_dump['timestamp'])
    print("Signal acquired successfully at: " + str(Nowtime))
    print("Current ISS co-ordinates are: Latitude " + str(json_dump['iss_position']['latitude']) + " Longitude: " + str(json_dump['iss_position']['longitude']))
else:
    print("NO ISS positional signal received") 
# Example prints:
#   Signal acquired successfully at: 2020-06-13 12:48:38
#   Current ISS co-ordinates are: Latitude 48.2132 Longitude: 44.9570