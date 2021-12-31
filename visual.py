"""
This module is responsible for visualising the data retrieved from a database using Matplotlib.
"""

"""
Task 28 - 30: Write suitable functions to visualise the data as follows:

- Display the top 5 countries for confirmed cases using a pie chart
- Display the top 5 countries for death for specific dates using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country/countries.

Each function for the above should utilise the functions in the module 'database' to retrieve any data.
You may add additional methods to the module 'database' if needed. Each function should then visualise
the data using Matplotlib.
"""

# TODO: Your code here

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import database
import matplotlib.animation as animation

def display_top_5_countries_confirmed():
    country_names = database.get_top_5_countries_confirmed()
    values = np.array([item[1] for item in country_names])
    label = [item[0] for item in country_names]
    # A function to compute values to be displayed on each wedge of the pie chart
    def absolute_value(x):
        x = np.round(x/100 * values.sum(), 0)
        return x
    plt.pie(values, labels = label, autopct= absolute_value)
    plt.title('Top 5 countries for confirmed cases')
    plt.show()


def display_top_5_countries_deaths():
    country_names = database.get_top_5_countries_deaths()
    values = np.array([item[1] for item in country_names])
    label = [item[0] for item in country_names]
    plt.bar(label, values)
    plt.title('Top 5 countries for death for observation dates')
    plt.show()