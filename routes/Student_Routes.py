
from flask import Blueprint, render_template, request, redirect, url_for

from service.StudentService import StudentService




student_bp= Blueprint('student', __name__)
@student_bp.route("/newstudent", methods=['GET'])
def student():
    return render_template("addstudent.html")

@student_bp.route("/liststudent", methods=['POST', 'GET'])
def liststudents():
    if request.method == 'POST':
        form = request.form
        student_name = form.get('Name')
        student_school = form.get('School')
        if student_name and student_school:
            StudentService.add_student(student_name, student_school)

    result = StudentService.get_all_students()
    return render_template("liststudent.html", result=result)


@student_bp.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if request.method == 'POST':
        name = request.form.get('Name')
        school = request.form.get('School')
        StudentService.update_student(student_id, name, school)
        return redirect(url_for('student.liststudents'))

    student = StudentService.get_by_id(student_id)
    if not student:
        return redirect(url_for('student.liststudents'))
    return render_template('editstudent.html', student=student)


@student_bp.route('/student/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    StudentService.delete_student(student_id)
    return redirect(url_for('student.liststudents'))