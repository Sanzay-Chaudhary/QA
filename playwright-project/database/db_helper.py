import mysql.connector

class Database:
    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="company",
            port=3306,
            use_pure=True   # <-- Important
        )