from pysondb import db
epiceries = db.getDb("db/epiceries.json")


listEpiceries = [
  {"nom": "Métro"},
  {"nom": "IGA"}
]
epiceries.addMany(listEpiceries)

monEpicier = epiceries.getByQuery({"nom": "Métro"})

print('Avant suppréssion', epiceries.getAll(), '\n')
epiceries.deleteById(monEpicier[0]["id"])
print('Après suppréssion', epiceries.getAll())