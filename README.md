# DRF Posts Project & Bot

## Setting up DRF Project
____
First build Dockerfile:

`cd task_prj/`

`docker-compose up --build`

Then run migrations:

`docker exec -it proj_web_1 bash`

`python manage.py makemigrations`

`python manage.py migrate`


## Running bot

First you need to install `requirements.txt` in the root directory:

`pip install -r requirements.txt`

Launching bot:

`cd bot/`

`python bot.py`

### Changing configuration

You can change `users_amount`, `max_posts_per_user` and `max_likes_per_user` in `conf.py` file
