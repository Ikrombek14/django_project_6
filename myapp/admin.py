from django.contrib import admin
from .models import Universitate, Fakultet, Guruh, Kafedra, Fan, Ustoz, Student

# Register your models here.
admin.site.register(Universitate)
admin.site.register(Fakultet)
admin.site.register(Guruh)
admin.site.register(Student)
admin.site.register(Kafedra)
admin.site.register(Fan)
admin.site.register(Ustoz)
