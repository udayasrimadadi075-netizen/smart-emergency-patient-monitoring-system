async function updateVitals() {
    try {
        const response = await fetch("/api/vitals");
        const data = await response.json();

        document.getElementById("heart").textContent = data.heart_rate;
        document.getElementById("spo2").textContent = data.spo2;
        document.getElementById("temperature").textContent = data.temperature;

        const status = document.getElementById("status");

        if (data.emergency) {
            status.textContent = "⚠️ EMERGENCY: Critical condition detected!";
            status.className = "status emergency";
        } else {
            status.textContent = "✓ Patient condition is normal";
            status.className = "status normal";
        }

    } catch (error) {
        document.getElementById("status").textContent =
            "Unable to connect to monitoring system.";
    }
}

updateVitals();

setInterval(updateVitals, 3000);
