собираем докер образ из solution через test -task

используйте docker-compose up --build для сборки образа из test-task

делаем без gitignore



mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env


docker compose up airflow-init


если не хочется разворачивать готовые скрипты находятся в папке или резьтаты вывода