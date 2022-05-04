from pysondb import db
magasins = db.getDb("db/magasins.json")

listmagasins = [
  {"nom": "Zellers", "Revenu annuel": "4,50$"},
  {"nom": "Walmart", "Revenu annuel": "100 000 000,50$"}
]
magasins.addMany(listmagasins)

result = magasins.getByQuery({"nom": "Zellers"})
print(result)