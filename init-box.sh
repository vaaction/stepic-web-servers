#!/usr/bin/env bash
#sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo gunicorn ask.wsgi -c etc/gunicorn_ask.conf.py --chdir /home/ibukanov/IdeaProjects/stepic-web-servers/ask
#sudo /etc/init.d/mysql start