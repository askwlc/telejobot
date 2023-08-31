## telejobot

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/)

Бот позволяет парсить сообщения и фильтровать по заданным параметрам с каналов о работе и пересылать их в личные сообщения. 

### Развернуть проект на удаленном сервере:

- Клонировать репозиторий:

```
git clone https://github.com/askwlc/telejobot
```

- Собрать контейнер:

```
docker build -t your_dockerhub_username/telejobot:latest .
```

- Создать файл env:

```
api_id=
api_hash=
```

- Установить на сервере Docker:

```
sudo apt update                                         # установка обновлений
sudo apt upgrade -y
sudo apt install docker.io                              # установка Докер

```

- Скопировать на сервер контейнер docker (удобнее через dockerhub) и файл env:

```
docker pull your_dockerhub_username/telejobot:latest
scp .env user@your_vps_ip:/path/to/your/project/
```

- Запустить контейнер:

```
docker run --env-file .env telejobot
```
