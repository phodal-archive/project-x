#!/bin/sh
source /home/www/MyXunta/bin/activate
nohup gunicorn xunta.wsgi --log-file=xunta.log --workers=2 -k gevent
