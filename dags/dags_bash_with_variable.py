from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, Variable

import pendulum

with DAG(
    dag_id="dags_bash_with_variable",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 5, 1, tz="Asia/Seoul"),
) as dag:
    var_value = Variable.get("simple_key")
    
    bash_var_1 = BashOperator(
        task_id="bash_var_1",
        bash_command=f"echo variable:{var_value}",
    )

    bash_var_2 = BashOperator(
        task_id="bash_var_2",
        bash_command="echo variable:{{var.value.sample_key}}",
    )