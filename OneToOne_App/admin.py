
from django.contrib import admin

from OneToOne_App.models import Student,Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'sno','sname','marks']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'cno','cname','cfee', 'student']

# Register with admin site
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
