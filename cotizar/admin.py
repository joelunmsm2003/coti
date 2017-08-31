from django.contrib import admin
from cotizar.models import *
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy



# @admin.register(Anio)
# class AnioAdmin(admin.ModelAdmin):
#     list_display = ('id_anio','anio_antig')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id_marca','name_marca','origen')
    list_editable = ('origen',)
    search_fields = ('origen',)

@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('id_serv','services')


@admin.register(Programa)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id_program','program',)
    search_fields = ('program',)

    
@admin.register(Cobertura)
class CoberturaAdmin(admin.ModelAdmin):
    list_display = ('id_cobert','descripcion')

@admin.register(Aseguradora)
class AseguradoraAdmin(admin.ModelAdmin):
    list_display = ('id_asegurad','name_asegurad')

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id_clase','clase')

@admin.register(TasaAsegur)
class TasaAsegurAdmin(admin.ModelAdmin):
	list_display = ('get_aseguradora','get_programa','get_uso','get_riesgo','origen','anio','value')
	list_editable = ('anio','value')
	list_filter = ('anio','programa__program')
	search_fields = ('id_aseg__name_asegurad','programa__program','riesgo__tipo_riesgo','origen','id_uso__uso','anio')


	def get_programa(self, obj):
		return obj.programa.program
	
	def get_aseguradora(self, obj):
		return obj.id_aseg.name_asegurad


	def get_riesgo(self, obj):
		return obj.riesgo.tipo_riesgo

	def get_uso(self, obj):
		return obj.id_uso.uso
	get_uso.short_description = 'Uso'

	def get_anio(self, obj):
		anio = Anio.objects.get(id_anio=obj.anio).anio_antig
		return anio


@admin.register(Tipouso)
class TipousoAdmin(admin.ModelAdmin):
	list_display = ('get_tipo','get_uso')

	def get_tipo(self, obj):
		return obj.tipo.clase
	def get_uso(self, obj):
		return obj.uso.uso


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
	list_display = ('id_model','name_model')
	search_fields = ('name_model',)


@admin.register(Gps)
class GpsAdmin(admin.ModelAdmin):
	list_display = ('id','get_modelo','aseguradora','marca','modelo','tipo','riesgo','programa','value')
	list_filter = ('id_aseg','id_auto__id_marca__name_marca','id_auto__id_modelo__name_model')
	search_fields = ('id_aseg__name_asegurad','id_auto__id_marca__name_marca','id_auto__id','id_auto__id_modelo__name_model','id_riesg__tipo_riesgo','id_prog__program','value')
	
	def aseguradora(self, obj):
		return obj.id_aseg.name_asegurad

	def riesgo(self, obj):
		return obj.id_riesg.tipo_riesgo

	def modelo(self, obj):
		return obj.id_auto.id_modelo.name_model

	def marca(self, obj):
		return obj.id_auto.id_marca.name_marca

	def tipo(self, obj):
		return obj.id_auto.id_tipo.clase

	def programa(self, obj):
		return obj.id_prog.program

	def get_modelo(self,obj):
		return obj.id_auto.id



@admin.register(ProgAseg)
class ProgAsegAdmin(admin.ModelAdmin):
	list_display = ('get_aseguradora','get_programa',)
	search_fields = ('id_aseg__name_asegurad','id_prog__program')
	list_filter = ('id_aseg',)
	def get_programa(self, obj):
		return obj.id_prog.program
	def get_aseguradora(self, obj):
		return obj.id_aseg.name_asegurad


@admin.register(RiesgAseg)
class RiesgAsegAdmin(admin.ModelAdmin):
	list_display = ('id','get_modelo','aseguradora','marca','modelo','tipo','riesgo','programa')
	list_filter = ('aseguradora',)
	search_fields = ('aseguradora__name_asegurad','id_model__id_marca__name_marca','id_model__id_modelo__name_model','id_riesg__tipo_riesgo','programa__program')
	
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

	def get_modelo(self,obj):
		return obj.id_model.id





# Some SimpleListFilter filters
@admin.register(AutoValor)
class AutoValorAdmin(admin.ModelAdmin):


	list_display = ('id','get_marca','get_modelo','get_clase','traccion','mapfretaxialto','permitidopositiva')
	list_filter = (
		('id_marca', RelatedOnlyFieldListFilter),
	)
	list_editable = ('traccion','mapfretaxialto','permitidopositiva')
	admin_order_field = ('id_marca',)
	search_fields = ('id_marca__name_marca','id_modelo__name_model','permitidopositiva')

	def get_marca(self, obj):
		return obj.id_marca.name_marca
	get_marca.short_description = 'Marca'
	get_marca.admin_order_field = 'autovalor__id_marca'

	def get_modelo(self, obj):
		return obj.id_modelo.name_model
	get_modelo.short_description = 'Modelo'
	get_modelo.admin_order_field = 'autovalor__id_modelo'

	def get_clase(self, obj):
		return obj.id_tipo.clase
	get_modelo.short_description = 'Clase'




# Some SimpleListFilter filters
@admin.register(ServicAsegur)
class ServicAsegurAdmin(admin.ModelAdmin):


	list_display = ('get_aseguradora','get_servicio','get_uso','get_programa','valor')
	search_fields = ('id_aseg__name_asegurad','id_serv__services','id_program__program','valor')

	def get_aseguradora(self, obj):
		return obj.id_aseg.name_asegurad
	get_aseguradora.short_description = 'Aseguradora'


	def get_servicio(self, obj):
		return obj.id_serv.services
	get_servicio.short_description = 'Servicio'


	def get_uso(self, obj):
		return obj.id_uso.uso
	get_uso.short_description = 'Uso'


	def get_programa(self, obj):
		return obj.id_program.program
	get_programa.short_description = 'Programa'




# Some SimpleListFilter filters
@admin.register(CobertAsegur)
class CobertAsegurAdmin(admin.ModelAdmin):


	list_display = ('get_aseguradora','get_cobertura','get_programa','get_uso','get_tipo','value')
	list_editable = ('value',)
	list_filter = ('id_cob__descripcion','programa__program')

	search_fields = ('id_aseg__name_asegurad','id_cob__descripcion','programa__program','id_uso__uso','tipo__clase','value')


	def get_aseguradora(self, obj):
		return obj.id_aseg.name_asegurad
	get_aseguradora.short_description = 'Aseguradora'

	def get_cobertura(self, obj):
		return obj.id_cob.descripcion
	get_cobertura.short_description = 'Cobertura'

	def get_programa(self, obj):
		return obj.programa.program
	get_programa.short_description = 'Programa'

	def get_value(self, obj):
		return obj.value
	get_value.short_description = 'Valor'

	def get_uso(self, obj):
		return obj.id_uso.uso
	get_uso.short_description = 'Uso'

	def get_tipo(self, obj):
		return obj.tipo.clase
	get_tipo.short_description = 'Tipo'


# Some SimpleListFilter filters
@admin.register(DeducAsegur)
class DeducAsegurAdmin(admin.ModelAdmin):


	list_display = ('get_aseguradora','get_deduccion','get_programa','get_uso','get_tipo','get_riesgo','value')

	list_editable = ('value',)

	list_filter = ('id_deduc__deducible','programa__program')

	search_fields = ('id_aseg__name_asegurad','id_deduc__deducible','programa__program','id_uso__uso','tipo__clase','riesgo__tipo_riesgo','value')


	def get_aseguradora(self, obj):
		return obj.id_aseg.name_asegurad
	get_aseguradora.short_description = 'Aseguradora'

	def get_deduccion(self, obj):
		return obj.id_deduc.deducible
	get_deduccion.short_description = 'Deducible'

	def get_programa(self, obj):
		return obj.programa.program
	get_programa.short_description = 'Programa'

	def get_value(self, obj):
		return obj.value
	get_value.short_description = 'Valor'

	def get_uso(self, obj):
		return obj.id_uso.uso
	get_uso.short_description = 'Uso'

	def get_tipo(self, obj):
		return obj.tipo.clase
	get_tipo.short_description = 'Tipo'

	def get_riesgo(self, obj):
		return obj.riesgo.tipo_riesgo
	get_riesgo.short_description = 'Riesgo'






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
