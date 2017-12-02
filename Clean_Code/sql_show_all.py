class sql_show_all():

    def show_all_patients(self):

        self.patienttable_tablemodel.select()
        self.patient_table.setModel(self.patienttable_tablemodel)
        self.patient_table.resizeColumnsToContents()