import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def do_what_i_want(examination_name, PESEL):

    # scsv = """Date,Examination,Polish,non-Latin,letters
    # 1,2,3,4,5
    # 3,4,c,d,e
    # 5,6,wąż,idzie,wąską
    # 6,8,wąż,idzie,wąską
    # 11,6,wąż,idzie,wąską"""

    a = []
    # reader = csv.reader(scsv.split('\n'), delimiter=',')
    # for row in reader:
    #     a.append(row)

    with open('C:\\Users\\Virneal\\Documents\\IFE\\Bachelor_code\\Clean_Code\\RHM_exportE.csv', 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            a.append(row)
    a = np.array(a)

    mydict = dict()
    # For number of columns in array
    for i in range(0,len(a[0])):
        # Take headers as labels
        mydict[str(a[0,i])] = a[1:,i]


    examination_dates = np.array(mydict['Examination Date'])
    examination = np.array(mydict['{}'.format(examination_name)]).astype(int)

    examination_dates = [i[23:-1] for i in examination_dates]
    examination_dates = [datetime.strptime(i, '%Y, %m, %d, %H, %M, %S') for i in examination_dates]
    examination_dates.sort()

    data_range = len(examination)
    i = 0
    while i < data_range:
        if examination[i] == 0:
            examination = np.delete(examination, [i], 0)
            del examination_dates[i]
            data_range -= 1
        else:
            i+=1

    ############# Plot Properties #############
    fig, ax = plt.subplots()
    plt.plot(examination_dates, examination, color='#EE6666', linewidth = 4)


    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()

    ax.set(facecolor='#E6E6E6')
    plt.title(examination_name + ' for patient ' + PESEL, fontsize=12, fontstyle='italic', fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel(examination_name, fontsize=12)
    ax.grid(color='w', linestyle='solid')
    # lighten ticks and labels
    ax.tick_params(colors='gray', direction='in')
    for tick in ax.get_xticklabels():
        tick.set_color('0.3')
    for tick in ax.get_yticklabels():
        tick.set_color('0.3')


    plt.xticks(fontsize = 8)
    ax.xaxis.set_major_locator(plt.MaxNLocator(1.4*len(examination_dates)))

    fig.savefig("test.png", format='eps', dpi=1000)
    plt.show()



#do_what_i_want('Heart Rate', '05479329432')