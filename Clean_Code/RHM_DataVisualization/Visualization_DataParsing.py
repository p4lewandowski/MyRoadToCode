import csv

import numpy as np

from datetime import datetime

def data_parsing(examination_name, PESEL):

    ########################## Data Parsing ##########################
    a = []
    with open ('C:\\Users\\Virneal\\Documents\\IFE\\Bachelor_code\\Clean_Code\\RHM_GUI\\examination_' + PESEL + '.csv', 'rt') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            a.append(row)
    a = np.array(a)

    mydict = dict()
    # For number of columns in array
    for i in range(0 ,len(a[0])):
        # Take headers as labels
        mydict[str(a[0 ,i])] = a[1: ,i]

    # Locate examination dates and rewrite it to array
    examination_dates = np.array(mydict['Examination Date'])
    examination = np.array(mydict['{}'.format(examination_name)]).astype(int)
    # Cut the QDatetime datatype part of the string
    examination_dates = [i[23:-1] for i in examination_dates]

    # When written from the server double 00 for seconds is omitted, therefore, different formating applies
    for i in range(0 ,len(examination_dates)):
        try:
            examination_dates[i] = datetime.strptime(examination_dates[i], '%Y, %m, %d, %H, %M, %S')
        except (ValueError):
            examination_dates[i] = datetime.strptime(examination_dates[i], '%Y, %m, %d, %H, %M')

    # examination_dates = [datetime.strptime(i, '%Y, %m, %d, %H, %M, %S') for i in examination_dates]
    examination_dates.sort()

    # If some examination value is 0 (i.e. different type of examination was done at this time, omit this data)
    data_range = len(examination)
    i = 0
    while i < data_range:
        if examination[i] == 0:
            examination = np.delete(examination, [i], 0)
            del examination_dates[i]
            data_range -= 1
        else: i+=1

    return examination_dates, examination
