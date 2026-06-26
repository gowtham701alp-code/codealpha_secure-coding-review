import sqlite3

# Hardcoded database connection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

print("=== User Login System ===")

username = input("Enter Username: ")
password = input("Enter Password: ")

# Vulnerable SQL Query (SQL Injection)
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

try:
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Login Successful")
    else:
        print("Invalid Username or Password")

except Exception as e:
    print("Database Error:", e)

conn.close()
