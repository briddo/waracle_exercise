from django.contrib import admin

from .models import Cake


@admin.register(Cake)
class CakesAdmin(admin.ModelAdmin):
    pass
