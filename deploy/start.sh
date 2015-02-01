#!/bin/sh
source /home/www/MyXunta/bin/activate
/home/www/MyXunta/bin/gunicorn server:app --workers=2 -k gevent &
