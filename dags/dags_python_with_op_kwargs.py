from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG
from common.common_func import regist2

import pendulum
import random

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 5, 1, tz="Asia/Seoul"),
) as dag:

    regist2_t1 = PythonOperator(
        task_id='regist2_t1',
        python_callable=regist2,
        op_args=['YG', 'man', 'kr', 'seoul'],
        op_kwargs={'email':'aaa@aaa.com', 'phone':'010-1234-5678'}
    )

    regist2_t1