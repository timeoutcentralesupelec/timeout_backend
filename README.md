# Projet TimeoutCentrale BAM

Le projet TimeOut CentraleSupélec est un projet d'option ISIA de 3ème année de l'année scolaire 2017-2018 en partenariat avec l'entreprise BAM.

Le projet a pour but de créer une application mobile récapitulant les évènements qui ont lieu sur le campus de l'école.

# Contributeurs

* Claire Clémot
* Maxime Allain
* Chloé Gobé
* BAM

# Structure du projet

Le projet est divisé en deux repositories, le back office admin en django est disponible sous le repository timeout_back et timeout-centrale est le repository de l'application mobile

# Rôles sur la plateforme

* Administrateur :
  * ajouter des événements pour le campus
  * modérer les événements rajoutés par d'autres associations
  * ajouter des associations
* Associations :
  * ajouter des événements associés à son association, qui seront modérés

# Requirements

* Installe Django `pip install django`

# Django

À la racine du dossier, lancer les commandes suivantes après avoir modifié un modèle :

    $ python manage.py makemigrations
    $ python manage.py migrate
    
# Déploiement sur Heroku

    $ git push heroku master
