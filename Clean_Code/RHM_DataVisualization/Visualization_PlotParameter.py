import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import sys
from PyQt5.QtWidgets import QDialog, QApplication,  QVBoxLayout
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class plott_instance(QDialog):

    def data_parsing(self, examination_name, PESEL):

        ############# Data Parsing Part #############
        a = []
        with open('C:\\Users\\Virneal\\Documents\\IFE\\Bachelor_code\\Clean_Code\\RHM_GUI\\examination_' + PESEL + '.csv', 'rt') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
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

        for i in range(0,len(examination_dates)):
            try:
                examination_dates[i] = datetime.strptime(examination_dates[i], '%Y, %m, %d, %H, %M, %S')
            except (ValueError):
                examination_dates[i] = datetime.strptime(examination_dates[i], '%Y, %m, %d, %H, %M')

        #examination_dates = [datetime.strptime(i, '%Y, %m, %d, %H, %M, %S') for i in examination_dates]
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

        self.plot_plotting(examination_dates,PESEL, examination, examination_name)

    def plot_plotting(self, examination_dates, PESEL, examination, examination_name):

        # Set up windows and data to be plotted
        fig, ax = plt.subplots()
        plotter, = ax.plot(examination_dates, examination, color='#EE6666', linewidth = 4)

        ################## GUI Properties Part ##################
        # Canvas to place figure in it
        self.canvas = FigureCanvas(fig)

        # Initialize navigation toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        ################## Plotting Properties Part ##################
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M:%S'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gcf().autofmt_xdate()
        # Set visuals and labels
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

        plt.xticks(fontsize = 6)
        ax.xaxis.set_major_locator(plt.MaxNLocator(len(examination_dates)))
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = plott_instance()
    main.data_parsing('Heart Rate', '50273596204')
    main.show()

    sys.exit(app.exec_())