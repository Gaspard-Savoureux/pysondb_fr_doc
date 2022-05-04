<h1 align="center"> <i><b> ~ PysonDB ~ </i></b></h1>

Je recommande de consulter la documentation officielle de [PysonDB](https://pysondb.github.io/pysonDB/) pour plus d'informations

###Installation
```
pip install pysondb
```
###Explication

Vous devez import le module pysondb.
```py
from pysondb import db
```

Vous pouvez initialiser/utiliser une collection avec cette commande:
```py
collection = db.getDb("collection.json")
```

Mais pour maintenir un environnement de travail propre je vous recommande d'utiliser:
```py
collection = db.getDb("db/collection.json")
```
>Puisque vous pouvez spécifier l'emplacement de vos collections, placé celles-ci dans un répertoire nommé "db".

Avec PysonDB vous pouvez ajoutez, retirez et modifier des éléments d'une collection.
>Notez que les collections doivents avec la même structure pour chacune 

####add
1. (**add**)
>Pour n'ajouter qu'une entrée.

```py
from pysondb import db
fruits = db.getDb("db/fruits.json")

fruits.add({"nom": "banane", "quantite": 200})
```

Vous pouvez vérifier le résultat avec ```cat db/fruits.json```.
Le résultat devrais ressembler à:
```json
{
   "data": [
      {
         "nom": "banane",
         "quantite": 200,
         "id": 263630127782736946
      }
   ]
}  
```

2. (**addMany**)
>Pour ajouter plusieurs entrées.
```py
from pysondb import db
employes = db.getDb("db/employes.json")

listEmploye = [
  {"nom": "Griffin", "prenom": "Peter"},
  {"nom": "Tyson", "prenom": "Michael"}
]

employes.addMany(listEmploye)
```

Vous pouvez vérifier le résultat avec ```cat db/employes.json```.
Le résultat devrais ressembler à:
```json
{
   "data": [
      {
         "nom": "Griffin",
         "prenom": "Peter",
         "id": 233282938750188381
      },
      {
         "nom": "Tyson",
         "prenom": "Michael",
         "id": 170907046911304967
      }
   ]
}
```
###get
1. (**get**):
>Pour retourner des données selon une quantitées données.

"get" ne reçois qu'un nombre entier comme paramètre. Il va renvoyer le nombre d'entré correspond au nombre donné.
```py
from pysondb import db
legumes = db.getDb("db/legumes.json")

listLegumes = [
  {"nom": "Concombre", "quantite": 200},
  {"nom": "Carrote", "quantite": 450}
]
legumes.addMany(listLegumes)
print('Paramètre  "1" donné', 'donc 1 entrée retournée \n ', legumes.get(1))
print('Paramètre  "2" donné ', 'donc 2 entrées retournées \n ', legumes.get(2))

```

Le résultat devrais ressembler à:
```
Paramètre  "1" donné donc 1 entrée retournée 
  [{'nom': 'Concombre', 'quantite': 200, 'id': 105077249742359822}]

Paramètre  "2" donné  donc 2 entrées retournées 
  [{'nom': 'Concombre', 'quantite': 200, 'id': 105077249742359822}, {'nom': 'Carrote', 'quantite': 450, 'id': 222315305243374514}]
```


1. (**getAll**)
>Pour retourner toutes les données.

3. **getByQuery**
>Pour obtenir de l'information selon un query donné.

"getByQuery" prend une query en paramètre qui un dictionnaire.
```py
from pysondb import db
magasins = db.getDb("db/magasins.json")

listmagasins = [
  {"nom": "Zellers", "Revenu annuel": "4,50$"},
  {"nom": "Walmart", "Revenu annuel": "100 000 000,50$"}
]
magasins.addMany(listmagasins)

result = magasins.getByQuery({"nom": "Zellers"})
print(result)
```

Le résultat devrais ressembler à:
```
[{'nom': 'Zellers', 'Revenu annuel': '4,50$', 'id': 324360928033120689}]
```

4. **getById**
>Pour obtenir de l'information selon un id donné.

"getById" prend un id en paramètre. 
>Noter que la fonction "add" renvoie le id de l'objet créé.
```py
from pysondb import db
individus = db.getDb("db/individus.json")

Id = individus.add({"nom complet": "Jean Melon", "profession": "Chômeur professionnel"})

result = individus.getById(Id)
print(result)
```

Le résultat devrais ressembler à:
```json
{'nom complet': 'Jean Melon', 'profession': 'Chômeur professionnel', 'id': 120322390294107486}
```

###delete

1. (**deleteAll**):
>Supprime toute les données d'une collection

"deleteAll" ne reçois aucun paramètre.
```py
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

```

Le résultat devrais ressembler à:
```
Avant suppréssion [{'nom': 'Métro', 'id': 130582309847042969}, {'nom': 'IGA', 'id': 837426113146777563}] 

Après suppréssion []
```


2. **deleteById**
>Pour supprimer une données selon un id donné.

"deleteById" prend un id en paramètre. 
>Noter que la fonction "add" renvoie le id de l'objet créé.
```py
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
```

Le résultat devrais ressembler à:
```
Avant suppréssion [{'nom': 'Métro', 'id': 258641293871288784}, {'nom': 'IGA', 'id': 139060333880566143}] 

Après suppréssion [{'nom': 'IGA', 'id': 139060333880566143}]
```

###update
1. (**updateById**):
>mets à jour une données selon son id.

"updateById(id, updated_data)" prend le id comme premier paramètre puis les champs à mettres à jour.
```py
from pysondb import db
composantes = db.getDb("db/composantes.json")
Id = composantes.add({"nom": "moteur", "quantity": 3})

print('Avant modification', composantes.getAll(), '\n')
composantes.updateById(Id, {"quantity": 5})
print('Après modification', composantes.getAll())
```

Le résultat devrais ressembler à:
```
Avant modification [{'nom': 'moteur', 'quantity': 3, 'id': 500696906555751634}] 

Après modification [{'nom': 'moteur', 'quantity': 5, 'id': 500696906555751634}]
```

2. (**updateByQuery**):
>mets à jour une données selon un query.

"updateById(researched_query, updated_data)" prend le id comme premier paramètre puis les champs à mettres à jour.
```py
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
```

Le résultat devrais ressembler à:
```
Avant modification [{'nom': 'Jake', 'groupe_sangin': 'O', 'donneur_universel': False, 'id': 782468395956862705}, {'nom': 'Jyll', 'groupe_sangin': 'O', 'donneur_universel': False, 'id': 331099113709518726}] 

Après modification [{'nom': 'Jake', 'groupe_sangin': 'O', 'donneur_universel': True, 'id': 782468395956862705}, {'nom': 'Jyll', 'groupe_sangin': 'O', 'donneur_universel': True, 'id': 331099113709518726}]
```