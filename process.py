"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

"""
import tui
def get_total_records(records):
    num_of_records = len(records)
    # Display the number of records using the total_records function in the tui module
    tui.total_records(num_of_records)

def get_record(records):
    serial = tui.serial_number() # Prompt the user to enter a serial number using the serial_number function in the tui module
    if serial not in range(len(records)):
        print('Record not found.')
    else:
        return records[serial]
