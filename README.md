#X Project

一个以WordPress作为编辑，Falcon + Peewee作为发布的项目。

> A project basis on WordPress as Editing, Falcon as Publishing.

start server
    
    gunicorn server:app
    
test
    
    nosetests tests/*.py