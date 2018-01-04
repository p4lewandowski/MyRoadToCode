from RHM_DataVisualization.Visualization_SteadyPlot import visualization_plot
from RHM_DataVisualization.Visualization_DataParsing import data_parsing
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog
import matplotlib.dates as mdates

class visualization_func_call(QDialog):

    # When the buttons on Trend-Tab (monitoring) are clicked
    def examination_parameter_plotting(self):

        # Fetch the data from the server
        self.trend_patientpart()
        self.export_query_examination_data(self.trend_patient_examination_querymodel,
                                           'examination_' + self.trend_pesel)

        # If radio button clicked - realtime plotting
        if self.trend_realtime_rb.isChecked():

            # Otherwise multiple figures may appear
            plt.close("all")
            # Disable Line Edit
            self.trend_examinationtype_le.setDisabled(True)

            # Do it once
            ex__dates, ex__param = data_parsing(self.trend_examinationtype_le.text(), self.trend_pesel_le.text())
            # Set up windows and data to be plotted
            self.fig = plt.figure('Real Time Plotting')
            ax = self.fig.add_subplot(111)
            self.plotter, = ax.plot(ex__dates, ex__param, color='#EE6666', linewidth=4)

            ################## Plotting Properties Part ##################
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M:%S'))
            ax.xaxis.set_major_locator(mdates.DayLocator())

            # Set visuals and labels
            ax.set(facecolor='#E6E6E6')
            plt.title('{}'.format(self.trend_examinationtype_le.text()) + ' for patient ' + '{}'.format(self.trend_pesel_le.text()), fontsize=12, fontstyle='italic',
                      fontweight='bold')
            plt.xlabel('Date', fontsize=12)
            plt.ylabel(self.trend_examinationtype_le.text(), fontsize=12)
            ax.grid(color='w', linestyle='solid')
            # lighten ticks and labels
            ax.tick_params(colors='gray', direction='in')
            for tick in ax.get_xticklabels():
                tick.set_color('0.3')
            for tick in ax.get_yticklabels():
                tick.set_color('0.3')

            # Adjust the ticksize and their amount
            plt.xticks(fontsize=7)

            while self.trend_realtime_rb.isChecked():

                try:

                    # Fetch the data each time
                    self.trend_patientpart()
                    self.export_query_examination_data(self.trend_patient_examination_querymodel,
                                                       'examination_' + self.trend_pesel)
                    ex__dates, ex__param = data_parsing(self.trend_examinationtype_le.text(), self.trend_pesel_le.text())

                    # Set new data
                    self.plotter.set_xdata(ex__dates)
                    self.plotter.set_ydata(ex__param)

                    # Crucial for proper date on x-axis display
                    self.fig.autofmt_xdate()
                    # Set strict number of ticks on x-axis
                    ax.xaxis.set_major_locator(plt.MaxNLocator(15))

                    # Set dynamic plot range
                    plt.axis(xmax = ex__dates[-1], ymin = min(ex__param)-10, ymax = max(ex__param) + 10)
                    # Allows the GUI to run during the pause
                    plt.pause(0.2)

                    if not self.trend_realtime_rb.isChecked():
                        # If real time unchecked enable Line Edit
                        self.trend_examinationtype_le.setDisabled(False)
                        self.trend_examinationtype_le.setEnabled(True)
                        break

                except:

                    # in case some error occurs the Line Edit still has to be re-enabled
                    self.trend_examinationtype_le.setDisabled(False)
                    self.trend_examinationtype_le.setEnabled(True)
                    break


        # If not - plot the steady parameter
        else:

            new_plot = visualization_plot()
            ex_dates, ex_param = data_parsing(self.trend_examinationtype_le.text(), self.trend_pesel_le.text())
            new_plot.plot_plotting(ex_dates, ex_param, self.trend_examinationtype_le.text(), self.trend_pesel_le.text())
            new_plot.show()


    def trend_patientpart(self):
        # Reset table before new search
        self.queryexamination_querymodel.setQuery("call DataVisualization_reset")
        self.trend_pesel = self.trend_pesel_le.text()
        # Find patient
        self.trend_findpatient_querymodel.setQuery(
            "call FindPatient_OR('', '', '', '', '', '', '', '', '{}')".format(self.trend_pesel))
        self.trend_patient_table.setModel(self.trend_findpatient_querymodel)
        self.trend_patient_table.resizeColumnsToContents()
        # When data gathered go to examinationpart
        self.trend_examinationpart()

    def trend_examinationpart(self):
        # Find patient's examinations and show it in table
        self.trend_patient_examination_querymodel.setQuery(
            "call DataVisualization_str('PESEL', '{}')".format(self.trend_pesel))
        self.trend_examinations_table.setModel(self.trend_patient_examination_querymodel)
        self.trend_examinations_table.resizeColumnsToContents()
        # export the data to file to be parsed later
        self.export_query_examination_data(self.trend_patient_examination_querymodel, 'examination_' + self.trend_pesel)

