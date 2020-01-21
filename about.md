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
