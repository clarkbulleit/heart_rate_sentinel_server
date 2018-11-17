import requests
import random
from patients import Patient
from pymodm import connect
import datetime

# Configured to hit virtual machine server
# Change to other url if running on own machine
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

    print("Enter 1 to run Functions of api/add_patient POST route")
    print("Enter 2 to run Functions of api/heart_rate POST route")
    print("Enter 3 to run Functions of api/status GET route")
    print("Enter 4 to run Functions of api/heart_rate GET route")
    print("Enter 5 to run Functions of api/heart_rate/average GET route")
    print("Enter 6 to run Functions of api/heart_rate/"
          "interval_average Post route")

    route = input("Enter Route Number ")

    try:
        route_type = int(route)
    except ValueError:
        route_type = 7

    num_patients = 5
    id = list(range(1, num_patients+1))

    # tests add_new_patient route by deleting current directory and
    # adding the specified number of patients
    if route_type == 1:
        email = 'clarkbulleit@gmail.com'

        # Deletes all prior files in the database
        p = Patient.objects.raw({})
        p.delete()

        for x in range(num_patients):
            rand = random.randint(1, 101)
            add = client_add_new_patient(id[x], email, rand)
            print(add.json())

        # exhibits the feature that patient information cannot
        # be overwritten
        for x in range(num_patients):
            rand1 = random.randint(1, 101)
            add1 = client_add_new_patient(id[x], email, rand1)
            print(add1.json())

    # tests the POST patient heart rate route by
    # posting random heart rates for the patients
    if route_type == 2:
        for x in id:
            for h in range(num_patients):
                hr = random.randint(45, 190)
                post_hr = client_add_patient_hr(x, hr)
                print(post_hr.json())

        # exhibits the feature that heart rates cannot be
        # added to patients who don't exist
        for x in range(num_patients+1, num_patients+6):
            hr1 = random.randint(45, 190)
            post_hr1 = client_add_patient_hr(x, hr1)
            print(post_hr1.json())

    # Tests the GET patient status route
    if route_type == 3:
        for x in id:
            status = client_get_status(x)
            print(status.json())

        # Shows that pulling from non-existent patients is
        # handled well
        for x in range(num_patients+1, num_patients+6):
            status1 = client_get_status(x)
            print(status1.json())

    # tests the GET patient heart rate data function
    if route_type == 4:
        for x in id:
            hr_list = client_get_hr_data(x)
            print(hr_list.json())

    # tests the GET patient total average heart rate function
    if route_type == 5:
        for x in id:
            avg = client_get_hr_avg(x)
            print(avg.json())

        # Tests functionality for patients without hr data
        client_add_new_patient(num_patients+1, 'clark@gmail.com', 1)
        avg1 = client_get_hr_avg(num_patients+1)
        print(avg1.json())

    # tests the POST patient interval average hr route
    if route_type == 6:
        cutoff_time = "2018-11-17 08:50:53.059721"
        time_now = str(datetime.datetime.now())

        for x in id:
            r6 = client_post_interval(x, cutoff_time)
            print(r6.json())

        # tests what happens when there are no heart rates
        # after the cutoff time
        for x in id:
            interval = client_post_interval(x, time_now)
            print(interval.json())

    if route_type == 7:
        print("Please enter and integer and run client.py again")
