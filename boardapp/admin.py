from django.contrib import admin
from boardapp.models import Users

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Users,UsersAdmin)