from mongoengine import connect, StringField, IntField, Document
import pymongo
#connect(db="cats", host="localhost")

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb['testing']

class CatBreed(Document):
	breed = StringField (required=True, max_length = 64)
	style = StringField()
	number_of_subspecies = IntField()

#b = CatBreed(
#	breed:"HI",
#	style:"Hungry",
#	number_of_subspecies :5,
#)

mydict = {"name":"testing", "address":"testing123"}


x = mycol.insert_one(mydict)

print(x)


