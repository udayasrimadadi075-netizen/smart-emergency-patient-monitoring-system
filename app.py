from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/vitals")
def vitals():
    heart_rate = random.randint(65, 100)
    spo2 = random.randint(95, 100)
    temperature = round(random.uniform(36.2, 37.5), 1)

    emergency = (
        heart_rate < 50 or heart_rate > 120
        or spo2 < 90
        or temperature < 35 or temperature > 39
    )

    return jsonify({
        "heart_rate": heart_rate,
        "spo2": spo2,
        "temperature": temperature,
        "emergency": emergency
    })


if __name__ == "__main__":
    app.run(debug=True)
