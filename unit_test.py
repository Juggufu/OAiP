import pytest
import sqlite3 as sq


class TestDataBase:
    @pytest.fixture
    def db_connection(self):
        db = sq.connect(':memory:')
        cur = db.cursor()
        cur.execute('''CREATE TABLE users (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        age INTEGER)''')
        db.commit()
        yield db
        db.close()

    def test_add_user(self, db_connection):
        cur = db_connection.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES ('Николай', 45)")
        db_connection.commit()
        cur.execute("SELECT * FROM users WHERE name='Николай'")
        user = cur.fetchone()
        assert user is not None

    def test_update_user_age(self, db_connection):
        cur = db_connection.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES ('Сава', 12)")
        db_connection.commit()
        cur.execute("UPDATE users SET age=13 WHERE name='Сава'")
        db_connection.commit()
        cur.execute("SELECT age FROM users WHERE name='Сава'")
        age = cur.fetchone()
        assert age[0] == 13

    def test_delete_user(self, db_connection):
        cur = db_connection.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES ('Сава', 12), ('Николай', 45), ('Алиса', 20)")
        db_connection.commit()
        cur.execute("DELETE FROM users WHERE name='Николай'")
        db_connection.commit()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        assert len(users) == 2

    def test_insert_multiple_users(self, db_connection):
        cur = db_connection.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES ('Сава', 12)")
        db_connection.commit()
        cur.execute("INSERT INTO users (name, age) VALUES ('Николай', 45)")
        db_connection.commit()
        cur.execute("INSERT INTO users (name, age) VALUES ('Михаил', 35)")
        db_connection.commit()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        assert len(users) == 3
