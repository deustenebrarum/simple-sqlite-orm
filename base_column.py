class Column:
    def __init__(
        self,
        name: str, _type: str,
        python_type: type = object,
        primary_key: bool = False,
        is_nullable: bool = False,
        default_value: str = None,
        unique: bool = False,
        checks: str = None,
        other_options: str = None
    ) -> None:
        self._python_type = python_type
        self._name = name
        self._type = _type

        self.primary_key = primary_key
        self.is_nullable = is_nullable
        self.default_value = default_value
        self.unique = unique
        self.checks = checks
        self.other_options = other_options

        self._sql_string = None

    @property
    def sql_string(self):
        if self._sql_string is not None:
            return self._sql_string

        self._sql_string = f'{self._name} {self._type}'

        if self.primary_key:
            self._sql_string += ' PRIMARY KEY AUTOINCREMENT'

        if not self.is_nullable:
            self._sql_string += ' NOT NULL'

        if self.default_value is not None:
            self._sql_string += f' DEFAULT {self.default_value}'

        if self.unique:
            self._sql_string += ' UNIQUE'

        if self.checks is not None:
            self._sql_string += f' CHECK ({self.checks})'

        if self.other_options is not None:
            self._sql_string += f' {self.other_options}'

        return self._sql_string

    @property
    def python_type(self):
        return self._python_type

    @property
    def name(self):
        return self._name

    def set_name_if_not_set(self, name):
        if self._name is None:
            self._name = name

    @property
    def type(self):
        return self._type
