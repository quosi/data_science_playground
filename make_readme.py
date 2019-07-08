"""
Dynamically generate a README file with the schedule
(in tabular format, with hyperlinks), based on the cohort and week selected.
"""

from scheduler import main

COHORT = "sigmoid_saffron"
WEEK = "1"
OUTPUT_FILE = "TEST.md"

def make_readme(cohort, week):
    """Using data extracted from the Google Sheets API (by calling the main
       scheduler function), generate a README file (line-by-line) that
       writes the schedule into tabular format with the appropriate data
       and associate hyperlinks.
    """

    j = main(cohort, week)

    cohort_title = " ".join(cohort.split('_')).title()
    sub_title = ' ('.join(list(reversed(j['headers'])))+')'
    wkdy = j['weekdays']
    am = j['am_lectures']
    pm = j['pm_lectures']

    with open(OUTPUT_FILE, 'w') as readme:
        readme.write('# {} Schedule\n\n'.format(cohort_title))
        readme.write('## {}\n\n'.format(sub_title))
        readme.write('| Day | Morning (9:15) | Afternoon (13:30) |')
        readme.write('\n| - | :--: | :--: |')

        for i, (w, a, p) in enumerate(zip(wkdy, am, pm)):
            readme.write(f'\n| {w} | [{a}][{i*2+1}] | [{p}][{i*2+2}] |')

        URL = 'http://krspiced.pythonanywhere.com'
        #At the moment, just hyperlinking all lectures in the table
        #to the main page of the course material, until I can think of
        #a good way to map the titles with the correct html files.

        for i in range(1, 2*len(wkdy) + 1):
            readme.write(f'\n\n[{i}]: {URL}')

        print(f'Successfully generated {OUTPUT_FILE}')


if __name__ == '__main__':
    make_readme(COHORT, WEEK)
