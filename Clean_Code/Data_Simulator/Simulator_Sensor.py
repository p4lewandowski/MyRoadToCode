from random import randint
from datetime import datetime, timedelta
import time

def sensor_simulator():

        # ################# For one patient ##################
        # patientID = 103
        # examination_type = 1
        # time.sleep(2)


        ################## For random patients ##################
        # random examination type and patient id
        examination_type = randint(1, 3)
        patientID = randint(1, 100)


        # Random time, increasing by strict amount of time per iteration cycle / or current time
        examination_date = datetime.now()
        examination_date = examination_date + timedelta(10)

        # Wellness examination
        if examination_type == 1:
            body_height = randint(150, 200)
            body_weight = randint(45, 140)

            transferred_string = '{}___{}___{}___{}___{}'.format(str(examination_type),str(patientID),str(examination_date),str(body_height),str(body_weight))

        # Heart rate examination
        elif examination_type == 2:
            heart_rate = randint(60, 100)

            transferred_string = '{}___{}___{}___{}'.format(str(examination_type),str(patientID),str(examination_date),str(heart_rate))

        # Blood pressure examination
        elif examination_type == 3:
            systolic_p = randint(100, 140)
            diastolic_p = randint(60, 100)

            transferred_string = '{}___{}___{}___{}___{}'.format(str(examination_type),str(patientID),str(examination_date),str(systolic_p),str(diastolic_p))

        return transferred_string

