# Projet3_DE
L’objectif de ce projet est de choisir, mettre en place, et peupler une base de données à partir d’un jeu de données de l’open data, et d’implémenter une API permettant de requêter cette base de données.

Le projet contient: 
* Une [api](https://github.com/bourrich90/Projet3_DE/blob/main/main/) développée avec le framework FastAPI.
* Une base de données [Mysql](https://dev.mysql.com/downloads/installer/).

## Jeu de données

Le jeu de données utilisée dans ce projet est [Football transfers](https://www.kaggle.com/vardan95ghazaryan/top-250-football-transfers-from-2000-to-2018) . Il s'agit des données des 250 plus cher transferts de joueurs de Football entre 2000 et 2008 .Le fichier csv contient les informations suivantes : Name, Position, Age, Team_from, League_from, Team_to, League_to ,Season , Market_value , Transfer_fee

## Choix d’une base de données

Le choix d'une bases de données relationnelle , dans notre cas Mysql est justifiée de fait que les données sont structurées et organisées. Une table avec un shéma fixe peut donc contenir les données  Football transfers sans probléme .

## API

Notre API est développée avec le framework FastAPI est dans le dossier [main](https://github.com/bourrich90/Projet3_DE/blob/main/main/) qui est composé des fichiers ci-dessous:

* [main.py](https://github.com/bourrich90/Projet3_DE/blob/main/main/main.py) : fichier principal, qui définit la route de l'insertion des données dans la base de données Mysql POST /insert_bdd_elemets et l'affichage des données depuis la base de données Mysql POST /show_bdd_elemets.
* [create_table.py](https://github.com/bourrich90/Projet3_DE/blob/main/main/Create_table.py) : permet la création de la table Football_Transfers dans Mysql
* [insert_data.py](https://github.com/bourrich90/Projet3_DE/blob/main/main/insert_data.py) : pemet de peupler la table Football_Transfers avec les données [Football transfers](https://www.kaggle.com/vardan95ghazaryan/top-250-football-transfers-from-2000-to-2018)
* [Football_Transfers_Class.py](https://github.com/bourrich90/Projet3_DE/blob/main/main/Football_Transfers_Class.py) : définit les modèles de données attendus en entrée de l'API.
* [requirements.txt](https://github.com/bourrich90/Projet3_DE/blob/main/main/requirements.txt) : dépendances Python.

La création de la table Football_Transfers et son chargement avec données est fait  au lancement de l'API avec les fonctions create_table() et insert_data().

Pour lancer l'API, exécutez les commandes suivantes :

* installer Mysql.
* Créer la base de données Football_Transfers.Pour ce faire , lancer la commande "create Football_Transfers" dans le terminal de Mysql , ensuite  excécuter 
"show databases" , vous devez avoir la vue suivante:

![image](https://user-images.githubusercontent.com/86717947/132197932-007e8c8f-c23f-4a19-a4c0-fe575aa73348.png)

* cd main
* pip install -r requirements.txt
* uvicorn main:app
 


L'API est désormais accessible à l'adresse localhost:8000.

En particulier, vous pouvez accéder à la documentation de l'API à l'adresse [localhost:8000/docs](http://localhost:8000/docs):

![image](https://user-images.githubusercontent.com/86717947/132199758-c45fc4f8-a919-4d50-91e6-3d0fa37da484.png)

