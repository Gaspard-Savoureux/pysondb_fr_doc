from pysondb import db
siblings = db.getDb("db/siblings.json")

listeSiblings = [
  {"nom": "Jake", "groupe_sangin": "O", "donneur_universel": False},
  {"nom": "Jyll", "groupe_sangin": "O", "donneur_universel": False}
]
Id = siblings.addMany(listeSiblings)

print('Avant modification', siblings.getAll(), '\n')
siblings.updateByQuery(
  {"groupe_sangin": "O"},
  {"donneur_universel": True}
)
print('Après modification', siblings.getAll())