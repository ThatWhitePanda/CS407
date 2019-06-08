from mongoengine import connect, StringField, IntField, Document
import pymongo
connect(db="cats", host="localhost")

class CatBreed(Document):
	breed = StringField (required=True, max_length = 64)
	style = StringField()
	number_of_subspecies = IntField()

#b = CatBreed(
#	breed:"HI",
#	style:"Hungry",
#	number_of_subspecies :5,
#)

CatBreed.insert({"name":"test"})


