from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://petkovskibojan8891:f0y4QHEggv8ox8cB@cluster0.iiujb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["sample_mflix"]
collection = db["users"]
movies = db["movies"]
comments = db["comments"]

bojan_db = client["Bojan_DB"]
users = bojan_db["users"]

if not users.find_one({"name" : "Bojan", "e-mail" : "petkovski.bojan.8891@gmail.com", "phone" : "078 385 198"}):
    users.insert_one({"name": "Bojan", "e-mail": "petkovski.bojan.8891@gmail.com", "phone": "078 385 198"})
else:
    print("korisnikot veke e registriran")

korisnici = users.find({"name" : "Bojan"})
for korisnik in korisnici:
    print(korisnik)

naslovi_na_filmovi = movies.find({}, {"title": 1, "_id" : 0})
for naslov in naslovi_na_filmovi:
    print(f"naslov: {naslov}")

komentari = comments.find({"name" : "Lisa"})
for comment in komentari:
    print(f"komentar: {comment}")

print(f"movies: {movies.title}")
print(f"find_one primer: {collection.find_one()}")
print(f"find_one(params) primer: {collection.find_one({"name":"Khal Drogo"})}")




