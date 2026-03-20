import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def fetch_due_tasks():
    conn = psycopg2.connect(os.getenv("DB_URL"))
    cur = conn.cursor()

    cur.execute("""
        SELECT task_name, phone_number
        FROM routines
        WHERE active = true
    """)

    tasks = cur.fetchall()
    conn.close()
    return tasks
