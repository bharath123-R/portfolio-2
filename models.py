import mysql.connector
from flask import current_app


def get_connection():
    return mysql.connector.connect(
        host=current_app.config["MYSQL_HOST"],
        user=current_app.config["MYSQL_USER"],
        password=current_app.config["MYSQL_PASSWORD"],
        database=current_app.config["MYSQL_DB"]
        port=current_app.config["MYSQL_PORT"]
    )


def init_db(app):
    pass  # mysql-connector ku init thevai illa


def contact_add(name, email, message):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )

    conn.commit()

    cur.close()
    conn.close()