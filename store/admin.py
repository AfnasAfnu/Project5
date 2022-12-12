from django.contrib import admin

# Register your models here.
from store.models import Courses, Departments, Person

admin.site.register(Courses)
admin.site.register(Departments)
admin.site.register(Person)
