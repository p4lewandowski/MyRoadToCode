from RHM_DataVisualization.Visualization_DataParsing import data_parsing
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QDialog, QApplication,  QVBoxLayout
import matplotlib.dates as mdates


class visualization_realmon():

    def realtime_plotting(self):

        # Do it once
        self.data_parsing(self.trend_examinationtype_le.text(), self.trend_pesel_le.text())
        # Set up windows and data to be plotted
        self.fig, ax = plt.subplots()
        self.plotter, = ax.plot(self.examination_dates, self.examination, color='#EE6666', linewidth=4)

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

        ################## Plotting Properties Part ##################
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M:%S'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gcf().autofmt_xdate()
        # Set visuals and labels
        ax.set(facecolor='#E6E6E6')
        plt.title(self.examination_name + ' for patient ' + self.PESEL, fontsize=12, fontstyle='italic', fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel(self.examination_name, fontsize=12)
        ax.grid(color='w', linestyle='solid')
        # lighten ticks and labels
        ax.tick_params(colors='gray', direction='in')
        for tick in ax.get_xticklabels():
            tick.set_color('0.3')
        for tick in ax.get_yticklabels():
            tick.set_color('0.3')

        # Adjust the ticksize and their amount
        plt.xticks(fontsize = 7)
        ax.xaxis.set_major_locator(plt.MaxNLocator(len(self.examination_dates)))

        while self.trend_realtime_rb.isChecked():
            self.trend_patientpart()
            self.export_query_examination_data(self.trend_patient_examination_querymodel,
                                               'examination_' + self.trend_pesel)
            data_parsing(self.trend_examinationtype_le.text(), self.trend_pesel_le.text())
            self.plotter.set_xdata(self.examination_dates)
            self.plotter.set_ydata(self.examination)
            plt.plot()
            plt.draw()
            plt.pause(0.05)

            if not self.trend_realtime_rb.isChecked():
                break

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     main = visualization_plot()
#     main.plot_plotting()
#     main.show()
#
#     sys.exit(app.exec_())
