"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should display the title 'COVID-19 (January) Data'.
    The welcome message should contain dashes above and below the title.
    The number of dashes should be equivalent to the number of characters in the title.

    :return: Does not return anything.
    """
    # TODO: Your code here
    print("""----------------------- 
        COVID-19 (January) Data
        -----------------------""")


def error(msg):
    """
    Task 2: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter 'msg' passed to this function

    :param msg: a string containing an error message
    :return: does not return anything
    """
    # TODO: Your code here
    error_msg = msg
    print(f'Error! {error_msg}')


def progress(operation, value):
    """
    Task 3: Display a message to indicate the progress of an operation.

    The function should display a message in the following format:
    '{operation} {status}.'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'has started' if the value of the parameter 'value' is 0
    {status} is 'is in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'has completed' if the value of the parameter 'value' is 100

    :param operation: a string indicating the operation being started
    :param value: an integer indicating the amount of progress made
    :return: does not return anything
    """
    # TODO: Your code here
    if value == 0:
        status = 'has started'
        print(f'{operation} {status}')
    elif (value > 0) & (value < 100):
        status = 'is in progress'
        print(f'{operation} {status} ({value}% completed)')
    elif value == 100:
        status = 'has completed'
        print(f'{operation} {status}')
    else:
        pass


def menu(variant=0):
    """
    Task 4: Display a menu of options and read the user's response.

    If no value or a zero is supplied for the parameter 'variant' then a menu with the following options
    should be displayed:

    '[1] Process Data', '[2] Query Database', '[3] Visualise Data' and '[4] Exit'

    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:

    '[1] Record by Serial Number', '[2] Records by Observation Date', '[3] Group Records by Country/Region,
    '[4] Summarise Records'

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Setup database',
    '[2] Retrieve all countries in alphabetical order from the database',
    '[3] Retrieve confirmed cases, deaths and recoveries for an observation from the database',
    '[4] Retrieve top 5 countries for confirmed cases from the database from the database',
    '[5] Retrieve top 5 countries for deaths for specific observation dates form the database'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    '[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: nothing if invalid selection otherwise an integer for a valid selection
    """
    # TODO: Your code here
    if variant == 0: # Use if condition to check the value of variant
        print('[1] Process Data, [2] Query Database, [3] Visualise Data and [4] Exit') # Print the category of menu
        response = int(input('Enter a number for your choice operation from the displayed options: '))
        if response not in [1, 2, 3, 4]: # Check that user entry is valid
            print('Invalid entry. Please enter a number from the displayed options.')
        else:
            return response
    elif variant == 1:
        print('[1] Record by Serial Number, [2] Records by Observation Date, [3] Group Records by Country/Region, [4] Summarise Records')
        response = int(input('Enter a number for your choice operation from the displayed options: '))
        if response not in [1, 2, 3, 4]: # Check that user entry is valid
            print('Invalid entry. Please enter a number from the displayed options.')
        else:
            return response
    elif variant == 2:
        print('''
        [1] Setup database
        [2] Retrieve all countries in alphabetical order from the database
        [3] Retrieve confirmed cases, deaths and recoveries for an observation from the database
        [4] Retrieve top 5 countries for confirmed cases from the database from the database
        [5] Retrieve top 5 countries for deaths for specific observation dates form the database
        ''')
        response = int(input('Enter a number for your choice operation from the displayed options: '))
        if response not in [1, 2, 3, 4, 5]: # Check that user entry is valid
            print('Invalid entry. Please enter a number from the displayed options.')
        else:
            return response
    elif variant == 3:
        print('[1] Country/Region Pie Chart, [2] Observations Chart, [3] Animated Summary')
        response = int(input('Enter a number for your choice operation from the displayed options: '))
        if response not in [1, 2, 3]:
            print('Invalid entry. Please enter a number from the displayed options.')
        else:
            return response
    else:
        print('Invalid entry. Please enter a valid number - 0, 1, 2, or 3')



def total_records(num_records):
    f"""
    Task 5: Display the total number of records in the data set.

    The function should display a message in the following format:

    "There are {num_records} records in the data set."

    Where {num_records} is the value of the parameter passed to this function

    :param num_records: the total number of movies in the data set
    :return: Does not return anything
    """
    print(f'There are {num_records} records in the data set.')

def serial_number():
    """
    Task 6: Read in the serial number of a record and return the serial number.

    The function should ask the user to enter a serial number for a record e.g. 189
    The function should then read in and return the user's response as an integer.

    :return: the serial number for a record
    """
    # TODO: Your code here
    serial_num = int(input('Enter a serial number for a record: '))
    return serial_num

def observation_dates():
    """
    Task 7: Read in and return a list of observation dates.

    The function should ask the user to enter some observation dates
    This should be entered in the format dd/mm/yyyy where dd is two-digit day, mm is two digit month and yyyy is
    a four digit year e.g. 01/22/2020
    The function should return a list containing the specified observation dates.

    :return: a list of observation dates
    """
    # TODO: Your code here
    observation_dates = []
    counter = 1 # used to determine when to exit the loop
    number_of_dates = int(input('How many dates do you want to observe?: ')) # Prompt the user for the number of dates to observe
    while counter <= number_of_dates: # A while condition to determine if more dates should be entered.
        date = input('Enter a date in the format - dd/mm/yyyy: ')
        observation_dates.append(date)
        counter += 1
    return observation_dates

def display_record(record, cols=None):
    """
    Task 8: Display a record. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the record will be displayed.

    The parameter record is a list of values e.g. [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    The parameter cols is a list of column indexes e.g. [0,3,5]
    The function should display a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    ['01/22/2020','Mainland China']

    E.g. if cols is [0,1,4] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    [1,'01/22/2020','1/22/2020 17:00']

    E.g. if cols is an empty list or None then all the values will be displayed
    [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]

    :param record: A list of data values for a movie
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """

    if cols == None:
        print(record)
    else:
        record = [record[val] for val in cols]
        print(record)


def display_records(records, cols=None):
    """
    Task 9: Display each record in the specified list of records.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a movie will be displayed.

    The function should have two parameters as follows:

    records     which is a list of records where each record itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each record in records and display the record.

    Each record should be displayed as a list of values e.g. [1,01/22/2020,Anhui,Mainland China,1/22/2020 17:00,1,0,0]
    Only the columns whose indexes are included in cols should be displayed for each record.

    If cols is an empty list or None then all values for the record should be displayed.

    :param records: A list of records
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    if cols == None:
        print(records)
    else:
        records = [records[val] for val in cols]
        print(records)
