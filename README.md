==============WhatsApp Routine Notifier (Airflow + Docker + Postgres)==========================
A Python-based automation system that sends WhatsApp reminders (like “drink water”, “take a break”, etc.) based on scheduled routines.

This project uses:

Apache Airflow for scheduling workflows

PostgreSQL for storing routine data

Docker Compose for easy local setup 

====================Features=====================================
Schedule daily routines (e.g., drink water, walk, study)

Send WhatsApp notifications automatically

Store and manage routines in PostgreSQL

Dynamic fetching of tasks based on time

Fully containerized using Docker Compose

======================Architecture=====================================
User Input → PostgreSQL → Airflow DAG → Python Script → WhatsApp Notification

PostgreSQL stores routine tasks

Airflow Scheduler triggers DAGs at defined intervals

Python scripts fetch tasks and send WhatsApp messages

========================Prerequisites======================================
Make sure you have installed:

Docker Desktop (Windows/Mac/Linux)

Docker Compose (comes with Docker Desktop)

Python (if running scripts locally outside Docker)

======================Setup Instructions====================================
1. Clone the repository
git clone https://github.com/python-automation-playground/python-automation-playground
cd whatsapp_routine_notifier
2. Start services using Docker
docker compose up -d --build

This will start:

Airflow Webserver (Port: 8080)

Airflow Scheduler

PostgreSQL database

3. Access Airflow UI

Open browser and go to:

http://localhost:8080

Default login (if not changed):

Username: admin
Password: admin
4. Enable DAG

Go to Airflow UI

Locate your DAG (routine_notifier_dag)

Turn it ON

================================How It Works================================
Routines are stored in PostgreSQL with:
task_name
phone_number
active

Airflow DAG runs at a defined interval

Python script: Fetches tasks matching current time

Sends WhatsApp notification
