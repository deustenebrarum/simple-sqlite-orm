from .base_column import Column


# class TableMeta:
#     def __prepare__(cls, name, bases, **kwargs):


#     def __new__(cls, name, bases, attrs):
#         _object = super().__new__(cls, name, bases, attrs)

#         return _object

class Table:
    @classmethod
    def _get_columns(cls):
        columns = {
            key: value
            for key, value in vars(cls).items()
            if isinstance(value, Column)
        }

        return columns

    @property
    def columns(self):
        return list(self._get_columns().values())

    @classmethod
    def create_model(cls):
        class Model:
            def __init__(self, *args):
                for column, value in zip(cls._get_columns().values(), args):
                    setattr(self, column.name, value)

            def as_dict(self):
                return {
                    column.name: getattr(self, column.name)
                    for column in cls._get_columns().values()
                }

        return Model

    def __init__(
        self, db, name: str,
        other_options: tuple = None,
    ) -> None:
        self.db = db
        self.name = name

        for name, column in self._get_columns().items():
            column.set_name_if_not_set(name)

        self.model = self.create_model()

        creation_query = f'''
            CREATE TABLE IF NOT EXISTS {self.name}
            (
                {', '.join(
                    column.sql_string
                    for column in self.columns
                )}
                {
                    ', ' + ', '.join(other_options)
                    if other_options is not None
                    else ''
                }
            );
        '''

        self.db.execute(creation_query)

    @staticmethod
    def _sqlValueByType(value):
        if value is None:
            return 'NULL'

        if isinstance(value, str):
            return f"'{value}'"

        return value

    def getBy(self, column: Column, value: str):
        self.db.execute(f'''
            SELECT * FROM {self.name}
            WHERE {column.name} = '{self._sqlValueByType(value)}';
        ''')
        return self.model(*self.db.getOne())

    def get(self, id: int):
        return self.getBy(self.id, id)

    def getAll(
        self, filter: str = None,
        limit: int = None, offset: int = None
    ):
        query = f'SELECT * FROM {self.name}'

        if filter is not None:
            query += f' WHERE {filter}'

        if limit is not None:
            query += f' LIMIT {limit}'

        # пропустить столько то строк и начать с них
        if offset is not None:
            query += f' OFFSET {offset}'

        self.db.execute(query)

        for row in self.db._cursor.fetchall():
            yield self.model(*row)

    def insert(self, modelObject):
        columns = [column.name for column in self.columns]
        self.db.execute(f'''
            INSERT INTO {self.name}
            ({', '.join(columns)})
            VALUES (
                {', '.join(
                    f"{self._sqlValueByType(value)}"
                    for value in modelObject.as_dict().values()
                )}
            )
        ''')

        self.db.commit()

        createdObject = self.getBy(self.id, self.db._cursor.lastrowid)

        return createdObject

    def delete(self, id: int):
        objectToDelete = self.get(id)

        self.db.execute(f'''
            DELETE FROM {self.name} WHERE id = {id};
        ''')

        self.db.commit()

        return objectToDelete

    def update(self, modelObject):
        self.db.execute(f'''
            UPDATE {self.name}
            SET
                {', '.join(
                    f'{name} = "{value}"' for name, value
                    in modelObject.as_dict().items()
                )}
            WHERE id = {modelObject.id};
        ''')

        self.db.commit()

        return self.get(modelObject.id)
