import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(self.logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_circle(self):
        sql = """
        CREATE TABLE IF NOT EXISTS circle (
            id INTEGER PRIMARY KEY,
            circle_days TEXT NOT NULL,
            circle_name TEXT NOT NULL,
            circular_science TEXT NOT NULL,
            science_teacher TEXT NOT NULL,
            start_time TEXT NOT NULL,
            finish_time TEXT NOT NULL
        )
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_circle(self, id: int, circle_days: str, circle_name: str, circular_science: str,
                   science_teacher: str, start_time: str, finish_time: str):
        sql = """INSERT INTO circle (id, circle_days, circle_name, circular_science, science_teacher,
        start_time, finish_time) VALUES (?,?,?,?,?,?,?)"""
        self.execute(sql, parameters=(
            id, circle_days, circle_name, circular_science, science_teacher, start_time, finish_time), commit=True)

    def select_all_circle(self):
        sql = """
        SELECT * FROM circle
        """
        return self.execute(sql, fetchall=True)

    def select_circle(self, id: int):
        sql = f"SELECT * FROM circle WHERE id={id}"
        return self.execute(sql, fetchone=True)

    def delete_circle_by_id(self, id):
        self.execute(f"DELETE FROM circle WHERE id={id}", commit=True)

    def logger(self, statement):
        print(f"""
        Executing:
        {statement}
        """)


class Database2:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(self.logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_student_info(self):
        sql = """
        CREATE TABLE IF NOT EXISTS student_info (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_student(self, id: int):
        sql = f"SELECT * FROM student_info WHERE id={id}"
        return self.execute(sql, fetchone=True)

    def select_all_student(self):
        sql = """
        SELECT * FROM student_info
        """
        return self.execute(sql, fetchall=True)

    def add_student(self, id: int, student: str):
        sql = """INSERT INTO student_info (id, username) VALUES (?,?)"""
        self.execute(sql, parameters=(id, student), commit=True)

    def logger(self, statement):
        print(f"""
        Executing:
        {statement}
        """)
