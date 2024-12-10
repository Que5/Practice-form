from django.contrib import admin
from . models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email", "mobile_number", "message",)


admin.site.register(Form, FormAdmin)
