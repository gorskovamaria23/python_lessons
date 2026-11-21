from sqlalchemy import create_engine, text


class StudentTable:
    __scripts = {
        "insert": text("INSERT INTO students (name, email) "
                       "VALUES (:name, :email)"),
        "delete": text("DELETE FROM students WHERE email = :email"),
        "select_by_email": text("SELECT * FROM students WHERE email = :email"),
        "update_name": text("UPDATE students SET name = :name WHERE email = :email")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, name, email):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert"], {"name": name, "email": email})
        conn.commit()
        conn.close()

    def delete(self, email):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete"], {"email": email})
        conn.commit()
        conn.close()

    def update_name(self, email, new_name):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update_name"], {"name": new_name, "email": email})
        conn.commit()
        conn.close()

    def get_student_by_email(self, email):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_by_email"],
                              {"email": email})
        student = result.mappings().all()
        conn.close()
        return student
