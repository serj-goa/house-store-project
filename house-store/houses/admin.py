from django.contrib import admin as a

from houses.models import House


@a.register(House)
class HouseAdmin(a.ModelAdmin):
    pass
