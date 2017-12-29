import csv
from PyQt5 import QtCore

class export_query_model:

    def export_query_examination_data(self, model):
        # Create and start writing the data to the file
        self.export_file = open('RHM_export.csv', 'wt')
        self.csv_writer = csv.writer(self.export_file)

        # Go through columns to obtain headers
        exported_data = []
        for column in range(model.columnCount()):
            exported_data.append(str(model.headerData(column, QtCore.Qt.Horizontal)))
            print (exported_data)
        self.csv_writer.writerow(exported_data)

        # Go through rows to get the data
        for row in range(model.rowCount()):
            exported_data = []
            for column in range(model.columnCount()):
                exported_data.append(str(model.record(row).value(column)))
            self.csv_writer.writerow(exported_data)

        # Close writing to the file
        self.export_file.close()