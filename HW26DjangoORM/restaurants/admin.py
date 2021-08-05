from django.contrib import admin
from .models import Restaurant, Workers, Menu, City, Country


admin.site.register(Restaurant)
admin.site.register(Workers)
admin.site.register(Menu)
admin.site.register(City)
admin.site.register(Country)

