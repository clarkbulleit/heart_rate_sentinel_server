from flask import Flask, jsonify, request
from patients import Patient
from pymodm import connect
from validate_post_inputs import validate_post_inputs
from is_tachycardic import is_tachycardic
import datetime
from first_sendgrid_email import send_email
from calc_avg_hr import calc_avg_hr
from validate_GET_request import validate_get_request
app = Flask(__name__)

error_messages = {
        0: {"message": "Please enter an integer"},
        1: {"message": "Patient does not exist, please enter new patient id"},
        2: {"message": "Patient does not have any saved heart rates"},
        3: {"message": "heart rate list contains non numeric inputs"},
        4: {"message": 'Required Keys not Present'},
        5: {"message": 'Cannot overwrite current patient information'},
        6: {"message": 'No heart rates exist after this time'}
            }


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    r = request.get_json()

    try:
        validate_post_inputs(r, 1)
    except KeyError:
        return jsonify(error_messages[4]), 500

    try:
        p = Patient.objects.raw({"_id": r['patient_id']}).first()
    except Patient.DoesNotExist:
        p = Patient(r['patient_id'], attending_email=r['attending_email'],
                    user_age=r['user_age'])
    else:
        return jsonify(error_messages[5]), 500

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
        validate_post_inputs(r, 2)
    except KeyError:
        return jsonify(error_messages[4]), 500

    timestamp = str(datetime.datetime.now())

    try:
        p = Patient.objects.raw({"_id": r["patient_id"]}).first()
    except Patient.DoesNotExist:
        return jsonify(error_messages[1]), 500

    p.heart_rate.append(r['heart_rate'])
    p.time.append(timestamp)

    tachy = is_tachycardic(r['heart_rate'], p.user_age)
    p.is_tachycardic = tachy
    p.save()

    # if tachy:
    # send_email(r['patient_id'], timestamp)

    result = {
        "message": "Added heart rate data for user {0} successfully "
                   "to the patient database".format(request.json["patient_id"])
    }
    return jsonify(result)


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    out = validate_get_request(patient_id)

    if out == 3:
        p = Patient.objects.raw({"_id": int(patient_id)}).first()
    else:
        return jsonify(error_messages[out]), 500

    tachy = p.is_tachycardic
    timestamp = p.time[-1]

    return jsonify({"Patient {} is tachycardic".format(patient_id): tachy,
                    "Time": timestamp})


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_heart_rate(patient_id):

    out = validate_get_request(patient_id)

    if out == 3:
        p = Patient.objects.raw({"_id": int(patient_id)}).first()
        return jsonify(p.heart_rate)
    else:
        return jsonify(error_messages[out]), 500


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_heart_rate(patient_id):
    out = validate_get_request(patient_id)

    if out == 3:
        p = Patient.objects.raw({"_id": int(patient_id)}).first()
        hr = p.heart_rate
    else:
        return jsonify(error_messages[out]), 500

    try:
        avg = calc_avg_hr(hr, 1, 1)
    except ZeroDivisionError:
        return jsonify(error_messages[2]), 500
    except TypeError:
        return jsonify(error_messages[3]), 500

    return jsonify({"message": "Patient {}'s average "
                               "heart rate is {} bpm".format(patient_id, avg)})


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def int_average_hr():
    r = request.get_json()

    try:
        validate_post_inputs(r, 3)
    except KeyError:
        return jsonify(error_messages[4]), 500

    try:
        p = Patient.objects.raw({"_id": r["patient_id"]}).first()
    except Patient.DoesNotExist:
        return jsonify(error_messages[1]), 500
    hr = p.heart_rate
    times = p.time
    date = r["heart_rate_average_since"]

    try:
        avg_hr_since = calc_avg_hr(hr, times, date)
    except ZeroDivisionError:
        return jsonify(error_messages[2]), 500
    except TypeError:
        return jsonify(error_messages[3]), 500
    except UnboundLocalError:
        return jsonify(error_messages[6]), 500

    return jsonify({"message": "The patients average "
                               "heart rate since {} "
                               "is {} bpm".format(
                                r['heart_rate_average_since'],
                                avg_hr_since)})


if __name__ == "__main__":
    connect("mongodb://clarkbulleit:goduke112@ds037778.mlab.com:"
            "37778/patients_cb329")
    app.run(host="127.0.0.1", port=5002)
