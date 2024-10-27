собираем докер образ из solution через test -task

используйте docker-compose up --build для сборки образа из test-task

делаем без gitignore



mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env


docker compose up airflow-init


если не хочется разворачивать готовые скрипты находятся в папке или резьтаты вывода




sudo apt-get update
sudo apt-get install build-essential совместимость

это обязательно добавить в mkdir  - ~/Solution_for_DNS_Technology/solution/outputfiles:/opt/airflow/outputfiles иначе прав не будет




