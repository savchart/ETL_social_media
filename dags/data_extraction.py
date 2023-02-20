from datetime import datetime, timedelta

from airflow import DAG

from plugins.operators.telegram_operator import TelegramOperator
from plugins.operators.discord_operator import DiscordOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_extraction',
    default_args=default_args,
    description='Extract data from Telegram and Discord',
    schedule_interval=timedelta(days=1),
)

telegram_task = TelegramOperator(
    task_id='telegram_extraction',
    channel='my_channel',
    api_key='my_api_key',
    api_secret='my_api_secret',
    dag=dag,
)

discord_task = DiscordOperator(
    task_id='discord_extraction',
    server='my_server',
    channel='my_channel',
    token='my_token',
    dag=dag,
)

telegram_task >> discord_task
