#!/bin/bash

mkdir -p ./dags ./logs ./plugins ./config ./outputfiles

echo -e "AIRFLOW_UID=$(id -u)" > .env

cp ./source/*.py ./dags/  
