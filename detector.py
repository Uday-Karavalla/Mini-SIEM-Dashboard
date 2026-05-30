import sqlite3

print("Detector Started")

failed_attempts = {}

with open("logs.txt", "r") as file:
    logs = file.readlines()

for log in logs:
    parts = log.split()

    event = parts[2]
    ip = parts[3]

    if event == "LOGIN_FAILED":
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
if event == "PORT_SCAN":

    print("ALERT!")
    print("Port Scan Detected")
    print("Source IP:", ip)

conn = sqlite3.connect("alerts.db")
cursor = conn.cursor()

for ip, count in failed_attempts.items():
    if count >= 5:

        print("ALERT!")
        print("Brute Force Attack Detected")
        print("Source IP:", ip)
        print("Failed Attempts:", count)
        print("Severity: HIGH")

        cursor.execute(
            "INSERT INTO alerts(ip, alert_type, severity) VALUES (?, ?, ?)",
            (ip, "Brute Force", "HIGH")
        )

conn.commit()
conn.close()

print("Alert Saved To Database")
