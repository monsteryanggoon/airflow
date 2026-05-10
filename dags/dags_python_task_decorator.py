from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, task

import pendulum

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 5, 1, tz="Asia/Seoul"),
) as dag:

    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)

    python_task_1 = print_context('task decorator 실행')
