from django.contrib import admin
from .models import Student, Venue, Trainer, Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'venue', 'trainer')
    list_filter = ('start_date', 'end_date', 'venue', 'trainer')
    search_fields = ('name', 'venue', 'trainer', 'description')


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_filter = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')


admin.site.register(Student)
admin.site.register(Venue)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Course, CourseAdmin)

#class StudentAdmin(admin.ModelAdmin):

