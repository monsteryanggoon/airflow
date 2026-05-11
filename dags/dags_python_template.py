from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, get_current_context, task

import pendulum

with DAG(
    dag_id="dags_python_template",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2026, 5, 1, tz="Asia/Seoul"),
) as dag:
    
    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)

    python_t1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_function1,
        op_kwargs={
            'start_date':'{{ data_interval_start | ds }}',
            'end_date':'{{ data_interval_end | ds }}',
        }
    )

    @task(task_id="python_task_2")
    def python_function2():
        context = get_current_context()
        print(context)
        print('ds:' + context['ds'])
        print('ts:' + context['ts'] )
        print('data_interval_start: ' + str(context['data_interval_start']))
        print('data_interval_end: ' + str(context['data_interval_end']))
        print('task_instance: ' + str(context['ti']))


    python_t1 >> python_function2()