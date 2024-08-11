from airflow.utils.email import send_email

def send_notification_email(message, subject="Airflow Alert", to=["example@example.com"]):
    send_email(to, subject, message)