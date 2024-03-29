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

import matplotlib.pyplot as plt
import numpy as np
import database
from matplotlib.animation import FuncAnimation


def display_top_5_countries_confirmed():
    country_names = database.get_top_5_countries_confirmed()
    values = np.array([item[1] for item in country_names])
    label = [item[0] for item in country_names]

    # A function to compute values to be displayed on each wedge of the pie chart
    def absolute_value(x):
        x = np.round(x / 100 * values.sum(), 0)
        return x

    plt.pie(values, labels=label, autopct=absolute_value)
    plt.title('Top 5 countries for confirmed cases')
    plt.show()


def display_top_5_countries_deaths():
    country_names = database.get_top_5_countries_deaths()
    values = np.array([item[1] for item in country_names])
    label = [item[0] for item in country_names]
    plt.bar(label, values)
    plt.title('Top 5 countries for death for observation dates')
    plt.show()


def display_case_statistics():
    records_country = database.get_case_statistics()
    ObservationDate = [record[0] for record in records_country[0]]
    Confirmed = [record[1] for record in records_country[0]]
    Deaths = [record[2] for record in records_country[0]]
    Recovered = [record[3] for record in records_country[0]]
    plt.plot(ObservationDate, Confirmed, label='Confirmed')
    plt.plot(ObservationDate, Deaths, label='Deaths')
    plt.plot(ObservationDate, Recovered, label='Recovered')
    plt.xlabel('ObservationDates')
    plt.ylabel('Cases')
    plt.legend()
    plt.title(f'Confirmed, Deaths & Recovery Cases over time for {records_country[1]}')
    plt.show()


if __name__ == '__main__':
    pass
