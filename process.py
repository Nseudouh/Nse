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
import numpy as np

def get_total_records(records):
    num_of_records = len(records)
    return num_of_records


def get_record(records):
    serial = tui.serial_number() # Prompt the user to enter a serial number using the serial_number function in the tui module
    if serial not in range(len(records) + 1):
        print('Record not found.')
    else:
        return records[serial -1]


def get_record_of_observe_dates(records):
    dates = tui.observation_dates()
    records = [record for record in records if record[1] in dates]
    return records


def get_record_by_region(records):
    record_group = {}
    for record in records:
        if record[3] not in record_group:
            record_group[record[3]] = []
            record_group[record[3]].append(record)
        else:
            record_group[record[3]].append(record)
    return record_group


def record_summary(records):
    summarized_records = {}
    record_by_region = get_record_by_region(records)
    for region in record_by_region:
        region_cases = np.array([record[5:] for record in record_by_region[region]], dtype=np.int32)
        region_summary = list(sum(region_cases))
        summarized_records[region] = {'total_confirmed': region_summary[0], 'total_deaths': region_summary[1],
                                      'total_recovered': region_summary[2]}
    return summarized_records


if __name__ == '__main__':
    rec = [[1, '01/22/2020', 'London', 'UK', '1/22/2020 17:00', 6, 4, 5],
           [2, '01/23/2020', 'Lagos', 'Nigeria', '1/23/2020 17:00', 4, 2, 1],
           [3, '01/24/2020', 'Lagos', 'Nigeria', '1/26/2020 17:00', 6, 3, 1],
           [4, '01/26/2020', 'Accra', 'Ghana', '1/29/2020 17:00', 4, 5, 6],
           [5, '01/29/2020', 'Ontario', 'Cannada', '1/22/2020 17:00', 4, 5, 6],
           [6, '01/28/2020', 'Manchester', 'UK', '1/29/2020 17:00', 4, 5, 6]]
    print(get_record_of_observe_dates(rec))
