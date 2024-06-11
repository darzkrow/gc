from django.contrib import admin
from .models import Estados, Employes

from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json
# Register your models here.
# admin.py
admin.site.site_header = 'HIDROVEN | Sala Situacional'
admin.site.site_title = 'Panel de Administración'
admin.site.index_title = 'Bienvenido al Panel de Administración'





@admin.register(Estados)
class EstadosAdmin(admin.ModelAdmin):
    list_display = ('estado', 'capital', 'sigla') 
    search_fields = ('estado', 'capital')
    ordering = ('estado',)  



@admin.register(Employes)
class EmpleadosAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Información Personal', {'fields': ['cedper', 'nomper', 'apeper', 'telmovper']}),
        ('Dependencia y Status', {'fields': [ 'dependencia','oficina', 'cargo', 'status']}),
        ('Ubicación', {'fields': ['estado', 'municipio','parroquia' ]}),
        ('Centro de Votación', {'fields': ['centro']}),
         ('Participo', {'fields': ['votacion']}),
    ]
    list_display = ('cedper', 'nomper', 'apeper','telmovper','votacion')
    search_fields = ('cedper', 'nomper', 'apeper',)
    ordering = ('cedper',)  
    list_filter = ('dependencia','status', )
    list_display_links = ('cedper', 'nomper', 'apeper',)
    autocomplete_fields = ['estado',]
    list_editable = ['votacion']
    actions = ['contador_hp','contador_jubilado' , 'contador_votos' ]

    def contador_jubilado(self, request, queryset):
        count = queryset.filter(status='JUB',votacion=True).count()
        self.message_user(request, f"Cant Participación por Jubilados: {count} votos")
    contador_jubilado.short_description = "Contar Jubilados"

    def contador_hp(self, request, queryset):
        count = queryset.filter(status='HP',votacion=True).count()
        self.message_user(request, f"Cant. Participación por Honorario Profesional: {count}  votos")
    contador_hp.short_description = "Contar Personal HP"

    def contador_votos(self, request, queryset):
        count = queryset.filter(votacion=True).count()
        self.message_user(request, f"Total de Participación: {count} votos")
    contador_votos.short_description = "Total de Participación"



    def get_readonly_fields(self, request, obj=None):
        if obj:
            if obj.votacion:
                return ('cedper', 'nomper', 'apeper', 'telmovper', 'dependencia', 'oficina', 'status', 'estado', 'municipio', 'parroquia','cargo', 'centro', 'votacion')
            else:
                return ('cedper', 'nomper', 'apeper', 'telmovper', 'dependencia', 'oficina', 'status', 'estado', 'municipio', 'parroquia', 'cargo','centro')
        return ()
   