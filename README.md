# Volcanic Eruption Patterns in the Americas

This Jupyter notebook presents a comprehensive analysis of volcanic eruption trends in Northern and Southern America. It explores regional and chronological distributions and investigates multiple geological and demographic factors affecting volcanic activity.

Regions analyzed include:
- **Northern America:** USA, Canada, Mexico  
- **Southern America:** Argentina, Chile, Chile-Argentina, Chile-Bolivia, Chile-Peru, Colombia, Colombia-Ecuador, Ecuador, Peru


## It includes:

- **Geospatial Visualization:** Interactive maps of volcano locations using Basemap.
- **Volcano Typology:** Pie charts by country showing dominant volcano types.
- **Eruption Frequency:** Bar charts by subregion.
- **Temporal Trends:** Scatter plots and histograms exploring elevation, eruption year, and population exposure.
- **Population Risk:** Box plots showing population proximity to volcanoes.
- **Correlation Analysis:** VEI (Volcanic Explosivity Index) vs. geographic location.

## Project Files:

- [Volcanic_Eruption_Analysis.ipynb] – The main notebook with full analysis and visuals.
- [volcano_analysis.py] – Utility functions for plotting and cleaning.
- [volcano_analysis_class.py] – Class-based methods for analysis.

## Data

This project uses raw volcanic data sourced from the Smithsonian Global Volcanism Program. The following CSV files are included in the repository:

- [GVP_Volcano_List_Northern_America.csv] – Volcano metadata for Northern America

- [GVP_Volcano_List_Southern_America.csv] – Volcano metadata for Southern America

- [GVP_Eruption_Results_Northern_America.csv] – Historical eruption data for Northern America

- [GVP_Eruption_Results_Southern_America.csv] – Historical eruption data for Southern America
  

## Key Insights:

Stratovolcanoes dominate both continents, particularly in the Andes and Cascade regions.

The Andes region in Southern America shows the highest eruption frequency over time.

Several volcanoes have populations exceeding 100,000+ within a 100 km radius.

Weak to moderate correlations between eruption explosivity (VEI) and geographic coordinates.
