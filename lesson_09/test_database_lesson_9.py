import uuid
from student_table import StudentTable

db = StudentTable("postgresql://postgres@localhost:5432/postgres")


def test_add_student():
    email = f"student_test_{uuid.uuid4().hex[:8]}@example.com"
    db.delete(email)
    db.create("Студент Тест", email)

    students = db.get_student_by_email(email)
    assert len(students) == 1
    assert students[0]["name"] == "Студент Тест"

    db.delete(email)


def test_update_student():
    email = f"student_test_{uuid.uuid4().hex[:8]}@example.com"
    db.delete(email)
    db.create("Студент Тест", email)

    db.update_name(email, "Студент изменен")

    students = db.get_student_by_email(email)
    assert students[0]["name"] == "Студент изменен"

    db.delete(email)


def test_delete_student():
    email = f"student_test_{uuid.uuid4().hex[:8]}@example.com"
    db.delete(email)
    db.create("Студент Тест", email)
    db.delete(email)

    students = db.get_student_by_email(email)
    assert len(students) == 0
