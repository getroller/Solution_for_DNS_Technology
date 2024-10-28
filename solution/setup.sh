#!/bin/bash

mkdir -p ./dags ./logs ./plugins ./config ./outputfiles

echo -e "AIRFLOW_UID=$(id -u)" > .env

docker compose up airflow-init

cp ./source/*.py ./dags/  
