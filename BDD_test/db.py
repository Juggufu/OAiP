import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        self.conn.commit()

    def add_record(self, name, age):
        if not name:
            raise ValueError("Name cannot be empty")
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def get_all_records(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

    def edit_record(self, name, new_age):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET age=? WHERE name=?", (new_age, name))
        self.conn.commit()

    def delete_record(self, name):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM users WHERE name=?", (name,))
        self.conn.commit()
