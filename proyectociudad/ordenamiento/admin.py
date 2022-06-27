from ctypes import addressof
from django.contrib import admin

# Register your models here.
from ordenamiento.models import Parroquia, Barrio

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo')
    search_fields = ('nombre','tipo')

admin.site.register(Parroquia,ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre','num_viviendas','num_parques','num_edificios','parroquia')
    search_fields = ('num_parques','num_viviendas','parroquia',)

admin.site.register(Barrio,BarrioAdmin)