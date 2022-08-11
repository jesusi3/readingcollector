from django.contrib import admin

# Register your models here.
from .models import Badge, Reading, BookMark

# Register your models here
admin.site.register(Reading)
admin.site.register(BookMark)
admin.site.register(Badge)