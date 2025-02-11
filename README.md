# Dashboard Spotify avec Power BI  

## Présentation  
Dashboard interactif et visuellement attrayant créé avec Power BI, basé sur les données Spotify. L'objectif était de transformer des données brutes en visualisations claires et engageantes, permettant d'explorer les tendances et performances des morceaux et des artistes.  

---

## Fonctionnalités  
- **Sources de données** :  
  - Jeu de données provenant de [Kaggle](https://www.kaggle.com/) contenant des informations sur les morceaux et leurs performances.  
  - Intégration avec l'API de Spotify via Python pour récupérer dynamiquement les images des artistes.  

- **Points forts** :  
  - Analyse détaillée des morceaux, incluant les streams, niveaux d'énergie et tendances de sortie.  
  - Calendrier dynamique affichant l'activité des streams par jour.  
  - Visualisations personnalisées, incluant des graphiques en barres, des courbes et un diagramme en anneau illustrant les niveaux d'énergie.  

- **Techniques avancées** :  
  - Utilisation de HTML et CSS pour des éléments visuels uniques dans Power BI.  
  - Utilisation de Dened pour créer des visualisations avancées avec des configurations JSON.  

---

## Installation  
### Étape 1 : Cloner le dépôt  
```bash  
git clone https://github.com/mawed22/dashboard-spotify.git  
cd dashboard-spotify

### Étape 2 : Installer les dépendances Python 
```bash  
pip install requests pandas spotipy  

### Étape 3 : Exécuter le script API 
```bash  
python api_integration.py  

### Étape 4 : Charger le fichier Power BI 
- **Ouvrez le fichier SpotifyDashboard.pbix dans Power BI Desktop pour explorer le dashboard** 
