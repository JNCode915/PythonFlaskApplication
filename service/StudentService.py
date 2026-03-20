from models.Student import Student,db




class StudentService:
    @staticmethod
    def justprint():
        print("Hello from StudentService")
        
    @staticmethod
    def add_student(student_name: str, student_school: str):
        new_student = Student(name=student_name, school=student_school)
        db.session.add(new_student)
        db.session.commit()
        return new_student
    
    @staticmethod
    def get_all_students():
        return Student.query.all()

    @staticmethod
    def get_by_id(student_id: int):
        return Student.query.get(student_id)

    @staticmethod
    def update_student(student_id: int, name: str, school: str):
        student = Student.query.get(student_id)
        if not student:
            return None
        if name:
            student.name = name
        if school:
            student.school = school
        db.session.commit()
        return student

    @staticmethod
    def delete_student(student_id: int):
        student = Student.query.get(student_id)
        if not student:
            return False
        db.session.delete(student)
        db.session.commit()
        return True