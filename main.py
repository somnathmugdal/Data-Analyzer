from logger import log 
from flask import Flask, render_template, request
import mysql.connector


# log("Soma","Flask is Running")

app = Flask(__name__)

# @app.route('/home')
# Creating a route that has both GET and POST request methods
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST" :
        hostname = request.form.get('hostname')
        username = request.form.get('username')
        password = request.form.get('password')

        log("soma",f'Database Credentials \n Hostname : {hostname},Username : {username},Password : {password}')

        try :
            log("soma","Trying to connect database")
            mydb = mysql.connector.connect(
            host = hostname,
            user = username,
            password = password
        )
            log("soma",f"Database Connected Successfully ! \n {mydb}")
            return f"<h1>Database Connected Successfully ! \n {mydb}</h1>"
        except Exception as e :
            log("soma",e)
            return f"Facing an Error while connecting to the Database \n {e}"
        # return f'Hostname : {hostname},Username : {username},Password : {password}'
    return render_template('db_credentials_form.html')
# log("soma","page loaded sucessfully")

try :
    if __name__ == '__main__':
        app.run(debug=True)
except Exception as e:
    log("soma",e)