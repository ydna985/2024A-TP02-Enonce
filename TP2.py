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
    library[line[3]]=line[:3]
csvfile.close()


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
csvfile=open("nouvelle_collection.csv", "r")
data=csv.reader(csvfile)
new_collection={}
for line in data:
    new_collection[line[3]]=line[:3]
csvfile.close()
for key,value in new_collection.items():
    is_inside=key in library
    if  (key in library) == False:
        library[key]=value
        print(f"Le livre {key} ---- {value[0]} par {value[1]} ---- a été ajouté avec succès")
    else:
        print(f"Le livre {key} ---- {value[0]} par {value[1]} ---- est déjà présent dans la bibliothèque")






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






