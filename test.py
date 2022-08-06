import  pymongo


client = pymongo.MongoClient("mongodb://sai1118:Sai1234@ac-hfsjren-shard-00-00.d8m7g8f.mongodb.net:27017,ac-hfsjren-shard-00-01.d8m7g8f.mongodb.net:27017,ac-hfsjren-shard-00-02.d8m7g8f.mongodb.net:27017/?ssl=true&replicaSet=atlas-z7p8m3-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

data = {
    'name' : 'Sai',
    'applying for' : 'Data Science'
}

list_of_records = [
    {
        'Sai' : 'Software Engineer',
        'Home' : 'Jajpur',
        'Location' : 'Bangalore'
    },
    {
        'Pragati' : 'Learning Coordinator',
        'Home' : 'Jajpur',
        'Location' : 'Bangalore'
    }
]

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]


database = client['inventory']
collection = database['table1']
collection.insert_many(data)

d = collection.find()

#collection.update_one({'item': 'canvas'}, {'$set':{'item' : 'Sai'}})

collection.delete_one({'item' : 'Sai'})

for i in d:
    print(i)