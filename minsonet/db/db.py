import sqlite3


class DB:
    def __init__(self, location):
        self.location = location

    def get_connection(self):
        print(f"DB.connect - location: {self.location}")
        connection = sqlite3.connect(self.location)
        return connection

    def close(self, connection):
        print("DB.close")
        connection.close()

    def rollback(self, connection):
        print("DB.rollback")
        connection.rollback()

    def execute(self, stmt):
        print(f"execute - stmt: {stmt}")

        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(stmt)
            connection.commit()
            lastrowid = cursor.lastrowid
        finally:
            self.close(connection)

        return lastrowid

    def fetchone(self, stmt):
        print(f"fetchOne - stmt: {stmt}")
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            result = cursor.execute(stmt).fetchone()
            return result
        finally:
            self.close(connection)

    def fetchall(self, stmt):
        print(f"fetchAll - stmt: {stmt}")
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            result = cursor.execute(stmt).fetchall()
            return result
        finally:
            self.close(connection)
