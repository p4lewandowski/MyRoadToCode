class patient_credentials_func():

    # Searching for patients is enabled with stored procedures on the server, not via querying

    def show_all_patients(self):

        #self.patienttable_tablemodel.select()
        self.patient_table.setModel(self.patienttable_tablemodel)
        self.patient_table.resizeColumnsToContents()
        # Enable all the values to be exported
        self.findpatient_querymodel.setQuery("call FindPatient_OR('%','%','%','%','%','%','%','%','%')")


    def call_find_patient(self):

        # For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
        entered_name = self.name_le.text()
        entered_surname = self.surname_le.text()
        entered_dateofbirth = self.dateofbirth_le.text()
        entered_gender = self.gender_cb.currentText()
        entered_country = self.country_cb.currentText()
        entered_city = self.city_le.text()
        entered_postalcode = self.postalcode_le.text()
        entered_phonenumber = self.phonenumber_le.text()
        entered_pesel = self.pesel_le.text()

        find_patient_args = [entered_name, entered_surname, entered_dateofbirth,entered_gender,entered_country, \
                             entered_city,entered_postalcode,entered_phonenumber,entered_pesel]


        if self.enable_a_search.isChecked():
            for index, values in enumerate(find_patient_args):
                if not find_patient_args[index]:
                    find_patient_args[index] = 'Null'

            # Calling QSqlQueryModel with specified query
            self.findpatient_querymodel.setQuery("call FindPatient_OR('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(*find_patient_args))

        else:
            for index, values in enumerate(find_patient_args):
                if not find_patient_args[index]:
                    find_patient_args[index] = '%'
            self.findpatient_querymodel.setQuery("call FindPatient_AND('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(*find_patient_args))

        # Changing table display
        self.patient_table.setModel(self.findpatient_querymodel)
        self.patient_table.resizeColumnsToContents()
