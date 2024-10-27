from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from sqlalchemy import create_engine
import pandas as pd


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'provide_context': True
}

# Установите соединение с базой данных
connection_string = 'postgresql://getroller:getroller@dbget/getroller'
engine = create_engine(connection_string)



queries = {
    "query1": # 1.Общая сумма продаж по каждому продукту за последний квартал 2010 года
        """ with all_sales as (
                select productkey, coalesce(salesamount, 0::money) as salesamount 
                from factresellersales
                where orderdate >= '2010-10-01' and orderdate < '2011-01-01' 

                union all
                
                select productkey, coalesce(salesamount, 0::money) as salesamount
                from factinternetsales
                where orderdate >= '2010-10-01' and orderdate < '2011-01-01')   
            select  
                a.productkey,
                d.englishproductname,
                sum(a.salesamount) as total_sales
            from all_sales a
            join dimproduct d on a.productkey = d.productkey
            group by 1, 2
            order by total_sales desc; """,


    "query2" : # 2.Список всех клиентов, которые сделали покупку в интернет-магазине в течение первого полугодия 2013 года
        """ select distinct 
                f.customerkey,
                d.firstname,
                d.lastname 
            from factinternetsales f 
            join dimcustomer d on f.customerkey = d.customerkey 
            where f.orderdate >= '2013-01-01' and f.orderdate < '2013-07-01'
            order by 1; """,


    "query3": # 3.Список всех продавцов, которые продали больше 1000 единиц продукта за 2 квартал 2012 года
        """ select f.employeekey, 
                    d.firstname, 
                    d.lastname, 
                    sum(f.orderquantity) as total_q2_2012
            from factresellersales f
            join dimemployee d on f.employeekey = d.employeekey
            where f.orderdate >= '2012-04-01' and f.orderdate < '2012-07-01'
            group by 1, 2, 3
            having sum(f.orderquantity) > 1000
            order by total_q2_2012 desc; """,


    "query4": # 4.Кумулятивная сумма продаж по любой из категорий за все время
        """ with all_sales as (
                select productkey, orderquantity, coalesce(salesamount, 0::money) as salesamount, orderdate 
                from factresellersales
                
                union all
                
                select productkey, orderquantity, coalesce(salesamount, 0::money) as salesamount, orderdate
                from factinternetsales) 
            select 
                a.productkey,
                a.orderquantity, 
                a.salesamount,                     
                dp.productcategorykey, 
                sum(a.salesamount) over (
                    partition by dp.productcategorykey
                    order by a.orderdate, a.productkey
                    rows between unbounded preceding and current row) as cumulative_sales,
                a.orderdate
            from all_sales a
            join dimproduct d on a.productkey = d.productkey
            join dimproductsubcategory dp on d.productsubcategorykey = dp.productsubcategorykey
            where dp.productcategorykey = 1  
            order by cumulative_sales; """ # Можно выбрать любую категорию из 4             
}


def extract_data(**kwargs):
    ti = kwargs['ti']
    all_data = {}
    for title, query in queries.items():
        df = pd.read_sql(query, engine)
        all_data[title] = df
    ti.xcom_push(key='all_data', value=all_data)  # Пушим весь словарь в XCom

def process_data(**kwargs):
    ti = kwargs['ti']
    all_data = ti.xcom_pull(key='all_data', task_ids='extract_data_task')  # Замените 'extract_data_task' на ID вашей задачи
    # all_data теперь будет словарем DataFrame
    for title, df in all_data.items():
        # Обработка каждого DataFrame
        df.to_csv(f'/opt/airflow/outputfiles/{title}.csv', index=False)  # Пример сохранения в CSV





with DAG('sql_extract_outrrrrr', default_args=default_args, schedule=None, catchup=False) as dag:
    
    extract_data_task = PythonOperator(
        task_id='extract_data_task',
        python_callable=extract_data
    )

    save_to_csv_task = PythonOperator(
        task_id='save_to_csv_task',
        python_callable=process_data
    )

    extract_data_task >> save_to_csv_task  
