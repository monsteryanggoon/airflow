from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

import pendulum

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 5, 1, tz="Asia/Seoul"),
) as dag:
    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
    )

    t2_avocado = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO",
    )

    t1_orange >> t2_avocado