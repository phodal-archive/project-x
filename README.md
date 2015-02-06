#X Project

start server
    
    gunicorn xunta.wsgi --log-file=xunta.log
    
test
    
    nosetests tests/*.py
    
License

[待我代码编成，娶你为妻可好](http://www.xuntayizhan.com/person/ji-ke-ai-qing-zhi-er-shi-dai-wo-dai-ma-bian-cheng-qu-ni-wei-qi-ke-hao-wan/)

© 2015 [Phodal Huang](http://www.phodal.com). This code is distributed under the GPLv3 license.    