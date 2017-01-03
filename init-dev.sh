#!/usr/bin/env bash
sudo ln -s /home/ibukanov/IdeaProjects/stepic-web-servers/etc/nginx.conf  /etc/nginx/sites-enabled/nginx.conf
sudo /etc/init.d/nginx restart
sudo gunicorn3 hello:app -c etc/gunicorn.conf.py
#sudo /etc/init.d/mysql start