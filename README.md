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

Le code de notre application backend se trouve dans le dossier `timeout_backend`. C'est ici qu'on y trouve les paramètres (`settings.py`), les pages de l'interface web (`urls.py`) et la vue principale (`views.py`).

Cette application appelle le module `events` qui inclut :
* le modèle Event (`models.py`)
* l'ajout de ce modèle à l'interface admin (`admin.py`)
* un serializer pour transformer le modèle en json (`serializers\event.py`)
* une vue de ce json (`views\event_list.py`)
* les urls associées au modèle ainsi qu'à cette vue (`urls.py`)

Après avoir modifié un modèle, ne pas oublier de lancer les commandes suivantes à la racine du dossier :

    $ python manage.py makemigrations
    $ python manage.py migrate
    
# Déploiement sur Heroku

    $ git push heroku master
