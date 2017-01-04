#!/usr/bin/env bash
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo gunicorn -c etc/gunicorn_ask.conf.py /home/box/web/ask ask.wsgi:application
sudo gunicorn hello:app -c etc/gunicorn.conf.py &
#sudo /etc/init.d/mysql start