#!/bin/sh
gunicorn server:app --workers=2 -k gevent