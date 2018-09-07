from pymongo import MongoClient
from bson.objectid import ObjectId
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()

marketing = db["customers"]

events = 0
advertisement = 0
wordsofmouth = 0

for item in marketing:
    if item["ref"] == "events":
        events += 1
    elif item["ref"] == "ads":
        advertisement += 1
    elif item["ref"] == "wom":
        wordsofmouth += 1

print("events count: ", events)
print("ads count: ", advertisement)
print("wom count: ", wordsofmouth)


# # #draw chart
# reference = [events, advertisement, wordsofmouth]
# ref_type = ["events","advertisement", "words of mouth"]

# pyplot.pie(reference, labels=ref_type, autopct= "%.1f%%", )
# pyplot.title("Reference types")
# pyplot.axis("equal")

# pyplot.show()