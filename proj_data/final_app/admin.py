from django.contrib import admin
from .models import Studentbody,Role,Department,Wings,Equipement,Equipment_user
# Register your models here.
admin.site.register(Studentbody)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Wings)
admin.site.register(Equipement)
admin.site.register(Equipment_user)