from pymongo import MongoClient
client = MongoClient()
mo = client['mo']

print type(mo.movies)

print "number of movie entries:" , mo.movies.count()

print "number of actor entries:" , mo.actors.count()
#for movie in mo.movies.find():
#	print movie['title'];
#	print "actors:", movie['actors']
