from django.contrib import admin

from watches.models import Watches, Category

admin.site.register(Watches)
admin.site.register(Category)