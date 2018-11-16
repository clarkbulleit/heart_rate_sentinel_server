import requests
import random
from patients import Patient
from pymodm import connect

# url = 'http://vcm-7335.vm.duke.edu:5002/'
url = 'http://127.0.0.1:5002/'


def client_add_new_patient(id, email, age):
    patient = {

        "patient_id": id,
        "attending_email": email,
        "user_age": age,
    }
    r = requests.post(url + 'api/new_patient',
                      json=patient)
    return r


def client_add_patient_hr(id, hr):
    patient = {
        "patient_id": id,
        "heart_rate": hr,
    }
    r = requests.post(url + 'api/heart_rate',
                      json=patient)
    return r


def client_get_status(patient_id):
    r = requests.get(url + 'api/status/{}'.format(patient_id))
    return r


def client_get_hr_data(patient_id):
    r = requests.get(url + 'api/heart_rate/{}'.format(patient_id))

    return r


def client_get_hr_avg(patient_id):
    r = requests.get(url + 'api/heart_rate/average/{}'.format(patient_id))

    return r


def client_post_interval(id, cutoff_time):
    patient = {
        "patient_id": id,
        "heart_rate_average_since": cutoff_time,
    }

    r = requests.post(url + 'api/heart_rate/interval_average',
                      json=patient)

    return r


if __name__ == "__main__":
    connect("mongodb://clarkbulleit:goduke112@ds037778.mlab.com:"
            "37778/patients_cb329")

    route_type = 1
    num_patients = 5

    id = list(range(1, num_patients+1))

    # tests add_new_patient route by deleting current directory and
    # adding the specified number of patients

    # Deletes all prior files in the database
    p = Patient.objects.raw({})
    p.delete()

    if route_type == 1:
        email = 'clarkbulleit@gmail.com'

        for x in range(num_patients):
            r = random.randint(1, 101)
            r1 = client_add_new_patient(id[x], email, r)
            print(r1.json())

    # tests the POST patient heart rate route by
    # posting random heart rates for the patients
    if route_type == 2:
        for x in id:
            print(x)
            for h in range(num_patients):
                hr = random.randint(45, 190)
                r2 = client_add_patient_hr(x, hr)
                print(r2.json())

    # Tests the GET patient status route
    if route_type == 3:
        for x in id:
            r3 = client_get_status(x)
            print(r3.json())

    # r4 = client_get_hr_data(id)
    # print(r4.json())

    # r5 = client_get_hr_avg(id)
    # print(r5.json())

    # r6 = client_post_interval(id, cutoff_time)
    # print(r6.json())