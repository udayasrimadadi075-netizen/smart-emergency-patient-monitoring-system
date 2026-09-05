from flask import Flask, render_template, jsonify

app = Flask(__name__)

patient = {
    "heart_rate": 130,
    "spo2": 98,
    "temperature": 36.7,
    "respiratory_rate": 16
}


def check_emergency(data):
    alerts = []

    if data["heart_rate"] < 50 or data["heart_rate"] > 120:
        alerts.append("Critical heart rate")

    if data["spo2"] < 90:
        alerts.append("Low SpO2 level")

    if data["temperature"] < 35 or data["temperature"] > 38.5:
        alerts.append("Abnormal body temperature")

    if data["respiratory_rate"] < 10 or data["respiratory_rate"] > 30:
        alerts.append("Abnormal respiratory rate")

    return alerts


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/vitals")
def vitals():
    alerts = check_emergency(patient)

    response = {
        "patient": patient,
        "emergency": len(alerts) > 0,
        "alerts": alerts
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
