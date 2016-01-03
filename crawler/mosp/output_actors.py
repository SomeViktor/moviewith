from pymongo import MongoClient
client = MongoClient()
mo = client['mo']
import json
actors = [];

for actor in mo.actors.find():
	actors.append(actor['name']);
	#print actor['name']

json_actors = json.dumps(actors)

print json_actors
f = open("actors.json", "w+");
f.write(json_actors);
