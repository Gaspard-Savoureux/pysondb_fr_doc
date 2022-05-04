from pysondb import db
epiceries = db.getDb("db/epiceries.json")

listEpiceries = [
  {"nom": "Métro"},
  {"nom": "IGA"}
]

epiceries.addMany(listEpiceries)
print('Avant suppréssion', epiceries.getAll(), '\n')
epiceries.deleteAll()
print('Après suppréssion', epiceries.getAll())