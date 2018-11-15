from flask import Flask, jsonify, request
from patients import Patient
from pymodm import connect
from validate_inputs import validate_inputs
from validate_HR_inputs import validate_hr_inputs
from is_tachycardic import is_tachycardic
import datetime
from first_sendgrid_email import send_email
app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    r = request.get_json()

    try:
        validate_inputs(r)
    except KeyError:
        return jsonify({"message": 'Required Keys not Present'}), 500

    p = Patient(r['patient_id'], attending_email=r['attending_email'],
                user_age=r['user_age'])
    p.save()
    result = {
        "message": "Added user {0} successfully "
                   "to the patient database".format(request.json["patient_id"])
    }

    return jsonify(result)


@app.route("/api/heart_rate", methods=["POST"])
def post_heart_rate():
    r = request.get_json()

    try:
        validate_hr_inputs(r)
    except KeyError:
        return jsonify({"message": 'Required Keys not Present'}), 500

    timestamp = str(datetime.datetime.now())

    p = Patient.objects.raw({"_id": r["patient_id"]}).first()

    p.heart_rate.append(r['heart_rate'])
    p.time.append(timestamp)
    p.save()

    result = {
        "message": "Added heart rate data for user {0} successfully "
                   "to the patient database".format(request.json["patient_id"])
    }
    return jsonify(result)


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    p = Patient.objects.raw({"_id": int(patient_id)}).first()
    hr = p.heart_rate[-1]
    age = p.user_age
    timestamp = p.time[-1]

    tachy = is_tachycardic(hr, age)

    result = {
        "is_tachycardic": tachy,
        "time": timestamp,
    }

    if tachy:
        send_email(patient_id, timestamp)

    return jsonify(result)


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_heart_rate(patient_id):

    try:
        id = int(patient_id)
    except ValueError:
        return jsonify({"message": "Please enter an integer"
                        }), 500

    try:
        p = Patient.objects.raw({"_id": id}).first()
        hr = p.heart_rate
    except Patient.DoesNotExist:
        return jsonify({"message": "Patient does not exist, "
                                   "please enter new patient id"
                        }), 500

    if not hr:
        return jsonify({"message": "Patient does "
                                   "not have any saved heart rates"})
    else:
        return jsonify(hr)


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_heart_rate(patient_id):
    return


@app.route("/api/heart_rate/interval_average", methods=["GET"])
def int_average_hr(patient_id):
    return


if __name__ == "__main__":
    connect("mongodb://clarkbulleit:goduke112@ds037778.mlab.com:"
            "37778/patients_cb329")
    app.run(host="127.0.0.1", port=5002)
