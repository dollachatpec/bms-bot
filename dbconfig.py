
from mysql.connector import (connection)
import os


user = "admin"
password = "&PEC181183"
dbname = "site"
hostname = "ec2-54-255-152-30.ap-southeast-1.compute.amazonaws.com"
port = 3306
def dbcon():
    cnx = connection.MySQLConnection(user=user, password=password,
                                     host=hostname,
                                    database=dbname,
                                    port=port)
    return cnx