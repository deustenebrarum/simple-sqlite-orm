from .base_column import Column


class IdColumn(Column):
    def __init__(self, name: str = 'id'):
        super().__init__(
            name,
            'INTEGER',
            python_type=int,
            primary_key=True
        )


class IntegerColumn(Column):
    def __init__(
        self, name: str = None,
        is_nullable: bool = False,
        default_value: str = None,
        unique: bool = False,
        checks: str = None,
        other_options: str = None
    ):
        super().__init__(
            name,
            'INTEGER',
            python_type=int,
            is_nullable=is_nullable,
            default_value=default_value,
            unique=unique,
            checks=checks,
            other_options=other_options
        )


class TextColumn(Column):
    def __init__(
        self, name: str = None,
        is_nullable: bool = False,
        default_value: str = None,
        unique: bool = False,
        checks: str = None,
        other_options: str = None
    ):
        super().__init__(
            name,
            'TEXT',
            python_type=str,
            is_nullable=is_nullable,
            default_value=default_value,
            unique=unique,
            checks=checks,
            other_options=other_options
        )


class NumericColumn(Column):
    def __init__(
        self, name: str = None,
        is_nullable: bool = False,
        default_value: str = None,
        unique: bool = False,
        checks: str = None,
        other_options: str = None
    ):
        super().__init__(
            name,
            'NUMERIC',
            python_type=float,
            is_nullable=is_nullable,
            default_value=default_value,
            unique=unique,
            checks=checks,
            other_options=other_options
        )


class RealColumn(Column):
    def __init__(
        self, name: str = None,
        is_nullable: bool = False,
        default_value: str = None,
        unique: bool = False,
        checks: str = None,
        other_options: str = None
    ):
        super().__init__(
            name,
            'REAL',
            python_type=float,
            is_nullable=is_nullable,
            default_value=default_value,
            unique=unique,
            checks=checks,
            other_options=other_options
        )


class BooleanColumn(Column):
    def __init__(
        self, name: str = None,
        is_nullable: bool = False,
        default_value: str = None,
        unique: bool = False,
        checks: str = None,
        other_options: str = None
    ):
        super().__init__(
            name,
            'BOOLEAN',
            python_type=bool,
            is_nullable=is_nullable,
            default_value=default_value,
            unique=unique,
            checks=checks,
            other_options=other_options
        )


class DateTimeColumn(Column):
    def __init__(
        self, name: str = None,
        is_nullable: bool = False,
        default_value: str = None,
        unique: bool = False,
        checks: str = None,
        other_options: str = None
    ):
        super().__init__(
            name,
            'DATETIME',
            python_type=str,
            is_nullable=is_nullable,
            default_value=default_value,
            unique=unique,
            checks=checks,
            other_options=other_options
        )


class DateColumn(Column):
    def __init__(
        self, name: str = None,
        is_nullable: bool = False,
        default_value: str = None,
        unique: bool = False,
        checks: str = None,
        other_options: str = None
    ):
        super().__init__(
            name,
            'DATE',
            python_type=str,
            is_nullable=is_nullable,
            default_value=default_value,
            unique=unique,
            checks=checks,
            other_options=other_options
        )
