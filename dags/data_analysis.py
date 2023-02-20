from datetime import datetime, timedelta

from airflow import DAG
from plugins.operators.data_analysis_operator import DataAnalysisOperator

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
    'data_analysis',
    default_args=default_args,
    description='Perform data analysis',
    schedule_interval=timedelta(days=1),
)

analysis_task = DataAnalysisOperator(
    task_id='data_analysis',
    dag=dag,
)

analysis_task
