"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 06
Numéro d'équipe :  12
Noms et matricules : Koutou Andy Abdoul Mouhaimine (2390725), Frédéric Michaud (2393155)
"""
import csv
from datetime import datetime

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
csvfile=open("collection_bibliotheque.csv", "r")
data=csv.reader(csvfile)
library={}
for line in data:
    library[line[3]]={"titre":line[0], "auteur":line[1], "date_publication":line[2]}
csvfile.close()
for key in library:
    print(key, library[key])
print("\n")

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
csvfile=open("nouvelle_collection.csv", "r")
data=csv.reader(csvfile)
new_collection={}
for line in data:
    new_collection[line[3]]={"titre":line[0], "auteur":line[1], "date_publication":line[2]}
csvfile.close()

for key,data in new_collection.items():
    if  key in library:
        print(f"Le livre {key} ---- {data['titre']} par {data['auteur']} ---- est déjà présent dans la bibliothèque")
    else:
        library[key]=data
        print(f"Le livre {key} ---- {data['titre']} par {data['auteur']} ---- a été ajouté avec succès")
print("\n")




########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
keys_to_delete={}
keys_to_add={}
for key,data in library.items():
    if data["auteur"] == "William Shakespeare":
        print(key, data)
        new_key="WS"+key[1:4]
        keys_to_add[new_key]=data
        keys_to_delete[key]=data
for key in keys_to_delete:
    del library[key]
for key,data in keys_to_add.items():
    library[key]=data

for key in library:
    print(key, library[key])      
print("\n")

        







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

csvfile = open("emprunts.csv", "r")
data = csv.reader(csvfile)
for line in data:
    cote = line[0]  
    date_emprunt = line[1]  

    if cote in library:
        library[cote]['emprunts'] = "emprunté"
        library[cote]['date_emprunt'] = date_emprunt
    else:
        print(f"Le livre avec la cote {cote} est disponible.")

csvfile.close()

print(f' \n Bibliotheque avec ajout des emprunts : \n {library} \n')
        

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 
frais_jour, frais_max = 2, 100
jour_si_perdu = 365

library['livres_retard'] = []
library['livres_perdus'] = []

ajd = datetime.now()

for key, cote in library.items():
    if 'date_emprunt' in cote:
        try:
            date_emprunt = datetime.strptime(cote['date_emprunt'], "%Y-%m-%d")
            days_borrowed = (ajd - date_emprunt).days

            if days_borrowed > 30:
                frais_retard = min((days_borrowed - 30) * frais_jour, frais_max)
                library['livres_retard'].append((key, frais_retard))

            if days_borrowed > 365:
                library['livres_perdus'].append(key)
        except ValueError as e:
            print(f"Error parsing date for {key}: {e}")

print(f' \n Bibliotheque avec ajout des retards et frais : {library} \n')




