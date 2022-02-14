## Animation-dynamique-et-cartographie-sur-le-web

### Indications

— L’objectif de ce projet est de procéder à la réalisation de cartes dynamque à l’aide de librairies Python telle que Folium ou similaire, distribuable via des pages web et autorisant une interaction avec l’utilisateur.

— Il s’agit dans cette évaluation de revoir les savoir-faire étudiés en cours ou montrer votre aptitude
à mettre en œuvre des cartes selon trois directions principales : la mise en valeur d’entités ou
d’objets géométriques géographiques à l’aide d’éléments visuels, en utilisant différents markers
avec toolTip ; coupler ces informations à des plugins d’interactivité (widgets) ; d’afficher le
rendu des cartes et de réaliser au moins une animation pilotable par l’utilisateur sur les thèmes
proposés.

— La gestion des données utilisées pour les exercices fait partie intégrante du travail, l’illustration
et la documentation de la préparation des données sera évaluée de manière favorable, si de
surcroît elle apporte un enrichissement au sujet.

— Le rendu des codes prendra la forme d’un code Python que l’on aura développé préférentielle
avec une IDE.

— L’étude de la distribution de la solution via Internet sera un plus (via une conteneurisation
type Docker)

[Référence à la programmation Python](https://docs.python.org/fr/3.5/tutorial/)

[Référence à la programmation Python avec Folium](https://python-visualization.github.io/folium)

Mots-clés : folium, geojson, pandas geopandas, cartes Choropleth, plugins folium, informations
quantitatives sur une région.

### 1. Réalisation de carte interactive afin de visualiser des informations
régionales, acquisition des données et production de jeu de don-
nées à l’aide de geopandas
Il s’agit dans l’exercice suivant de manipuler la librairie geopandas et produire des jeux de données
nouveaux assemblés pour permettre une visualisation en utilisant différentes couches et les plugins
(widgets) de visualisation. On pourra visualiser par exemple les données socio-économiques relatives à
l’eau dans les pays du Mékong, ou encore l’utilisation des sols, tout en affichant des données ponctuelles
(points), de limites (lignes), ou régionales (polygones).
Réaliser une carte interactive où l’on peut examiner les caractéristiques de la zone couverte ac-
tuellement par le Vietnam, Cambodge, Laos (fichiers de données à recueillir sur les pays avec les liens
suivants Vietnam Cambodge Laos ).
Pour cela vous proposerez plusieurs couches (layers) contrôlables avec un plugin d’interaction, un
utilisateur pourra choisir de visualiser différentes source de données.

1. Pour chaque pays, sélectionner des fichiers de données, regroupant la localisation des villes
principales (type données = Point), des découpages administratifs en régions ou provinces
(type données = Polygone), et fleuves et réseaux routiers (type données = LineString ) aux
divers formats que vous trouverez. Compléter avec des informations quantitatives.

2. avec geopandas et ses méthodes, relire les données et les manipuler conjointement dans un
programme Python. Opérer des jointures de dataframes afin d’obtenir des données regroupées
par type de géométrie pour les 3 pays réunis. Exporter vos jeux de données et sauvegarder les
dans les formats usuels utiles.

3. Réaliser des cartes interteractives avec folium permettant de mettre en avant des informations
caractéristiques de la région. Pour cela vous proposerez plusieurs couches (layers) contrôlables
avec un plugin d’interaction, un utilisateur pourra choisir de visualiser le dessin des frontières
administratives, les réseaux routiers ou fluviaux, ou les villes et leur coordonnées, et de l’occu-
pation des sols .

### 2. Carte dynamique exploitant les données OpenStreetMap 
1. Avec votre binôme sélectionner une des neuf communes du territoire de Plaine Commune de
façon différenciée (chaque binôme traite une ville différente), et réaliser une carte interactive
des bâtiments publics présents sur la commune (il est nécessaire pour cela constituer un jeu de
données, vous pourrez fournir le code Python utile)

2. Réaliser une carte Folium interactive utilisant un plugin et permettant par exemple la mesure
des surfaces des toits.

3. Récupérer le réseau routier et calculer un plus courts chemins, par exemple de la mairie à une
équipement sportif (stade, gymnase, ou piscine) et l’afficher sur la carte.

4. Faire une carte interactive des réseaux que vous pourrez récupérer (réseau routier, réseau élec-
tricité, réseau eau ). Pour cela vous proposerez plusieurs couches (layers) contrôlables avec un
plugin d’interaction, un utilisateur pourra choisir de visualiser les différents réseaux.
