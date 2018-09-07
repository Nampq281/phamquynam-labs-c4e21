from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db["posts"]

write = {
    "title":"Tất cả là tạm thời",
    "author": "NamPhamq",
    "content":"Tất cả đều không vĩnh hằng. Điều gì được sinh ra rồi thì cũng sẽ chết. Gặp mặt rồi cũng chia li. Được rồi cũng mất. Tạo dựng rồi cũng đổ vỡ. Thời gian trôi nhanh như một mũi tên. Tất cả đều phù du. Có điều gì trên thế gian này mà không phải tạm thời",
}

posts.insert_one(write)
print("done")
