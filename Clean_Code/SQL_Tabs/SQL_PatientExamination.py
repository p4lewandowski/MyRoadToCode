from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel

class patient_examination_func():

    def examination_add_criteria(self):

        # Get entered data
        entered_parameter_col = self.parameter_cb.currentText()
        entered_operator = self.operator_cb.currentText()
        entered_parameter_val = self.parameter_le.text()

        # Divide string with the data using divider
        divider = ' '
        criteria_label_text = (str(self.criteria_index), entered_parameter_col, entered_operator, entered_parameter_val)
        criteria_label_text = divider.join(criteria_label_text)

        # Collect criteria parameters
        criteria_parameters = [entered_parameter_col, entered_operator, entered_parameter_val]
        self.prepared_criteria.append(criteria_parameters)

        # Create labels per criteria
        name = 'examination_criteria_label_{}'.format(self.criteria_index)
        label = QLabel(self.criteria_container_groupbox)
        label.setObjectName(name)
        label.setText(criteria_label_text)
        label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        label.setMaximumSize(QtCore.QSize(16777215, 25))
        label.setMinimumSize(QtCore.QSize(16777215, 25))
        self.verticalLayout.addWidget(label)
        self.criteria_labels[name] = label

        self.criteria_index += 1

    def query_examination(self):
        for i in self.prepared_criteria:

            if (i[0] == 'Name' or i[0] == 'Surname' or i[0] == 'Examination Date' or i[0] == 'Parameter Warning'):

                self.queryexamination_querymodel.setQuery("call DataVisualization_str('{}', '{}')".format(i[0], i[2]))
                self.examination_table.setModel(self.queryexamination_querymodel)
                self.examination_table.resizeColumnsToContents()

            else:

                self.queryexamination_querymodel.setQuery("call DataVisualization_int('{}', '{}', '{}')".format(*i))
                self.examination_table.setModel(self.queryexamination_querymodel)
                self.examination_table.resizeColumnsToContents()

    def query_examination_reset(self):

        # Reset the table
        self.examination_table.setModel(self.examinationtable_tablemodel)
        self.examination_table.resizeColumnsToContents()

        # Deleting temporary tables in the database
        self.queryexamination_querymodel.setQuery("call DataVisualization_reset")

        # Reset the criteria labels
        for i in range(1, self.criteria_index):
            self.criteria_labels['examination_criteria_label_{}'.format(i)].deleteLater()

        # Reset the criteria index count
        self.criteria_index = 1

        # Empty the criteria with its paremeters
        self.prepared_criteria = []



