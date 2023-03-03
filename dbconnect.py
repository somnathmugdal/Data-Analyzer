from logger import log
import mysql.connector

localhost =  ""
username  = ""
password = ""

log("soma","Trying to connect database")
try:
    mydb = mysql.connector.connect(
        host = localhost,
        user = username,
        password = password
    )
except Exception as e :
    log("soma",e)


print("Database Connected ! ", mydb)