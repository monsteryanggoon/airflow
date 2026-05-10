from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG
from common.common_func import get_sftp

import pendulum

with DAG(
    dag_id="dags_python_import_func",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 5, 1, tz="Asia/Seoul"),
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id='task_get_sftp',
        python_callable=get_sftp
    )

    task_get_sftp