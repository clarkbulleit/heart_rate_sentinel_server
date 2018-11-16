import requests

if __name__ == "__main__":
    patient = {
        "patient_id": 1,
        # "attending_email": 'clarkbulleit@gmail.com',
        # "user_age": 55,
        # "heart_rate": 105,
        "heart_rate_average_since": "2018-03-09 11:00:36.372339",

    }

    # r = requests.post("http://127.0.0.1:5002/api/new_patient", json=patient)
    # r = requests.post("http://127.0.0.1:5002/api/heart_rate", json=patient)
    r = requests.post("http://127.0.0.1:5002/api/heart_rate/interval_average",
                      json=patient)
    print(r.json())
