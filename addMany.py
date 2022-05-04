from pysondb import db
employes = db.getDb("db/employes.json")

listEmploye = [
  {"nom": "Griffin", "prenom": "Peter"},
  {"nom": "Tyson", "prenom": "Michael"}
]

employes.addMany(listEmploye)