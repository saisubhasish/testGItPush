import pymongo

client = pymongo.MongoClient("mongodb+srv://sai1118:Sai1234@cluster0.d8m7g8f.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : 'Sai',
    "email" : 'sai@gmail.com',
    "surname" : 'Rout'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

d = {
    "name" : 'Sai',
    "email" : 'sai@gmail.com',
    "surname" : 'Rout',
    'friends' : ['Sid','Somu','Kanhu']
}

d = {
    "name" : 'Sai',
    "email" : 'sai@gmail.com',
    "surname" : 'Rout'
}

