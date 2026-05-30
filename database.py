import sqlite3

conn = sqlite3.connect("alerts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    alert_type TEXT,
    severity TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")