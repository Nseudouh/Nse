"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any database related querying should be done using the appropriate functions the module 'database'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

# Task 10: Import required modules
import numpy as np
import matplotlib.pyplot as plt
import tui
import process
import database
import visual
import csv

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
covid_records = []


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    tui.progress('Data loading operation', 0)
    try:
        with open('./data/covid_19_data.csv', 'r') as covid_19_data:
            reader = csv.reader(covid_19_data)
            next(reader, None)
            for record in reader:
                covid_records.append(record)
    except FileNotFoundError as e:
        print('File is not available. Check that the covid_19_data data is in the "data" folder')
    total_num_records = len(covid_records)
    tui.total_records(total_num_records)
    tui.progress('Data loading operation', 100)

    # Populate database
    #database.setup_database(covid_records)
    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here
        response = tui.menu(0)
        if response == 1:
            tui.progress('Data processing', 0)
            option = tui.menu(1)
            if option == 1:
                tui.progress('Record retrieval process', 0)
                record = process.get_record(covid_records)
                tui.display_record(record)
                tui.progress('Record retrieval process', 100)
            elif option == 2:
                tui.progress('Record retrieval process', 0)
                records = process.get_record_of_observe_dates(covid_records)
                tui.display_records(records)
                tui.progress('Record retrieval process', 100)
            elif option == 3:
                tui.progress('Record grouping by country/region', 0)
                records = process.get_record_by_region(covid_records)
                tui.display_records(records)
                tui.progress('Record grouping by country/region', 100)
            elif option == 4:
                tui.progress('Summarise Records operation', 0)
                records = process.record_summary(covid_records)
                tui.display_records(records)
                tui.progress('Summarise Records operation', 100)
            else:
                pass
        # Task 21: Check if the user selected the option for setting up or querying the database.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has started.
        # - Query the database by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what querying is to be done.
        #   - call the appropriate function in the module 'database' to retrieve the results
        #   - call the appropriate function in the module 'tui' to display the results
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has completed.
        # TODO: Your code here

        elif response == 2:
            tui.progress('Database querying operation', 0)
            option = tui.menu(2)
            if option == 1:
                database.setup_database(covid_records)
            elif option == 2:
                country_records = database.get_country_names()
                tui.display_records(country_records)
                tui.progress('Retrieval of countries', 100)
            elif option == 3:
                case_stats = database.get_case_stats_for_serial_no()
                tui.display_records(case_stats)
                tui.progress('Retrieval of Confirmed, deaths and recoveries cases', 100)
            elif option == 4:
                top_5_countries_confirmed = database.get_top_5_countries_confirmed()
                tui.display_records(top_5_countries_confirmed)
                tui.progress('Retrieval of top 5 countries for confirmed cases', 100)
            elif option == 5:
                top_5_countries_death = database.get_top_5_countries_deaths()
                tui.display_records(top_5_countries_death)
                tui.progress('Retrieval of top 5 countries for deaths for specific observation dates', 100)
            else:
                pass


        # Task 27: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here

        elif response == 3:
            tui.progress('Visualise Data operation', 0)
            option = tui.menu(3)
            if option == 1:
                visual.display_top_5_countries_confirmed()
                tui.progress('Visualization of the top 5 countries for confirmed cases using a pie chart', 100)
            elif option == 2:
                visual.display_top_5_countries_deaths()
                tui.progress('Visualization of the top 5 countries for death for specific dates using a bar chart', 100)
            elif option == 3:
                visual.display_case_statistics()
                tui.progress('Visualization of Animated Summary', 100)

        # Task 31: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here

        elif response == 4:
            print('Bye...')
            break

        # Task 32: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here

        else:
            message = 'Invalid entry. Please enter a value between 1 and 4'
            tui.error(message)


if __name__ == "__main__":
    run()