from datetime import datetime, timedelta

from airflow import DAG
from plugins.operators.data_aggregation_operator import DataAggregationOperator

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
    'data_aggregation',
    default_args=default_args,
    description='Aggregate data',
    schedule_interval=timedelta(days=1),
)

aggregation_task = DataAggregationOperator(
    task_id='data_aggregation',
    dag=dag,
)

aggregation_task
