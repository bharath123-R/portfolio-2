from flask_mysqldb import MySQL
mysql = MySQL()
def init_db(app):
    mysql.init_app(app)

def contact_add(name, email, message):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO contact(name, email, message) VALUES (%s,%s,%s)",(name, email, message))
    mysql.connection.commit()
    cur.close()

