from airflow import DAG # type: ignore
from airflow.operators.python import PythonOperator # type: ignore
from datetime import datetime
from services.whatsapp_notifier import send_whatsapp # type: ignore
from db.fetcher import fetch_due_tasks # type: ignore

def notify():
    tasks = fetch_due_tasks()
    for task, phone in tasks:
        send_whatsapp(phone, task)

with DAG(
    dag_id="routine_whatsapp_notifier",
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/1 * * * *",  # every minute
    catchup=False
) as dag:

    notify_task = PythonOperator(
        task_id="send_whatsapp_notifications",
        python_callable=notify
    )
