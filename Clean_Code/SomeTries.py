def StartDance(args):
    print("call FindPatient('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(*args))


entered_name = 'name'
entered_surname = 'sname'
entered_dateofbirth = 'dob'
entered_gender ='gender'
entered_country = 'country'
entered_city = 'city'
entered_postalcode = 'postal'
entered_phonenumber = 'phone'
entered_pesel = 'pesel'

find_patient_args = [entered_name, entered_surname, entered_dateofbirth, entered_gender, entered_country, \
                     entered_city, entered_postalcode, entered_phonenumber, entered_pesel]

#StartDance(*find_patient_args)
print("call FindPatient('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(*find_patient_args))
StartDance(find_patient_args)
