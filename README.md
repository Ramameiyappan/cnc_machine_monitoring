# CNC Machine Monitoring System (Django)

This project is a Django-based CNC Machine Monitoring System designed to collect machine data, monitor machine health, generate alerts, assign technicians, and improve operational efficiency.

It simulates how automated machines in a factory communicate with a central monitoring server.

---

## Features

- Machine registration and monitoring
- Technician management
- Operation tracking
- Real-time alert generation
- Alert resolution system
- Admin dashboard
- REST APIs for integration
- Automated health monitoring

---

## Tech Stack

- Backend: Django, Django REST Framework
- Database: SQLite / MySQL / PostgreSQL
- Frontend: HTML, CSS (Django Templates)
- API Testing: Postman

---

## Project Setup

### 1. Clone Repository
clone this repo

---

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6. Start Server

```bash
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

# 🔗 API Endpoints

Base URL:

```
http://127.0.0.1:8000/
```

---

## 1️⃣ Machine API

### Get All Machines

**Method:** GET  
**Endpoint:**
```
/machines/
```

**Description:**  
Returns a list of all registered machines.

---

### Create Machine

**Method:** POST  
**Endpoint:**
```
/machines/
```

**Description:**  
Registers a new machine in the system.

**Sample Request:**
```json
{
  "name": "CNC-01",
  "machine_type": "CNC",
  "status": "running"
}
```

---

## 2️⃣ Technician API

### Get All Technicians

**Method:** GET  
**Endpoint:**
```
/technician/
```

**Description:**  
Returns a list of all technicians.

---

### Create Technician

**Method:** POST  
**Endpoint:**
```
/technician/
```

**Description:**  
Creates a technician and automatically assigns a pending alert.

**Sample Request:**
```json
{
  "name": "Ramu",
  "phone": "9876543210",
  "available": true
}
```

---

## 3️⃣ Operation API (Telemetry Data)

### Send Operation Data

**Method:** POST  
**Endpoint:**
```
/operation/
```

**Description:**  
Sends machine telemetry data and triggers health monitoring.

**Sample Request:**
```json
{
  "machine": 1,
  "temperature": 78,
  "vibration": 40,
}
```

---

## 4️⃣ Alert API

### Get Active Alerts

**Method:** GET  
**Endpoint:**
```
/alert/
```

**Description:**  
Returns all unresolved alerts sorted by severity.

---

## 5️⃣ Resolve Alert API

### Resolve an Alert

**Method:** POST  
**Endpoint:**
```
/alert/resolve/<alert_id>/
```

**Example:**
```
/alert/resolve/3/
```

**Description:**  
Marks the alert as resolved, frees the technician, and updates machine status.

---

## 6️⃣ Dashboard

### View Dashboard

**Method:** GET  
**Endpoint:**
```
/
```

**Description:**  
Displays the web dashboard showing machines, alerts, and technicians.

---
