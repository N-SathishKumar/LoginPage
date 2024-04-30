#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
import mysql.connector

print("Content-Type:text/html")
print()
import cgi

form = cgi.FieldStorage()


# Creating connection object
def connect_to_database():
    """Connects to the MySQL database."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="userlogin"
    )
    return conn


def login(uname, pwd):
    """Logs in the user to the database."""
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registration WHERE uname=%s AND pwd=%s", (uname, pwd))
    user = cursor.fetchone()
    if user is not None:
        return True
    else:
        return False

def main():
    """The main function."""
    uname = form.getvalue("uname")
    pwd = form.getvalue("pwd")
    if login(uname, pwd):
        print("<h1>Login successful!</h1>")
    else:
        print("<h1>Login failed!</h1>")

if __name__ == "__main__":
    main()