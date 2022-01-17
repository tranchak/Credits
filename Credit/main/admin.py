from django.contrib import admin

# Register your models here.
from .models import Bank, Credit, Client

admin.site.register(Bank)
admin.site.register(Credit)
admin.site.register(Client)