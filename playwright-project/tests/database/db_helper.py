import mysql.connector

class Database:
    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="playwright_db"
        )