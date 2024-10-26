from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.utils.dates import days_ago

# Определяем аргументы по умолчанию
default_args = {
    'owner': 'airflow',
    'retries': 1,
}

# Создаем экземпляр DAG
with DAG(
    dag_id='check_db_connection',
    default_args=default_args,
    description='DAG to check database connection',
    schedule_interval=None,  # Запуск только вручную
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Оператор для выполнения SQL-запроса
    check_connection = SQLExecuteQueryOperator(
        task_id='check_connection',
        conn_id='your_postgres_connection_id',  # Убедитесь, что это правильно настроено в Airflow
        sql="create table ANAL (id int);"  # Простой запрос для проверки соединения
    )

    check_connection
