# Projet Messier

Mise en place d'un catalogue de Messier dans le cadre du cours de Python du Mastère data à Hétic.

> Charles Messier, astronome français du XVIIIème siècle spécialiste des comètes a élaboré ce catalogue des objets diffus. En cherchant de nouvelles comètes dans le ciel, il était perturbé par de nombreuses taches laiteuses et diffuses. Afin de se débarasser de ces objets parasites, il décida de les lister ... Autrefois inconnus, ces objets diffus sont des galaxies, des nébuleuses planétaires, des amas globulaires ou des amas ouverts, tous visibles dans l'hémisphère nord. Aujourd'hui, ce catalogue de 110 objets fait autorité en France parmi la communauté des astronomes amateurs. Dans le catalogue Messier, vous trouverez les coordonnées ainsi que les principales caractéristiques de ces objets.

Source [astropolis.fr](https://www.astropolis.fr/catalogue-Messier/page-de-garde/astronomie-accueil-catalogue-Messier.html)

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
- Name
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
- Facilité l'exploration des différentes galaxies listées par Messier

### Fonctionnalités minimales
- Versioning de l'API
- Fonction de recherche libre
- Accès au tableau complet des données
- Fonction de tri pour chaque colonne
- Fonction de récupération des données au format indiqué par l'utilisateur (json, csv...)
- Fonction permettant de générer des graphiques à partir de deux dimensions choisies par l'utilisateur

### Technologies utilisées
* [Python] - Langage utilisé pour la création de l'API
* [Django] - Framework permettant la création de l'API
* [PostgreSQL] - Base de données relationnelle
* [MS Azure] - Utilisé pour déployé le code en serverless et hébergement du front
* [JavaScript] - Utilisé pour l'affichage du FrontEnd (Librairies à définir en fonction de la motivation (ThreeJS)

## Request & Response Examples

### API Resources

  - [GET /api/v1/objects](#get-objects)
  - [GET /api/v1/objects/{id}](#get-objectsid)
  - [GET /api/v1/objects/{id}/{parameter}](#get-objectsidparameter)
  - [POST /api/v1](#post-objects)

### GET /objects

Example: http://example.gov/api/v1/objects.json

Response body:
```
{
    "results": [
        {
            "id": "1",
            "messier_number": "M1",
            "name": "Crab Nebula",
            "ngc": "NGC 1952",
            "constellation": "Taurus",
            "type": "Supernova remnant",
            "dimension": "6'×4'",
            "distance": {
                "value": "6.3",
                "unit": "kly"
            },
            "magnitude": "8.4",
            "ascension": "05h 34m 31.94s",
            "discovery_date": "03/05/1731",
            "discoverer": "John Bevis",
            "image_link": "https://en.wikipedia.org/wiki/Messier_object#/media/File:Crab_Nebula.jpg"
        },
        {
            "id": "2",
            "messier_number": "M2",
            "name": None,
            "ngc": "NGC 7089",
            "constellation": "Aquarius",
            "type": "Globular cluster",
            "dimension": "16′.0",
            "distance": {
                "value": "33",
                "unit": "kly"
            },
            "magnitude": "6.3",
            "ascension": "21h 33m 27.02s",
            "discovery_date": "03/05/1731",
            "discoverer": "John Bevis",
            "image_link": "https://en.wikipedia.org/wiki/Messier_object#/media/File:Messier_2_Hubble_WikiSky.jpg"
        },
    ]
}
```

### GET /objects/{id}

Example: http://example.gov/api/v1/objects/1.json

Response body:
```
{
    "result": {
        "id": "1",
        "messier_number": "M1",
        "name": "Crab Nebula",
        "ngc": "NGC 1952",
        "constellation": "Taurus",
        "type": "Supernova remnant",
        "dimension": "6'×4'",
        "distance": {
            "value": "6.3",
            "unit": "kly"
        },
        "magnitude": "8.4",
        "ascension": "05h 34m 31.94s",
        "discovery_date": "03/05/1731",
        "discoverer": "John Bevis",
        "image_link": "https://en.wikipedia.org/wiki/Messier_object#/media/File:Crab_Nebula.jpg"
    }
}
```

### GET /objects/{id}/{parameter}

Example: http://example.gov/api/v1/objects/1/name.json

Response body:
```
{
    "result": {
        "name": "Crab Nebula"
    }
}
```


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

### Installation

> __TODO :__ Compléter les instructions d'installation et de déploiement

### Todos

 - Compléter le fichier about.md
 - Documenter les routes utilisées
 - Initialiser Django Rest Framework
 - Mettre en place l'infrastructure Azure
 - Développer les Az function requises
 - Mettre en place un FrontEnd ludique et interactif

License
----

MIT
