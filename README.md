# Тестовое задание DNS Technology

## Описание

Доступны два варианта решений:

[1 вариант] Если не хотите ничего разворачивать и требуются только сырые скрипты (располагается в папке raw_scripts) 

[2 вариант] Для решения задач используются docker compose и Airflow (располагается в папке solution) (RECOMMENDED)

---

## Начало работы

1. Чтобы начать, клонируйте репозиторий:

```bash
git clone https://github.com/getroller/Solution_for_DNS_Technology.git
```
2. В корне репозитория, необходимо установить окружение:

```bash
python -m venv venv 
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

---

## [1 вариант] Если требуются только скрипты

1. Перейдите в папку raw_scripts/

2. Соберите образ Docker: 
```bash
docker build ../test-task -t dwh-test
```

3. Запустите контейнер Docker: 
```bash
docker run --rm --name dwh-test -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test -e POSTGRES_DB=test -p 5557:5432 -d dwh-test
```

4. Все готово, запускайте скрипты!

---

## [2 вариант] Полный запуск (RECOMMENDED)

1. Перейдите в папку solution/

2. Сделайте скрипт setup.sh исполняемым: 
```bash
chmod +x setup.sh
```

3. Запустите скрипт для подготовки окружения: 
```bash
./setup.sh
```

4. Соберите и запустите контейнеры с помощью Docker Compose (Ожидание запуска ~3 min):
```bash
docker-compose up --build -d 
```

5. Все готово!   
Переходите на localhost:8080 и запускайте DAG's  
Результат 1 задания будет отображен в логах Airflow  
Результат 2 задания приходит в папку solution/outputfiles  

---

## Дополнительная информация
Все полностью автоматизированно, ничего дополнительно настраивать не нужно








