from pysondb import db
fruits = db.getDb("db/fruits.json")

fruits.add({"nom": "banane", "quantite": 200})