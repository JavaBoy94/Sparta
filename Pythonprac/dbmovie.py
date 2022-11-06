from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.k3kqx9z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# movie = db.movies.find_one({'title':'가버나움'})
# star = movie['star']
#
# movie = list(db.movies.find({'star':star},{'_id':False}))
# for m in movie:
#     print(m['title'])

db.movies.update_one({'title': '가버나움'}, {'$set': {'star': '0'}})