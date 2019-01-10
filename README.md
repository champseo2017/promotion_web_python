# promotion_web_python
promotion_web_python <br>
django with python <br>
py manage.py runserver 0.0.0.0:8000 <br>

error mysqldb module <br>
pip install pymysql <br>
Then, edit the __init__.py file in your project origin dir(the same as settings.py) <br>
 
add:  <br>
import pymysql <br>
pymysql.install_as_MySQLdb() <br>

