from django.contrib import admin
from .models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'email',  'gender', 'company_name', 'last_login']
    list_filter = ['name', 'email', 'last_login']
    prepopulated_fields = {'name':('email',)}
