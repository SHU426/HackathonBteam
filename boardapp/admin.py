# from django.contrib import admin
# from boardapp.models import Users

# # Register your models here.

# class UsersAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Users,UsersAdmin)

from django.contrib import admin
from .models import User,Board,Msg_detail
# Register your models here.
# from .models import Question
# from .models import Choice
admin.site.register(User)
admin.site.register(Board)
admin.site.register(Msg_detail)