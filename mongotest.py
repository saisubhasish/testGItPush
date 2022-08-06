import pymongo


client = pymongo.MongoClient("mongodb://sai1118:Sai1234@ac-hfsjren-shard-00-00.d8m7g8f.mongodb.net:27017,ac-hfsjren-shard-00-01.d8m7g8f.mongodb.net:27017,ac-hfsjren-shard-00-02.d8m7g8f.mongodb.net:27017/?ssl=true&replicaSet=atlas-z7p8m3-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
d = {
     'name' : 'Sai',
     'email' : 'sai@gmail.com',
     'surname' : 'Rout'
 }
db2 = client['mongotest']
coll = db2['test']
coll.insert_one(d)