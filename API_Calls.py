import urllib.request
import json
"""
Capsules
Detailed info for serialized dragon capsules
    Get all capsules : GET /capsules
    Get one capsule : GET /capsules/:id
    Query capsules : POST /capsules/query
    lock Create a capsule : POST /capsules
    lock Update a capsule : PATCH /capsules/:id
    lock Delete a capsule : DELETE /capsules/:id
Cores
Detailed info for serialized first stage cores
    Get all cores : GET /cores
    Get one core : GET /v4/cores/:id
    Query cores : POST /cores/query
    lock Create a core : POST /cores - lock
    lock Update a core : PATCH /cores/:id - lock
    lock Delete a core : DELETE /cores/:id - lock
Crew
Detailed info on dragon crew members
    Get all crew members : GET /crew
    Get one crew member : GET /crew/:id
    Query crew members : POST /crew/query
Dragons
Detailed info about dragon capsule versions
    Get all dragons : GET /dragons
    Get one dragon : GET /dragons/:id
    Query dragons : POST /dragons/query
Landpads
Detailed info about landing pads and ships
    Get all landpads : GET /landpads
    Get one landpad : GET /landpads/:id
    Query landpads : POST /landpads/query
Launches
Detailed info about launches
    Get past launches : GET /launches/past
    Get upcoming launches : GET /launches/upcoming
    Get latest launches : GET /launches/latest
    Get next launches : GET /launches/next
    Get all launches : GET /launches
    Get one launch : GET /launches/:id
    Query launches : POST /launches/query
Launchpads
Detailed info about launchpads
    Get all launchpads : GET /launchpads
    Get one launchpad : GET /launchpads/:id
    Query launchpads : POST /launchpads/query
Payloads
Detailed info about launch payloads
    Get all payloads : GET /payloads
    Get one payload : GET /payloads/:id
    Query payloads : POST /payloads/query
Rockets
Detailed info about rocket versions
    Get all rockets : GET /rockets
    Get one rocket : GET /rockets/:id
    Query rockets : POST /rockets/query
Ships
Detailed info about ships in the SpaceX fleet
    Get all ships : GET /ships
    Get one ship : GET /ships/:id
    Query ships : POST /ships/query
Company Info
Detailed info about SpaceX as a company
    Get company info : GET /company
Roadster info
Detailed info about Elon's Tesla roadster's current position
    Get roadster info : GET /roadster
"""

req = urllib.request.Request('https://api.spacexdata.com/v4/payloads')
#req = urllib.request.Request('https://api.spacexdata.com/v4/roadster')
response = urllib.request.urlopen(req)
the_page = response.read()

json_dump = json.loads(the_page)
#print(json_dump[0])

print(len(json_dump))
#print(json.dumps(json_dump,indent=3, sort_keys = True))



for key in json_dump:
    print("Name: ", key["name"], "| Reused:", key["reused"],  "| Type:", key["type"], "| Customers: ", ", ".join(key["customers"]))
    #print(key)
    #print("{0} - {1}".format(i["name"], i["date_local"]))
    #print("Name: ", v["name"])
    
    

    #for value in key:
    #   print("Value: " + value)

        

"""
print("orignal list is : " + str(json_dump))


#res = [dict(zip(json_dump, i)) for i in zip(*json_dump.values())] 
  
# printing result 
#print ("The converted list of dictionaries " +  str(res)) 

for i in json_dump['flickr_images']:
    print(i)
    


for k in json_dump.keys():
    for i in json_dump[k]:
        print(k)


#response.close()
"""
