import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap
from volcano_analysis import load_and_clean_data, plot_volcano_map, plot_pie_chart_for_country, plot_bar_chart

"""

volcano_analysis_class.py file defines the VolcanoAnalysis class for loading, cleaning, and visualizing volcanic data using methods encapsulated in a class. This class provides methods to display the initial rows of the dataset (show_head), map volcano locations (map_volcano_locations), plot pie charts of volcano types by country (plot_volcano_types_by_country), and visualize eruption frequency by subregion (plot_eruption_frequency_by_subregion).

"""
class VolcanoAnalysis:
    """
    A class used to perform various analysis tasks on volcanic data.
    
    Attributes:
    - data (pandas.DataFrame): DataFrame containing the cleaned volcano data.
    """

    def __init__(self, csv_path):
        """
        Initialize the VolcanoAnalysis class with a CSV file path.

        Parameters:
        - csv_path (str): Path to the CSV file containing volcano data.
        """
        self.data = load_and_clean_data(csv_path)

    def show_head(self):
        """
        Display the first few rows of the cleaned DataFrame.
        """
        print(self.data.head())

    def map_volcano_locations(self):
        """
        Plot a map of volcano locations in Northern America.
        """
        plot_volcano_map(self.data, 'Volcano Locations in Northern America')

    def plot_volcano_types_by_country(self):
        """
        Plot pie charts of primary volcano types for each country.
        """
        countries = self.data['Country'].unique()
        for country in countries:
            self._plot_pie_chart_for_country(country)

    def plot_eruption_frequency_by_subregion(self):
        """
        Plot a bar chart of eruption frequency by subregion.
        """
        self.data['Last Eruption Year'] = pd.to_numeric(self.data['Last Eruption Year'], errors='coerce')
        plot_bar_chart(self.data, x_col='Last Eruption Year', y_col='Subregion', title='Eruption Frequency by Subregion', xlabel='Number of Eruptions', ylabel='Subregion')

    def _plot_pie_chart_for_country(self, country_name):
        """
        Plot a pie chart of primary volcano types for a given country.

        Parameters:
        - country_name (str): Name of the country to filter data.
        """
        country_data = self.data[self.data['Country'] == country_name]
        volcano_types = country_data['Primary Volcano Type'].value_counts()
        volcano_types = volcano_types[volcano_types > 0]
        
        plt.figure(figsize=(8, 8))
        plt.pie(volcano_types, labels=volcano_types.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(volcano_types))))
        plt.title(f'Primary Volcano Types in {country_name}')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()