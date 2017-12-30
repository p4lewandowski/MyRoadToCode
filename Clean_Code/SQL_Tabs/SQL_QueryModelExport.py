import csv
from PyQt5 import QtCore
import numpy as np

class export_query_model:

    def export_query_examination_data(self, model):
        # Create and start writing the data to the file
        self.export_file = open('RHM_export.csv', 'wt', newline='')
        self.csv_writer = csv.writer(self.export_file)

        # Go through columns to obtain headers
        exported_data = []
        for column in range(model.columnCount()):
            exported_data.append(str(model.headerData(column, QtCore.Qt.Horizontal)))
        self.csv_writer.writerow(exported_data)

        # Save whole results of the export
        complete_data = []


        # Go through rows to get the data
        for row in range(model.rowCount()):

            exported_data = []

            for column in range(model.columnCount()):

                exported_data.append(str(model.record(row).value(column)))

            self.csv_writer.writerow(exported_data)
            # Append having each data category in one column
            complete_data.append(exported_data)

        complete_data = np.array(complete_data)


        # Close writing to the file
        self.export_file.close()