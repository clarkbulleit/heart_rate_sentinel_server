import requests

if __name__ == "__main__":
    patient = {
        "patient_id": 7,
        # "attending_email": 'clarkbulleit@gmail.com',
        # "user_age": 60,
        "heart_rate": 105,
    }

    # r = requests.post("http://127.0.0.1:5002/api/new_patient", json=patient)
    r = requests.post("http://127.0.0.1:5002/api/heart_rate", json=patient)
