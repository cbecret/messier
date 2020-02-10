# Projet Messier

Mise en place d'un catalogue de Messier dans le cadre du cours de Python du Mastère data à Hétic.

> Charles Messier, astronome français du XVIIIème siècle spécialiste des comètes a élaboré ce catalogue des objets diffus. En cherchant de nouvelles comètes dans le ciel, il était perturbé par de nombreuses taches laiteuses et diffuses. Afin de se débarasser de ces objets parasites, il décida de les lister ... Autrefois inconnus, ces objets diffus sont des galaxies, des nébuleuses planétaires, des amas globulaires ou des amas ouverts, tous visibles dans l'hémisphère nord. Aujourd'hui, ce catalogue de 110 objets fait autorité en France parmi la communauté des astronomes amateurs. Dans le catalogue Messier, vous trouverez les coordonnées ainsi que les principales caractéristiques de ces objets.

Source [astropolis.fr](https://www.astropolis.fr/catalogue-Messier/page-de-garde/astronomie-accueil-catalogue-Messier.html)

## Instructions d'installation :

* Cette API utilise les dépendances suivantes :

| Dépendance | Versions |
| ------ | ------ |
| Python | (3.5, 3.6, 3.7, 3.8) |
| Django | (1.11, 2.0, 2.1, 2.2, 3.0) |
| djangorestframework | (3.11) |

* Procédure d'installation :

```sh
$ git clone https://github.com/cbecret/messier.git
$ cd messier
$ python manage.py migrate
$ python manage.py runserver
```

## Contraintes d'accessibilité :

- Performance
- Flexibilité et facilité de recherche/exploitation
- Complétude des données
- Recoupement avec d'autres sources
- Entièrement en Python
- Hébergé sur un service en ligne

### Participants
* Cyril Bécret
* Quentin Monmousseau
* Mehdi Bey

### Données
- Messier number
- Usual Name
- NGC number
- Constellation
- Object type
- Dimension
- Earth distance
- Magnitude
- Right ascension
- Discovery date
- Discoverer
- Image link

### L'intérêt scientifique de ces données et de votre catalogue
- Faciliter l'exploration des différentes galaxies listées par Messier

### Fonctionnalités minimales
- Versioning de l'API
- Accès au tableau complet des données
- Fonction de récupération des données au format indiqué par l'utilisateur (json, api...)

### Technologies utilisées
* [Python] - Langage utilisé pour la création de l'API
* [Django] - Framework permettant la création de l'API
* [Sqlite3] - Base de données relationnelle

#### Prochaines évolutions :
* [JavaScript] - Utilisé pour l'affichage du FrontEnd (Librairies à définir en fonction de la motivation (ThreeJS)

## Request & Response Examples

### API Resources

  - [GET /api/v1](#api-root)
  - [GET /api/v1/objects](#get-objects)
  - [GET /api/v1/objects/{id}](#get-objectsid)
  - [POST /api/v1/objects](#post-objects)


### API root

Example: https://cbecret.pythonanywhere.com/api/v1/

Response body:
```
{
    "mobjects": "https://cbecret.pythonanywhere.com/api/v1/mobjects/",
    "users": "https://cbecret.pythonanywhere.com/api/v1/users/"
}
```


### GET /objects

Example: https://cbecret.pythonanywhere.com/api/v1/objects.json

Response body:
```

[
    {
        "id": 1,
        "messier_number": "M1",
        "usual_name": "",
        "ngc": "NGC 1952",
        "constellation": "Taurus",
        "messier_type": "Supernova remnant",
        "dimension": "6'×4'",
        "distance_value": 6.3,
        "distance_unit": "kly",
        "magnitude": 8.4,
        "ascension": "05h 34m 31.94s",
        "discovery_date": "1731-05-01",
        "discoverer": "John Bevis",
        "image_link": "https://en.wikipedia.org/wiki/Messier_object#/media/File:Crab_Nebula.jpg",
        "owner": 1
    },
    {
        "id": 2,
        "messier_number": "M1",
        "usual_name": "",
        "ngc": "NGC 1952",
        "constellation": "Taurus",
        "messier_type": "Supernova remnant",
        "dimension": "6'×4'",
        "distance_value": 6.3,
        "distance_unit": "kly",
        "magnitude": 8.4,
        "ascension": "05h 34m 31.94s",
        "discovery_date": "1731-05-01",
        "discoverer": "John Bevis",
        "image_link": "https://en.wikipedia.org/wiki/Messier_object#/media/File:Crab_Nebula.jpg",
        "owner": 1
    }
]
```

### GET /objects/{id}

Example: https://cbecret.pythonanywhere.com/api/v1/objects/1.json

Response body:
```
{
    "id": 1,
    "messier_number": "M1",
    "usual_name": "",
    "ngc": "NGC 1952",
    "constellation": "Taurus",
    "messier_type": "Supernova remnant",
    "dimension": "6'×4'",
    "distance_value": 6.3,
    "distance_unit": "kly",
    "magnitude": 8.4,
    "ascension": "05h 34m 31.94s",
    "discovery_date": "1731-05-01",
    "discoverer": "John Bevis",
    "image_link": "https://en.wikipedia.org/wiki/Messier_object#/media/File:Crab_Nebula.jpg",
    "owner": 1
}
```

## Format des données renvoyées par l'API

* Il est possible de choisir le type de retour via le **Accept header** :

http http://127.0.0.1:8000/api/v1/objects/ Accept:application/json  # Request JSON
http http://127.0.0.1:8000/api/v1/objects/ Accept:text/html         # Request HTML

* ou en utilisant un suffix spécifique :

http http://127.0.0.1:8000/api/v1/objects.json  # JSON suffix
http http://127.0.0.1:8000/api/v1/objects.api   # Browsable API suffix


### Status Codes

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

## Liens annexes de données
* [HyperLeda](http://leda.univ-lyon1.fr/)
* [CDS Portal](http://cdsportal.u-strasbg.fr/)


### Todos

> __TODO :__ Développer un petit front sexy avec du THREE.js ¯_(ツ)_/¯


License
----

MIT
