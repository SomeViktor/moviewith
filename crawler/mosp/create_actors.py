from pymongo import MongoClient
client = MongoClient()
mo = client['mo']
actors = []
import sys


mo.actors.drop();
print "inserting actors into database:"
not_inserted = 0;
inserted = 0;
for movie in mo.movies.find():
	for actor in movie['actors']:
		actordict = { 'name' : actor};
		f = mo.actors.find(actordict).count();
		if f:
			not_inserted += 1;	
		else:
			mo.actors.insert(actordict);
			inserted += 1;
			sys.stdout.write("\r" + str(inserted))
print ""
print "actors inserted to database, number:",mo.actors.count()
print "did not insert ", not_inserted , "duplicates"
