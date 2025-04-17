import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap

"""

volcano_analysis.py file contains a set of utility functions designed to assist with the analysis and visualization of volcanic data. These functions include loading and cleaning CSV data (load_and_clean_data), plotting maps of volcano locations (plot_volcano_map), generating pie charts for primary volcano types by country (plot_pie_chart_for_country), and creating bar charts for eruption frequency by subregion (plot_bar_chart). 

"""

def load_and_clean_data(csv_path, header=1):
   """
   Load and clean CSV data.

    Parameters:
    - csv_path (str): Path to the CSV file.
    - header (int): Row number to use as column names.

    Returns:
    - pandas.DataFrame: Cleaned DataFrame with NaN values dropped.

    """
    df = pd.read_csv(csv_path, header=header)
    cleaned_df = df.dropna()
    return cleaned_df

def plot_volcano_map(data, title, lon_col='Longitude', lat_col='Latitude'):
    """
    Plot a map of volcano locations.

    Parameters:
    - data (pandas.DataFrame): DataFrame containing the volcano data.
    - title (str): Title of the plot.
    - lon_col (str): Column name for longitude data.
    - lat_col (str): Column name for latitude data.
   
    """
    plt.figure(figsize=(12, 8))
    m = Basemap(projection='merc', llcrnrlat=5, urcrnrlat=75, llcrnrlon=-190, urcrnrlon=-50, resolution='i')
    m.drawcoastlines()
    m.drawcountries()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='lightgray', lake_color='aqua')
    m.drawmeridians(range(-180, 180, 10), labels=[1, 0, 0, 1], linewidth=0.2)
    m.drawparallels(range(-90, 90, 10), labels=[1, 0, 0, 1], linewidth=0.2)
    
    x, y = m(data[lon_col].astype(float).values, data[lat_col].astype(float).values)
    m.scatter(x, y, marker='o', color='red', zorder=5, alpha=0.7)
    
    plt.xlabel('Longitude', labelpad=35)
    plt.ylabel('Latitude', labelpad=35)
    plt.title(title)
    plt.show()

def plot_pie_chart_for_country(data, country_name):
    """
    Plot a pie chart of primary volcano types for a given country.

    Parameters:
    - data (pandas.DataFrame): DataFrame containing the volcano data.
    - country_name (str): Name of the country to filter data.
    
    """
    country_data = data[data['Country'] == country_name]
    volcano_types = country_data['Primary Volcano Type'].value_counts()
    volcano_types = volcano_types[volcano_types > 0]
    
    plt.figure(figsize=(8, 8))
    plt.pie(volcano_types, labels=volcano_types.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(volcano_types))))
    plt.title(f'Primary Volcano Types in {country_name}')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def plot_bar_chart(data, x_col, y_col, title, xlabel, ylabel):
    """
    Plot a bar chart for the given data.

    Parameters:
    - data (pandas.DataFrame): DataFrame containing the data.
    - x_col (str): Column name for x-axis data.
    - y_col (str): Column name for y-axis data.
    - title (str): Title of the plot.
    - xlabel (str): Label for the x-axis.
    - ylabel (str): Label for the y-axis.
   
    """
    plt.figure(figsize=(14, 10))
    sns.countplot(y=y_col, data=data, palette='viridis', order=data[y_col].value_counts().index)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
