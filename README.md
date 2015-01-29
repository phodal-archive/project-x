#X Project

start server
    
    gunicorn server:app
    
test
    
    nosetests tests/*.py