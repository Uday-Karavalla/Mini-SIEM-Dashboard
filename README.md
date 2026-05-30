# 🛡️ Mini SIEM Dashboard

A Security Information and Event Management (SIEM) system built using Python, Flask, and SQLite.

## Features

- Log Collection
- Brute Force Attack Detection
- Alert Generation
- SQLite Database Storage
- Web Dashboard Monitoring

## Technologies Used

- Python
- Flask
- SQLite
- HTML

## Project Architecture

Logs.txt
↓
Detector.py
↓
Alerts.db
↓
Dashboard.py
↓
Web Dashboard

## How to Run

### Install Flask

```bash
pip install flask
```

### Run Detection Engine

```bash
python detector.py
```

### Start Dashboard

```bash
python dashboard.py
```

Open:

http://127.0.0.1:5000

## Sample Detection

Brute Force Attack Detected

Source IP: 192.168.1.10

Severity: HIGH

## Author

Uday Karavalla
