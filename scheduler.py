"""
Script for extracting schedule information from
Google spreadsheet and returning the relevant data
as a JSON object.

Code is adapted for the way the data science schedule
is currently structured.

Returns different data depending on the spreadsheet ID,
cohort name, and the week number.
"""

import os.path
import pickle
from pprint import pprint

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID of the DS-Master-Schedule Google spreadsheet.
MASTER_SCHEDULE_ID = '1CQwyThQ1Zeug3Fit8BQreqsRcfFiQ6tWffTUNqyl7Gc'

BASE_PATH = os.path.split(__file__)[0]
CREDENTIALS_FILE = os.path.join(BASE_PATH, 'credentials.json')
TOKEN_FILE = os.path.join(BASE_PATH, 'token.pickle')


# Default starting values for testing
COHORT_NAME = 'sigmoid_saffron'
WEEK_NUM = '4'

def convert_week_to_cell(week_num):
    """Convert week number of course (e.g. '2', '8') into
       cell in the spreadsheet that corresponds to that week's data.
    """
    week_num = int(week_num)
    cell_num = 7*(week_num - 1) + 2
    cell = f'B{cell_num}'

    #TO-DO: Run test to check if input is valid (e.g. positive integer)

    return cell

def get_ranges(cohort_name, week_num):
    """
    Given the cohort name and week number of the course,
    generate spreadsheet cell ranges that correspond to
    the days of the week, the AM lectures, the PM lectures,
    and the header data (i.e. starting date & project title).
    Cell offset values currently hardcoded to adhere to Master Schedule format.
    """

    start_cell = convert_week_to_cell(week_num)

    #for designating the prefix of the sheet name (e.g. 'sigmoid_saffron!...')
    pre = cohort_name+'!'

    #defining letter and number ranges (e.g. B3:D7)
    start_let = start_cell[0]
    start_num = int(start_cell[1:])
    date_let = chr(ord(start_let) - 1)
    am_let = chr(ord(start_let) + 1)
    pm_let = chr(ord(start_let) + 3)

    headers = f'{pre}{start_cell}:{am_let}{start_num}'
    day_range = f'{pre}{start_let}{str(start_num+1)}:{start_let}{str(start_num+5)}'
    date_range = f'{pre}{date_let}{str(start_num+1)}:{date_let}{str(start_num+5)}'
    am_lecture_range = f'{pre}{am_let}{str(start_num+1)}:{am_let}{str(start_num+5)}'
    pm_lecture_range = f'{pre}{pm_let}{str(start_num+1)}:{pm_let}{str(start_num+5)}'

    return headers, day_range, am_lecture_range, pm_lecture_range, date_range

def authenticate():
    """
    Boilerplate code taken from Google Sheets API quickstart documentation,
    used to authenticate the API connection.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    return service


def main(cohort_name=COHORT_NAME, week_num=WEEK_NUM):
    """
    Primary function to generate JSON of the schedule corresponding
    to a particular cohort name and week number.
    """

    # Call the Sheets API
    service = authenticate()
    sheet = service.spreadsheets()

    # Grab data ranges from cells, using previously defined function.
    hr, dr, ar, pr, dater = get_ranges(cohort_name, week_num)

    headers = sheet.values().get(spreadsheetId=MASTER_SCHEDULE_ID,
                                 range=hr).execute().get('values', [])

    weekdays = sheet.values().get(spreadsheetId=MASTER_SCHEDULE_ID,
                                  range=dr).execute().get('values', [])

    am_lectures = sheet.values().get(spreadsheetId=MASTER_SCHEDULE_ID,
                                     range=ar).execute().get('values', [])

    dates = sheet.values().get(spreadsheetId=MASTER_SCHEDULE_ID,
                                     range=dater).execute().get('values', [])

    pm_lectures = sheet.values().get(spreadsheetId=MASTER_SCHEDULE_ID,
                                     range=pr).execute().get('values', [])

    if not headers:
        print(f'No data found. Ensure that schedule is filled in\
               for week {week_num}.')
    else:
        schedule_json = {
            'dates': [i[0] for i in dates],
            'headers': headers[0],
            'weekdays': [i[0] for i in weekdays],
            'am_lectures': [i[0] for i in am_lectures],
            'pm_lectures': [i[0] for i in pm_lectures]
        }

    return schedule_json

if __name__ == '__main__':
    pprint(main())
