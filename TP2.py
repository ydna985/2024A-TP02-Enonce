"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""
import csv
########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
csvfile=open("collection_bibliotheque.csv", "r")
data=csv.reader(csvfile)
library={}
for line in data:
    library[line[3]]={"title":line[0], "author":line[1], "publication date":line[2]}
csvfile.close()
for key in library:
    print(key, library[key])
print("\n")
#print(f' \n Bibliotheque initiale : {library} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
csvfile=open("nouvelle_collection.csv", "r")
data=csv.reader(csvfile)
new_collection={}
for line in data:
    new_collection[line[3]]={"title":line[0], "author":line[1], "publication date":line[2]}
csvfile.close()

for key,data in new_collection.items():
    if  key in library:
        print(f"Le livre {key} ---- {data["title"]} par {data["author"]} ---- est déjà présent dans la bibliothèque")
    else:
        library[key]=data
        print(f"Le livre {key} ---- {data["title"]} par {data["author"]} ---- a été ajouté avec succès")
print("\n")




########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
keys_to_delete={}
keys_to_add={}
for key,data in library.items():
    if data["author"] == "William Shakespeare":
        print(key, data)
        new_key="WS"+key[1:4]
        keys_to_add[new_key]=data
        keys_to_delete[key]=data
for key in keys_to_delete:
    del library[key]
for key,data in keys_to_add.items():
    library[key]=data

for key in library:
    if "WS" in key:
        print(key, library[key])
print("\n")
#print(f' \n Bibliotheque avec modifications de cote : {library} \n')

        







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






