import requests

url = 'http://vcm-7335.vm.duke.edu:5002/'
# url = 'http://127.0.0.1:5002/'


def client_add_new_patient(id, email, age):
    patient = {

        "patient_id": int(id),
        "attending_email": str(email),
        "user_age": int(age),
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

    id = 9
    age = 25
    hr = 70
    cutoff_time = "2018-03-09 11:00:36.372339"

    r1 = client_add_new_patient(id, 'clarkbulleit@gmail.com', age)
    print(r1.json())

    r2 = client_add_patient_hr(id, hr)
    print(r2.json())

    r3 = client_get_status(id)
    print(r3.json())

    r4 = client_get_hr_data(id)
    print(r4.json())

    r5 = client_get_hr_avg(id)
    print(r5.json())

    r6 = client_post_interval(id, cutoff_time)
    print(r6.json())
