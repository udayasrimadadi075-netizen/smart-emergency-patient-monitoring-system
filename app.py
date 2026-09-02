from flask import Flask, render_template, jsonify

app = Flask(__name__)

patient = {
    "heart_rate": 78,
    "spo2": 98,
    "temperature": 36.7,
    "respiratory_rate": 16
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/vitals")
def vitals():
    return jsonify(patient)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
