# Тестовое задание 

## Описание

Доступны два варианта решений:

[1 вариант] находится в папке raw_scripts (Если не хотите ничего разворачивать и требуются только сырые скрипты) 

[2 вариант] находится в папке solution (Для решения задач используются docker compose и Airflow)

---

## Начало работы

1. Чтобы начать, клонируйте репозиторий:

```bash
git clone https://github.com/getroller/Solution_for_DNS_Technology.git
```
2. В корне репозитория, необходимо установить зависимоти

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

## [1 вариант] Если требуются только сырые скрипты

1. Перейдите в папку raw_scripts

2. Соберите образ Docker: 
```bash
docker build ../test-task -t dwh-test
```

3. Запустите контейнер Docker: 
```bash
docker run --rm --name dwh-test -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test -e POSTGRES_DB=test -p 5557:5432 -d dwh-test
```

---

## [2 вариант] Полный запуск

1. Перейдите в папку solution

2. Сделайте скрипт setup.sh исполняемым: 
```bash
chmod +x setup.sh
```

3. Запустите скрипт для подготовки окружения: 
```bash
./setup.sh
```

4. Соберите и запустите контейнеры с помощью Docker Compose:
```bash
docker-compose up --build -d 
```

---

## Дополнительная информация
Все автоматизированно, ничего дополнительно настраивать не нужно








