from pysondb import db
individus = db.getDb("db/individus.json")

Id = individus.add({"nom complet": "Jean Melon", "profession": "Chômeur professionnel"})

result = individus.getById(Id)
print(result)