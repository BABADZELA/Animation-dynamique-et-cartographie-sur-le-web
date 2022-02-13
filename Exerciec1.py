import os
import geopandas as gpd
import pandas as pd
import folium
from folium import plugins
import json

# on a fabriqué une carte avec instantiation de la classe Map
fondCarte = folium.Map(
    location=[15.790, 108.239],
    tiles='',
    zoom_start=6,
)

# --------------------------------------------------------------------------------
# 1. Import des données
# ---------------------------------------------------------------------------------

# 1.1 Données du Cambodge
limiteAdminCambodge = gpd.read_file("./data/data_exo1/Cambodge.geojson")
districtsCambodge = gpd.read_file('./data/data_exo1/Cambodge_districts.geojson')
provincesCambodge = gpd.read_file('./data/data_exo1/Cambodge_provinces.geojson')
surfaceHydroCambodge = gpd.read_file('./data/data_exo1/Cambodge_surface_hydro.geojson')
routesCambodge = gpd.read_file('./data/data_exo1/Cambodge_routes.geojson')
waterLineCambodge = gpd.read_file('./data/data_exo1/Cambodge_water_lines.geojson')
communeCambodge = gpd.read_file('./data/data_exo1/Cambodge_communes.geojson')

# 1.2 Données du Laos
limiteAdminLaos = gpd.read_file("./data/data_exo1/Laos.geojson")
districtsLaos = gpd.read_file('./data/data_exo1/Laos_districts.geojson')
provincesLaos = gpd.read_file('./data/data_exo1/Laos_provinces.geojson')
surfaceHydroLaos = gpd.read_file('./data/data_exo1/Laos_surface_hydro.geojson')
routesLaos = gpd.read_file('./data/data_exo1/Laos_routes.geojson')
waterLineLaos = gpd.read_file('./data/data_exo1/Laos_water_lines.geojson')
communeLaos = gpd.read_file('./data/data_exo1/Laos_communes.geojson')

# 1.3 Données du Vietnam
limiteAdminVietnam = gpd.read_file("./data/data_exo1/Vietnam.geojson")
districtsVietnam = gpd.read_file('./data/data_exo1/Vietnam_district.geojson')
provincesVietnam = gpd.read_file('./data/data_exo1/Vietnam_provinces.geojson')
surfaceHydroVietnam = gpd.read_file('./data/data_exo1/Vietnam_surface_hydro.geojson')
routesVietnam = gpd.read_file('./data/data_exo1/Vietnam_routes.geojson')
waterLineVietnam = gpd.read_file('./data/data_exo1/Vietnam_water_lines.geojson')
communeVietnam = gpd.read_file('./data/data_exo1/Vietnam_communes.geojson')

# --------------------------------------------------------------------------------
# 2. Jointures des données afin d'obtenir des données regroupées par type de géométrie
# pour les 3 pays réunis
# ---------------------------------------------------------------------------------

limiteAdmin = gpd.GeoDataFrame(pd.concat([limiteAdminCambodge, limiteAdminLaos, limiteAdminVietnam],
                                         ignore_index=True), crs=limiteAdminCambodge.crs)

district = gpd.GeoDataFrame(pd.concat([districtsVietnam, districtsLaos, districtsCambodge],
                                      ignore_index=True), crs=districtsCambodge.crs)
province = gpd.GeoDataFrame(pd.concat([provincesVietnam, provincesLaos, provincesCambodge],
                                      ignore_index=True), crs=provincesCambodge.crs)

surfaceHydro = gpd.GeoDataFrame(pd.concat([surfaceHydroVietnam, surfaceHydroLaos, surfaceHydroCambodge],
                                          ignore_index=True), crs=surfaceHydroCambodge.crs)
route = gpd.GeoDataFrame(pd.concat([routesLaos, routesVietnam, routesCambodge],
                                   ignore_index=True), crs=routesCambodge.crs)
waterLine = gpd.GeoDataFrame(pd.concat([waterLineVietnam, waterLineLaos, waterLineCambodge],
                                       ignore_index=True), crs=waterLineCambodge.crs)
commune = gpd.GeoDataFrame(pd.concat([communeVietnam, communeLaos, communeCambodge],
                                     ignore_index=True), crs=communeCambodge.crs)

# 2.1 Export des données au format GeoJson
# commune.to_file("./output", driver="GeoJSON")

# ---------Création des variables contanant les fonds cartos------------------
cartodb = folium.TileLayer('cartodbpositron', name='Cartodb')
stamen = folium.TileLayer('Stamen Terrain', name='Stamen')

# on ajoute une couche à la carte
cartodb.add_to(fondCarte)
stamen.add_to(fondCarte)

# -------------------------------------------
limite_administrative = folium.GeoJson(
    limiteAdmin,
    style_function=lambda feature: {
        'fillColor': 'black',
        'color': 'NA',
        'weight': 1,
        'dashArray': '2'
    },
    name="limite administrative",
)

districts = folium.GeoJson(
    district,
    style_function=lambda feature: {
        'fillColor': 'NA',
        'color': 'black',
        'weight': 0.2,
        'dashArray': '2'
    },
    name="District",
)

provinces = folium.GeoJson(
    province,
    style_function=lambda feature: {
        'fillColor': 'NA',
        'color': 'black',
        'weight': 0.5,
        'dashArray': '2'
    },
    name="Province",
)

surfaceHydros = folium.GeoJson(
    surfaceHydro,
    style_function=lambda feature: {
        'fillColor': 'blue',
        'color': 'blue',
        'weight': 0.5,
    },
    name="Surface hydrographique",
)

routes = folium.GeoJson(
    route,
    style_function=lambda feature: {
        'color': 'gray',
        'weight': 0.8,
        'dashArray': '2'
    },
    name="Route",
)

waterLines = folium.GeoJson(
    waterLine,
    style_function=lambda feature: {
        'color': 'blue',
        'weight': 0.5,
        'dashArray': '2'
    },
    name="WaterLine",
)

# ajout des limites administratives des états à la carte
limite_administrative.add_to(fondCarte)
districts.add_to(fondCarte)
provinces.add_to(fondCarte)
routes.add_to(fondCarte)
surfaceHydros.add_to(fondCarte)
waterLines.add_to(fondCarte)
# markerCluster.add_to(fondCarte)

# -----------------------------------------------------------------------------------------
# Ajout de quelques fonctionnalités à  la carte
# -----------------------------------------------------------------------------------------

# controleur des couches
lc = folium.LayerControl(position='topright')
lc.add_to(fondCarte)

# zoom plein écran
fullscreen = folium.plugins.Fullscreen(
    position='topleft',
)
fullscreen.add_to(fondCarte)

# position de la souris
mousePosition = folium.plugins.MousePosition(position='bottomright', separator=' : ', empty_string='Invalide',
                                             lng_first=False, num_digits=5, prefix='',
                                             lat_formatter=None, lng_formatter=None)
mousePosition.add_to(fondCarte)

# export de la carte sous le format html
fondCarte.save("./result/carde_des_informations_regionales.html")
