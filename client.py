import requests


def client_add_new_patient(id, email, age):
    patient = {
        "patient_id": int(id),
        "attending_email": str(email),
        "user_age": int(age),
    }
    r = requests.post("http://127.0.0.1:5002/api/new_patient",
                      json=patient)
    return r


def client_add_patient_hr(id, hr):
    patient = {
        "patient_id": id,
        "heart_rate": hr,
    }
    r = requests.post("http://127.0.0.1:5002/api/heart_rate",
                      json=patient)
    return r


def client_get_status(patient_id):
    url = 'http://127.0.0.1:5002/api/status/{}'.format(patient_id)
    r = requests.get(url)

    return r


def client_get_hr_data(patient_id):
    url = 'http://127.0.0.1:5002/api/heart_rate/{}'.format(patient_id)
    r = requests.get(url)

    return r


def client_get_hr_avg(patient_id):
    url = 'http://127.0.0.1:5002/api/heart_rate/average/{}'.format(patient_id)
    r = requests.get(url)

    return r


def client_post_interval(id, cutoff_time):
    patient = {
        "patient_id": id,
        "heart_rate_average_since": cutoff_time,
    }

    r = requests.post("http://127.0.0.1:5002/api/heart_rate/interval_average",
                      json=patient)

    return r

if __name__ == "__main__":
    r1 = client_add_new_patient(6, 'clarkbulleit@gmail.com', 30)
    print(r1.json())

    r2 = client_add_patient_hr(6, 170)
    print(r2.json())

    r3 = client_get_status(6)
    print(r3.json())

    r4 = client_get_hr_data(6)
    print(r4.json())

    r5 = client_get_hr_avg(6)
    print(r5.json())

    cutoff_time = "2018-03-09 11:00:36.372339"
    r6 = client_post_interval(6, cutoff_time)
    print(r6.json())
