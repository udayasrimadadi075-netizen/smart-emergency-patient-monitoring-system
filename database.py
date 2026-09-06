import sqlite3

DATABASE = "patients.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS vital_signs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            heart_rate REAL NOT NULL,
            spo2 REAL NOT NULL,
            temperature REAL NOT NULL,
            respiratory_rate REAL NOT NULL,
            emergency INTEGER NOT NULL,
            alerts TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_vitals(heart_rate, spo2, temperature, respiratory_rate,
                emergency, alerts):

    connection = get_connection()

    connection.execute("""
        INSERT INTO vital_signs
        (heart_rate, spo2, temperature, respiratory_rate, emergency, alerts)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        heart_rate,
        spo2,
        temperature,
        respiratory_rate,
        int(emergency),
        ", ".join(alerts)
    ))

    connection.commit()
    connection.close()


def get_vitals_history():

    connection = get_connection()

    records = connection.execute("""
        SELECT *
        FROM vital_signs
        ORDER BY created_at DESC
    """).fetchall()

    connection.close()

    return [dict(record) for record in records]
