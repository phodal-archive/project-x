#!/bin/sh
source /home/www/MyXunta/bin/activate
nohup /home/www/MyXunta/bin/gunicorn server:app -k gevent&
