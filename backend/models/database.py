
import sqlite3

def init_db():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS vitals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            heart_rate INTEGER,
            spo2 INTEGER,
            temperature REAL,
            alcohol_level REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_vitals(data):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute("INSERT INTO vitals (patient_id, heart_rate, spo2, temperature, alcohol_level) VALUES (?, ?, ?, ?, ?)",
              (data['patient_id'], data['heart_rate'], data['spo2'], data['temperature'], data['alcohol_level']))
    conn.commit()
    conn.close()

def get_latest_vitals():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute("SELECT patient_id, heart_rate, spo2, temperature, alcohol_level FROM vitals ORDER BY timestamp DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return str(rows)
