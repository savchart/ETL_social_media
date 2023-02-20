import os
from airflow import DAG
from airflow.operators.sensors import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

class FileSensor(BaseSensorOperator):
    """
    Custom sensor that checks if a file exists in a given directory
    """
    @apply_defaults
    def __init__(self, directory, file_pattern, *args, **kwargs):
        self.directory = directory
        self.file_pattern = file_pattern
        super().__init__(*args, **kwargs)

    def poke(self, context):
        files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
        for file in files:
            if self.file_pattern in file:
                return True
        return False

dag = DAG(
    dag_id='file_sensor_dag',
    default_args=default_args,
    schedule_interval='@daily'
)

file_sensor_task = FileSensor(
    task_id='file_sensor_task',
    directory='/path/to/directory',
    file_pattern='*.csv',
    dag=dag
)
