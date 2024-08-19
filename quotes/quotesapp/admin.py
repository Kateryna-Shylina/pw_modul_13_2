from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tag, Authors, Qoutes

# Register your models here.
admin.site.register(Tag)
admin.site.register(Authors)
admin.site.register(Qoutes)