from django.contrib import admin
from cotizar.models import *
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy



@admin.register(Anio)
class AnioAdmin(admin.ModelAdmin):
    list_display = ('id_anio','anio_antig')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id_marca','name_marca')



@admin.register(RiesgAseg)
class RiesgAsegAdmin(admin.ModelAdmin):
	list_display = ('riesgo','marca','modelo','aseguradora','programa')
	list_filter = ('aseguradora',)
	search_fields = ('aseguradora__name_asegurad','id_model__id_marca__name_marca')
	
	def aseguradora(self, obj):
		return obj.aseguradora.name_asegurad

	def riesgo(self, obj):
		return obj.id_riesg.tipo_riesgo

	def modelo(self, obj):
		return obj.id_model.id_modelo.name_model

	def marca(self, obj):
		return obj.id_model.id_marca.name_marca

	def tipo(self, obj):
		return obj.id_model.id_tipo.clase

	def programa(self, obj):
		return obj.programa.program





# Some SimpleListFilter filters
@admin.register(AutoValor)
class AutoValorAdmin(admin.ModelAdmin):


	list_display = ('get_marca','get_modelo','traccion')
	list_filter = (
		('id_marca', RelatedOnlyFieldListFilter),
	)
	list_editable = ('traccion',)
	admin_order_field = ('id_marca',)
	search_fields = ('traccion',)

	def get_marca(self, obj):
		return obj.id_marca.name_marca
	get_marca.short_description = 'Marca'
	get_marca.admin_order_field = 'autovalor__id_marca'

	def get_modelo(self, obj):
		return obj.id_modelo.name_model
	get_modelo.short_description = 'Modelo'
	get_modelo.admin_order_field = 'autovalor__id_modelo'





# @admin.register(AutoValor)
# class AutoValorAdmin(admin.ModelAdmin):
	
# 	list_display = ('get_marca','get_modelo','traccion')
	
# 	def get_marca(self, obj):
# 		return obj.id_marca.name_marca
# 	get_marca.short_description = 'Marca'
# 	get_marca.admin_order_field = 'autovalor__id_marca'

# 	def get_modelo(self, obj):
# 		return obj.id_modelo.name_model
# 	get_modelo.short_description = 'Modelo'
# 	get_modelo.admin_order_field = 'autovalor__id_modelo'
