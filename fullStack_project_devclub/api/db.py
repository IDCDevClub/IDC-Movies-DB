import sqlite3
from typing import List, Dict

DB_NAME = "movies.db"


class SQLiteConnection:
    def __init__(self):
        self._connection = None
        self.init_favorites_table()

    def execute_command(self, command, get=False):
        fetchall = None
        try:
            self._connection = sqlite3.connect(DB_NAME)
            cursor = self._connection.cursor()
            print("Connected to SQLite")

            cursor.execute(command)
            if get:
                fetchall = cursor.fetchall()
            print("executed")
            self._connection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            if self._connection:
                self._connection.close()
                print("The SQLite connection is closed")
        return fetchall

    def init_favorites_table(self):
        command = """CREATE TABLE if not exists add_to_favorites (
        id INTEGER PRIMARY KEY,
        imdbID INTEGER,
        title VARCHAR(20)
        );"""
        self.execute_command(command)

    def save_to_favorites(self, movie: dict):
        values = (movie['movie_title'], movie['imdbID'])
        command = f"""INSERT INTO add_to_favorites
                  (title, imdbID) 
                   VALUES
                  {values}"""
        self.execute_command(command)

    def get_list_of_favorites(self) -> List[Dict]:
        command = f"""SELECT imdbID, title FROM add_to_favorites;"""
        fetchall = self.execute_command(command, True)
        return [{"imdbID": row[0], "title": row[1]} for row in fetchall]
