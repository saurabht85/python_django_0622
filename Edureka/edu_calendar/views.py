from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar
from .forms import ContactUsForm, StudentForm
from django.views import View, generic
from django.core.mail import send_mail, get_connection
from .models import Student, Venue, Trainer, Course

def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 2015 or year > 2022:
        year = date.today().year
    if month < 1 or month > 12:
        month = date.today().month
    month_name = calendar.month_name[month]
    title = f"Edureka Course calendar for : {month_name} - {year}"
    cal = HTMLCalendar().formatmonth(year, month)
    context_data = {'title': title, 'cal': cal}
    print(cal)
    return render(request, 'edu_calendar/calendar.html', context_data)


def contact_us(request):
    submitted = False
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data
            print(content)
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                content['subject'],
                content['message'],
                content['email'],
                ['admin@edurka.com', 'saurabh@edureka.com'],
                connection=con
            )
            return HttpResponseRedirect('/cal/contactus?submitted=True')

    else:
        form = ContactUsForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'edu_calendar/contact_us.html', {'form': form,
                                                            'submitted': submitted})

class ContactUs(View):

    def __init__(self):
        self.form_class = ContactUsForm
        self.template_name = 'edu_calendar/contact_us.html'
        self.submitted = False

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        print(f"Get: {request.GET}")
        if 'submitted' in request.GET:
            self.submitted = True
        return render(request, self.template_name, {'form': form,
                                                'submitted': self.submitted})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            content = form.cleaned_data
            print(content)
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                content['subject'],
                content['message'],
                content['email'],
                ['admin@edurka.com', 'saurabh@edureka.com'],
                connection=con
            )
            return HttpResponseRedirect('/cal/contact_us?submitted=True')
        return render(request, self.template_name, {'form': form,
                                                    'submitted': self.submitted})


"""
class ClassName(View):
    def __init__(self):
        self.form_class = ContactUsForm
    
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        pass
    def put(self, request, *args, **kwargs):
        pass
    def delete(self, request, *args, **kwargs):
        pass
"""

# class StudentList(View):
#     def __init__(self):
#         self.template_name = 'edu_calendar/student_list.html'
#
#     def get(self, request, *args, **kwargs):
#         all_students = Student.objects.all()
#         context_data = {'all_students': all_students}
#         return render(request, self.template_name, context_data)

# class StudentDetail(View):
#     def __init__(self):
#         self.template_name = 'edu_calendar/student_detail.html'
#
#     def get(self, request, *args, **kwargs):
#         student = Student.objects.get(id=kwargs['id'])
#         context_data = {'student': student}
#         return render(request, self.template_name, context_data)


class StudentList(generic.ListView):
    model = Student
    template_name = 'edu_calendar/student_list.html'


class StudentDetail(generic.DetailView):
    model = Student
    template_name = 'edu_calendar/student_detail.html'


class StudentCreate(View):
    def __init__(self):
        self.template_name = 'edu_calendar/student_create.html'
        self.form_class = StudentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            student = form.cleaned_data
            stu_obj = Student(firstname=student['firstname'],
                                lastname=student['lastname'],
                                email=student['email'])
            stu_obj.save()
            return HttpResponseRedirect('/cal/students/')
        return render(request, self.template_name, {'form': form})