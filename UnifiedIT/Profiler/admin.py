from django.contrib import admin
from .models import *


class InstituteAdmitSite(admin.AdminSite):
    site_header = "Institute Admin"


institute_admin_site = InstituteAdmitSite(name='institute_admin')


institute_admin_site.register(Person)
institute_admin_site.register(Address)
institute_admin_site.register(Contact)
institute_admin_site.register(Department)
institute_admin_site.register(Faculty)
institute_admin_site.register(Student)
institute_admin_site.register(Course)
institute_admin_site.register(Subject)
institute_admin_site.register(Session)
institute_admin_site.register(SessPrac)
institute_admin_site.register(SessTheory)
institute_admin_site.register(Division)
institute_admin_site.register(Batch)
institute_admin_site.register(Exam)
institute_admin_site.register(Grade)
institute_admin_site.register(ToBeCovered)
institute_admin_site.register(TimeTable)
institute_admin_site.register(Attendance)
institute_admin_site.register(Topic)
institute_admin_site.register(FacultyIncharge)