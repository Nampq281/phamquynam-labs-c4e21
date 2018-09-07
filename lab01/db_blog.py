from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb://quynph13:db8pawrf@ds237922.mlab.com:37922/c4e21nam"

client = MongoClient(uri)
db = client.get_default_database()

posts = db["post"]

post = {
    "title":"Lop moi",
    "content":"Update nhieu thong tin moi",
}

# posts.insert_one(post)
# print("done")

# cond = {
#     "title" : {
#         "$regex": "lop"
#         "$options": "i"
#     }
# }

post_list = posts.find(cond)
print(post)