from django.contrib import admin
from . import models

from jazigo.models import Cemiterio, Sepultado, QuadraESepultura, TransferenciaDeOssada, Jazigo, Concessionario

class ListandoJazigo(admin.ModelAdmin):
    list_display = ('identificacao_jazigo', 'nome_concessionaro')
    list_display_links = ('identificacao_jazigo', 'nome_concessionaro')
    """search_fields = ('nome_concessionaro',)"""
    list_per_page = 10

class ListandoSepulturas(admin.ModelAdmin):
    list_display = ('quadra', 'sepultura', 'complemento')

admin.site.register(Cemiterio)
admin.site.register(Sepultado)
admin.site.register(QuadraESepultura, ListandoSepulturas)
admin.site.register(Concessionario)
admin.site.register(TransferenciaDeOssada)
admin.site.register(Jazigo, ListandoJazigo)

#@admin.register(models.Jazigo)
#class AuthorAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ('identificacao_jazigo',), }