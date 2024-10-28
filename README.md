# Тестовое задание 

## Описание

Доступны два варианта решений:

[1 вариант] находится в папке raw_scripts (Если не хотите ничего разворачивать)

[2 вариант] находится в папке solution (Используется docker compose, написаны Dags под решение каждой задачи)

---

## Начало работы

Чтобы начать, клонируйте репозиторий:

```bash
git clone https://github.com/getroller/Solution_for_DNS_Technology.git
```

---

## 1 вариант (Если вы не хотите ничего разворачивать и вам требуются только скрипты) выполните следующие шаги: 

1. Перейдите в папку raw_scripts

2. Собрать образ Docker: 
```bash
docker build ../test-task -t dwh-test
```

3. Запустить контейнер Docker: 
```bash
docker run --rm --name dwh-test -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test -e POSTGRES_DB=test -p 5557:5432 -d dwh-test
```

---

## [2 вариант] Полный запуск

1. Перейдите в папку solution.

2. Сделайте скрипт setup.sh исполняемым: 
```bash
chmod +x setup.sh
```

3. Запустите скрипт для установки зависимостей и подготовки окружения: 
```bash
./setup.sh
```

4. Соберите и запустите все контейнеры с помощью Docker Compose:
bash``` 
docker-compose up --build -d 
```

---

## Дополнительная информация
Все работает автоматически ничего настраивать не нужно








