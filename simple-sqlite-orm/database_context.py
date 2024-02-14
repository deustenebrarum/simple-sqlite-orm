import sqlite3
from os import path
from .table import Table


class DBContext:
    class DBError(Exception):
        pass

    def __init__(self, file_dir: str, file_name: str) -> None:
        file_path = path.join(file_dir, file_name)

        self._connection = sqlite3.connect(file_path)
        self._cursor = self._connection.cursor()

    def commit(self):
        self._connection.commit()

    def execute(self, query: str) -> None:
        try:
            self._cursor.execute(query)
        except sqlite3.OperationalError as e:
            raise self.DBError(e)

    def getAll(self):
        return self._cursor.fetchall()

    def getOne(self):
        return self._cursor.fetchone()

    def createTable(
        self, name: str, model,
        columns: dict[str, str],
        table_options: str
    ):
        return Table(self, name, model, columns, table_options)
