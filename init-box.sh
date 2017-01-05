#!/usr/bin/env bash
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo gunicorn ask.wsgi -c ../../etc/gunicorn_ask.conf.py
sudo gunicorn hello:app -c etc/gunicorn.conf.py &
#sudo /etc/init.d/mysql start