from RHM_DataVisualization.Visualization_DataParsing import data_parsing
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QDialog, QApplication,  QVBoxLayout
import matplotlib.dates as mdates
import sys

class visualization_real_mon(QDialog):

    def realtime_plotting(self, ex_name, ex_pesel):

        # Do it once
        # ex_dates, ex_data = data_parsing(ex_name, ex_pesel)
        # # Set up windows and data to be plotted
        # self.fig, self.ax = plt.subplots()
        # self.ax.plot(ex_dates, ex_data, color='#EE6666', linewidth=4)


        self.fig = plt.figure(1)
        ex_dates, ex_data = data_parsing(ex_name, ex_pesel)
        # plt.ion() # in order to enable interactive plotting
        self.ax = self.fig.add_subplot(111)
        self.plotter, = plt.plot(ex_dates, ex_data, color='#EE6666', linewidth=4)  # after subplot to add it to subplots

        ############################### GUI Properties ###############################
        # Canvas to place figure in it
        self.canvas = FigureCanvas(self.fig)

        # Initialize navigation toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        #plt.plot()
        #plt.pause(0.2)

        ################## Plotting Properties Part ##################
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M:%S'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gcf().autofmt_xdate()
        # Set visuals and labels
        self.ax.set(facecolor='#E6E6E6')
        plt.title(ex_name + ' for patient ' + ex_pesel, fontsize=12, fontstyle='italic', fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel(ex_name, fontsize=12)
        self.ax.grid(color='w', linestyle='solid')
        # lighten ticks and labels
        self.ax.tick_params(colors='gray', direction='in')
        for tick in self.ax.get_xticklabels():
            tick.set_color('0.3')
        for tick in self.ax.get_yticklabels():
            tick.set_color('0.3')

        # Adjust the ticksize and their amount
        plt.xticks(fontsize = 7)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(len(ex_dates)))

        # try:
        #     while True:
        #         #ax.xaxis.set_major_locator(plt.MaxNLocator(len(ex__dates)))
        #         self.trend_patientpart()
        #         self.export_query_examination_data(self.trend_patient_examination_querymodel,
        #                                            'examination_' + self.trend_pesel)
        #         ex__dates, ex__param = data_parsing(self.trend_examinationtype_le.text(), self.trend_pesel_le.text())
        #         self.plotter.set_xdata(ex__dates)
        #         self.plotter.set_ydata(ex__param)
        #
        #         plt.gcf().autofmt_xdate()
        #         plt.plot()
        #         plt.draw()
        #
        #         plt.pause(0.2)
        #
        # except KeyboardInterrupt:
        #     pass


            # if not self.trend_realtime_rb.isChecked():
            #     break

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = visualization_real_mon()
    main.realtime_plotting('BMI', '65957022551')
    main.show()

    sys.exit(app.exec_())
