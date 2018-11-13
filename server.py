from flask import Flask, jsonify, request
from patients import Patient
from pymodm import connect
app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    r = request.get_json()

    p = Patient(patient_id=r['patient_id'], attending_email=r['attending_email'], user_age=r['user_age'])

    p.save()

    result = {
        "message": "Added user {0} successfully to the class list".format(request.json["patient_id"])
    }
    return jsonify(result)


@app.route("/api/heart_rate", methods=["POST"])
def post_heart_rate():
    return


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):
    return


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_heart_rate(patient_id):
    return


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_heart_rate(patient_id):
    return


@app.route("/api/heart_rate/interval_average", methods=["GET"])
def int_average_hr(patient_id):
    return


if __name__ == "__main__":
    connect("mongodb://clarkbulleit:goduke112@ds037778.mlab.com:37778/patients_cb329")
    app.run(host="127.0.0.1", port=5002)
