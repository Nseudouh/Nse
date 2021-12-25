"""
This module is responsible for setting up and querying the database.
"""

"""
Task 22 - 26: Write suitable functions to query the database as follows:

Setup database
Retrieve the names of all (unique) countries in alphabetical order
Retrieve the number of confirmed cases, deaths and recoveries for a specified observation / serial number.
Retrieve information for the top 5 countries for confirmed cases
Retrieve information for the top 5 countries for death for specific observation dates


The function for setting up the database should do the following:
- Take a list of records as a parameter
- Use the list passed as a parameter value to create and populate a suitable database. You are required to design a
suitable (small) database.
- It is recommended that you complete this function last and start by creating your database using a tool such as
SQL DB Browser. This would allow you to complete the other database functions first.  You can then complete this
function to generate the database via code.

Each function for querying the database should follow the pattern below:
- Take no parameters
- Query the database appropriately. You may use the module 'tui' to retrieve any additional information 
required from the user to complete the querying.
- Return a list of records as retrieved from the database

"""
import tui
import sqlite3
from sqlite3 import Error

# Establish connection to the database
connection = None
try: # A try & except block to connect to database or catch connection error
    connection = sqlite3.connect(r'C:\Users\nudou\Documents\com728_project_assignment\project_database.db')
    cursor = connection.cursor() # Create a cursor object for executing sql queries
except Error as e:
    print('Unable to establish connection to the database', e)


def setup_database(records):
        tuple_records = [tuple(record) for record in records] # Convert list of records to a format (tuple) required by the database
        # Define the sql query to insert data into the database
        query = 'INSERT INTO covid_19_data (SNo, ObservationDate, State, Country, LastUpdate, Confirmed, Deaths, Recovered) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        cursor.executemany(query, tuple_records)
        connection.commit() # Save changes to the database
        print('Records populated successfully to the database')
        if connection:
            connection.close()


def get_country_names():
    # Define sql query to extract data
    query = '''
    SELECT DISTINCT Country FROM covid_19_data
    ORDER BY 1 ASC
    '''
    cursor.execute(query)
    records = [list(record) for record in cursor.fetchall()] # Covert records of tuple to list of records
    return records


def get_case_stats_for_serial_no():
    s_no = tui.serial_number() # Re-use the serial_number function from tui module
    # Define sql query to extract data
    query = '''
    SELECT SNo, Confirmed, Deaths, Recovered
    FROM covid_19_data
    WHERE SNo = {0}
    '''.format(s_no)
    cursor.execute(query)
    records = [list(record) for record in cursor.fetchall()] # Covert records of tuple to list of records
    return records


def get_top_5_countries_confirmed():
    # Define sql query to extract data
    query = '''
    SELECT Country, sum(Confirmed) as total_confirmed FROM covid_19_data
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 5
    '''
    cursor.execute(query)
    records = [list(record) for record in cursor.fetchall()] # Covert records of tuple to list of records
    return records
