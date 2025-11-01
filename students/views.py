from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students} )

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        course = request.POST['course']
        Student.objects.create(name=name, email=email, age=age, course=course)
        return redirect('student_list')
    return render(request, 'students/add_student.html')


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'students/edit_student.html', {'student': student})  # Folder name is students




def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')
