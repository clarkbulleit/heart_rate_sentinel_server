from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route("/api/new_patient", methods=["POST"])
def new_patient():


@app.route("/api/heart_rate", methods=["POST"])
def post_heart_rate():


@app.route("/api/status/<patient_id>", methods=["GET"])
def status(patient_id):


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_heart_rate(patient_id):


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def average_heart_rate(patient_id):


@app.route("/api/heart_rate/interval_average", methods=["GET"])
def int_average_hr(patient_id):


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run(host="127.0.0.1", port=5002)