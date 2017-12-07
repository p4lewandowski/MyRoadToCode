import numpy as np

def add_one_more():

    entered_parameter_col_1 = 'param'
    entered_operator_1 = 'operator'
    entered_parameter_val_1 = 'pvalue'
    criteria_index = 0
    criteria_index += 1
    divider = ' '
    criteria_label_lext = (str(criteria_index), entered_parameter_col_1, entered_operator_1, entered_parameter_val_1)
    criteria_label_lext = divider.join(criteria_label_lext)
    #print(criteria_label_lext)
    prepared_criteria = ['p1','o1','pv1']
    criteria_parameters = [entered_parameter_col_1, entered_operator_1, entered_parameter_val_1]
    prepared_criteria = np.vstack([prepared_criteria, criteria_parameters])
    #print(prepared_criteria[1])
    for i in prepared_criteria:
        print (i[1])
        #print(i)

add_one_more()
b = [['Diastolic Pressure', '>', '100'], ['Diastolic Pressure', '<', '110']]
#print (*b[1])


