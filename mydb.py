import pymysql

# connect to the database
dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="elderco",
    autocommit=True
)

# create a cursor object
cursor = dataBase.cursor()

# drop the database if it already exists
cursor.execute("DROP DATABASE IF EXISTS elderco")

# create the database
cursor.execute("CREATE DATABASE elderco")

print("ALL Done!")
