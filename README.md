# DRF Posts Project & Bot

## Setting up DRF Project
____
First build Dockerfile:

`cd task_proj/`

`docker-compose up --build`

Then run migrations:

`docker exec -it proj_web_1 bash`

`python manage.py makemigrations`

`python manage.py migrate`


## Running bot

First you need to install `requirements.txt` in the root directory:

`pip install -r requirements.txt`

NOTE! You have to run bot, while main app is working!!!

Launching bot:

`cd bot/`

`python bot.py`

### Changing configuration

You can change `MAX_USERS`, `MAX_POSTS` and `MAX_LIKES` in `conf.py` file
