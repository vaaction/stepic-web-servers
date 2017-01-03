#!/usr/bin/env bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo gunicorn hello:app -c etc/gunicorn.conf.py
#sudo /etc/init.d/mysql start