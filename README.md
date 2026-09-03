# Smart Emergency Patient Monitoring System

A web-based patient monitoring system built with Python and Flask for
real-time monitoring of heart rate, SpO2, and body temperature.

## Features

- Real-time patient vital monitoring
- Heart rate monitoring
- SpO2 monitoring
- Body temperature monitoring
- Automated emergency condition detection
- Emergency alerts for critical readings
- Responsive web dashboard
- REST API integration

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- REST APIs

## Project Description

The Smart Emergency Patient Monitoring System is designed to monitor
important patient vital signs through a web-based dashboard.

The system allows users to view heart rate, SpO2, and body temperature
readings. An automated emergency detection mechanism checks the readings
against predefined critical ranges and generates an alert when a patient's
condition requires attention.

## System Architecture

Patient Vital Data
        ↓
REST API
        ↓
Flask Backend
        ↓
Emergency Detection
        ↓
Web Dashboard
        ↓
Emergency Alert

## How It Works

1. Patient vital signs are received by the application.
2. Flask processes the incoming data.
3. The system evaluates the vital signs.
4. Critical readings trigger an emergency alert.
5. Normal readings are displayed on the monitoring dashboard.

## Future Improvements

- Connect real IoT health-monitoring sensors
- Add database storage for patient records
- Add user authentication
- Add historical vital-sign charts
- Add SMS/email emergency notifications
- Deploy the application to a cloud platform

## Author

Udayasri Madadi
