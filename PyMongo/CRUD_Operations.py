# -*- coding: utf-8 -*-


import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = client['EmployeeDB']

collection = mydb.mycollection

records = [{'name':'Charlie','gender':'M','age':28},
           {'name':'Harry','gender':'M','age':20},
           {'name':'Emma','gender':'F','age':27}  ]


collection.insert_many(records)

record = {'name':'Natasha','gender':'F','age':32}
collection.insert_one(record)


collection.find_one()


collection.find_one({'name':'Emma'})
# print all the records
for rec in collection.find():
    print(rec)

# print record - where condition
for record in collection.find({'gender':'M'}):
    print(record)
    
for record in collection.find({'gender':'F'}):
    print(record)

# "$in" operator
for record in collection.find({'age':{'$in':[20,28]}}):
    print(record)

# "$gt" -- greater than
for record in collection.find({'gender':'M','age':{'$gt':20}}):
    print(record)


# "$lt" -- less than
for record in collection.find({'gender':'F','age':{'$lt':32}}):
    print(record)

# "$and" -- and operator
for record in collection.find({"$and":[{'gender':'F'},{'age':27}]}):
    print(record)
    
    
collection.find_one({"$and":[{'gender':'F'},{'age':27}]})
   # print(record)

# "$or" -- or operator
for record in collection.find({'$or':[{'gender':'F'},{'age':28}]}):
    print(record)

mydb2 = client['pawandb']

records = mydb2.thedata

for record in records.find():
    print(record)

records.insert_one({'name':'Python','type':'Full Stack','videos':34,'active':True})


# Update -- update one
records.update_one({'type':'Back End'},{'$set':{'active':True}})

# Update -- update many
records.update_many({'type':'Back End'},{'$set':{'active':False}})

# Update -- update many
records.update_many({'type':'Back End'},{'$set':{'active':False}})


# Update -- update many
records.update_many({'type':'Back End'},{'$set':{'active':False}})

# Replace   --replace_one
records.replace_one({'name':'Python'},{'name':'Hello Python','type':"I don't Know",'videos':0,'active':False})

# Replace   --replace_one
records.replace_one({'name':'Hello Python'},{'name': 'Python', 'type': 'Full Stack', 'videos': 34, 'active': True})








             


