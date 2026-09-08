from flask import Flask, jsonify, render_template, request

from database import get_vitals_history, initialize_database, save_vitals

app = Flask(__name__)

initialize_database()

patient = {
    "heart_rate": 78.0,
    "spo2": 98.0,
    "temperature": 36.7,
    "respiratory_rate": 16.0,
}

REQUIRED_FIELDS = (
    "heart_rate",
    "spo2",
    "temperature",
    "respiratory_rate",
)


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


def parse_vitals(data):
    if not isinstance(data, dict):
        return None, "Request body must be a JSON object."

    missing = [
        field for field in REQUIRED_FIELDS
        if field not in data
    ]

    if missing:
        return None, (
            f"Missing field(s): {', '.join(missing)}"
        )

    try:
        values = {
            field: float(data[field])
            for field in REQUIRED_FIELDS
        }
    except (TypeError, ValueError):
        return None, "All vital-sign values must be numeric."

    # Reject NaN values
    if any(value != value for value in values.values()):
        return None, "Vital-sign values must be valid numbers."

    # Reject infinity
    if any(
        value in (float("inf"), float("-inf"))
        for value in values.values()
    ):
        return None, "Vital-sign values must be finite numbers."

    # Basic input validation
    limits = {
        "heart_rate": (0, 300),
        "spo2": (0, 100),
        "temperature": (20, 50),
        "respiratory_rate": (0, 100),
    }

    for field, (minimum, maximum) in limits.items():
        if not minimum <= values[field] <= maximum:
            return None, (
                f"{field} must be between "
                f"{minimum} and {maximum}."
            )

    return values, None


def build_response():
    alerts = check_emergency(patient)

    return {
        "patient": patient,
        "emergency": bool(alerts),
        "alerts": alerts,
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/vitals", methods=["GET", "POST"])
def vitals():
    global patient

    if request.method == "POST":
        data = request.get_json(silent=True)

        patient_data, error = parse_vitals(data)

        if error:
            return jsonify({
                "error": error
            }), 400

        patient = patient_data

        alerts = check_emergency(patient)

        save_vitals(
            patient["heart_rate"],
            patient["spo2"],
            patient["temperature"],
            patient["respiratory_rate"],
            bool(alerts),
            alerts,
        )

    return jsonify(build_response())


@app.route("/api/history", methods=["GET"])
def history():
    return jsonify(get_vitals_history())


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
