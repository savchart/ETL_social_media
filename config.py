import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.getcwd(), 'airflow.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Airflow configuration
    AIRFLOW_HOME = os.environ.get('AIRFLOW_HOME') or os.path.join(os.getcwd(), 'airflow')
    DAGS_FOLDER = os.path.join(AIRFLOW_HOME, 'dags')
    PLUGINS_FOLDER = os.path.join(AIRFLOW_HOME, 'plugins')
    LOGS_FOLDER = os.path.join(AIRFLOW_HOME, 'logs')
    REST_API_PLUGIN_ENABLED = True
