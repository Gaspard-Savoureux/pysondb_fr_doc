from pysondb import db
composantes = db.getDb("db/composantes.json")

Id = composantes.add({"nom": "moteur", "quantity": 3})
print('Avant suppréssion', composantes.getAll(), '\n')
composantes.updateById(Id, {"quantity": 5})
print('Après suppréssion', composantes.getAll())