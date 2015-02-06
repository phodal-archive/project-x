#X Project

[![Coverage Status](https://coveralls.io/repos/phodal/project-x/badge.svg?branch=master)](https://coveralls.io/r/phodal/project-x?branch=master)

start server
    
    gunicorn xunta.wsgi --log-file=xunta.log
    
test
    
    nosetests tests/*.py


test with coverage:

    nosetests --with-coverage --cover-erase --cover-package=xunta --cover-html

License

[待我代码编成，娶你为妻可好](http://www.xuntayizhan.com/person/ji-ke-ai-qing-zhi-er-shi-dai-wo-dai-ma-bian-cheng-qu-ni-wei-qi-ke-hao-wan/)

© 2015 [Phodal Huang](http://www.phodal.com). This code is distributed under the GPLv3 license.    