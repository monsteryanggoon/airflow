from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, task

import pendulum

with DAG(
    dag_id="dags_python_with_xcom_eg2",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 5, 1, tz="Asia/Seoul"),
) as dag:
    
    @task(task_id='python_xcom_push_by_return')
    def xcom_push_result(**context):
        return 'Success'

    @task(task_id='python_xcom_pull_1')
    def xcom_pull_1(**context):
        ti = context['ti']
        value1 = ti.xcom_pull(task_ids='python_xcom_push_by_return')

        print('xcom_pull 메서드로 직접 찾은 리턴 값: ' + value1)

    @task(task_id='python_xcom_pull_2')
    def xcom_pull_2(status, **context):
        print('함수 입력값으로 받은 값: ' + status)

    python_xcom_push_by_return = xcom_push_result()
    xcom_pull_2(python_xcom_push_by_return)
    python_xcom_push_by_return >> xcom_pull_1()
    