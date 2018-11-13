from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    return

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
    app.run(host="127.0.0.1", port=5002)
