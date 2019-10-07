from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('sonder',
          default_args=default_args,
          schedule_interval=timedelta(days=1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(task_id='t1', bash_command='sleep 60', dag=dag)

t2 = BashOperator(task_id='t2', bash_command='sleep 60', dag=dag)

t3 = BashOperator(task_id='t3', bash_command='sleep 10', dag=dag)

t4 = BashOperator(task_id='t4', bash_command='sleep 10', dag=dag)

t5 = BashOperator(task_id='t5', bash_command='sleep 60', dag=dag)

t6 = BashOperator(task_id='t6', bash_command='sleep 60', dag=dag)

t7 = BashOperator(task_id='t7', bash_command='sleep 60', dag=dag)

t8 = BashOperator(task_id='t8', bash_command='sleep 60', dag=dag)

t9 = BashOperator(task_id='t9', bash_command='sleep 60', dag=dag)

t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8 >> t9
