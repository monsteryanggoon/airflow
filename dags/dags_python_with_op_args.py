from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG
from common.common_func import regist

import pendulum
import random

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 5, 1, tz="Asia/Seoul"),
) as dag:

    regist_t1 = PythonOperator(
        task_id='regist_t1',
        python_callable=regist,
        op_args=['YG', 'man', 'kr', 'seoul']
    )

    regist_t1