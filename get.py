from pysondb import db
legumes = db.getDb("db/legumes.json")

listLegumes = [
  {"nom": "Concombre", "quantite": 200},
  {"nom": "Carrote", "quantite": 450}
]
legumes.addMany(listLegumes)
print('Paramètre  "1" donné', 'donc 1 entrée retournée \n ', legumes.get(1))
print('Paramètre  "2" donné ', 'donc 2 entrées retournées \n ', legumes.get(2))