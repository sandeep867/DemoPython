from django.contrib import admin
from . models import MyTable
from . models import NewTable
# Register your models here.
admin.site.register(MyTable)
admin.site.register(NewTable)