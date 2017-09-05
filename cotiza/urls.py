from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import patterns
from cotizar.views import *


from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns, include


admin.site.site_header = 'Cotizador Hermes'

urlpatterns = [

    url(r'^api-token-auth/', 'jwt_auth.views.obtain_jwt_token'),
    url(r'^admin/', admin.site.urls),
    url(r'^perfil/$', Perfil.as_view()),
    url(r'^riesgocsv/(\d+)', 'cotizar.views.riesgocsv'),
    url(r'^riesgosubir/(\d+)', 'cotizar.views.riesgosubir'),
    url(r'^riesgohdi/(\d+)', 'cotizar.views.riesgohdi'),
    url(r'^tipousosubir/', 'cotizar.views.tipousosubir'),
    url(r'^usos/(\d+)', 'cotizar.views.usos'),
    
    url(r'^descuentopositiva/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)', 'cotizar.views.descuentopositiva'),
    url(r'^excluidoshdi/', 'cotizar.views.excluidoshdi'),
    url(r'^marca/', 'cotizar.views.marca'),
    url(r'^anio/', 'cotizar.views.anio'),
    url(r'^uso/', 'cotizar.views.uso'),
    url(r'^timon/', 'cotizar.views.timon'),
    url(r'^riesgos/', 'cotizar.views.riesgos'),
    url(r'^modalidad/', 'cotizar.views.modalidad'),
    url(r'^tasascsv/(\d+)/', 'cotizar.views.tasascsv'),
    url(r'^modelo/(\d+)/', 'cotizar.views.modelo'), 
    url(r'^precio/(\d+)/(\d+)', 'cotizar.views.precio'),
    url(r'^generate_pdf_view/', 'cotizar.views.generate_pdf_view'),
    url(r'^preciodreprecio/(\d+)/', 'cotizar.views.preciodreprecio'),
    url(r'^claseModelo/(\d+)/', 'cotizar.views.claseModelo'),
    url(r'^cotiSave/', 'cotizar.views.cotiSave'),
    url(r'^datosfiltro/(\d+)/', 'cotizar.views.datosfiltro'),
    url(r'^cobertura/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/', 'cotizar.views.cobertura'),
    url(r'^deducible/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/', 'cotizar.views.deducible'),
    url(r'^servic/(\w+)/(\w+)', 'cotizar.views.servic'),
    url(r'^servicio/(\d+)/', 'cotizar.views.servicio'),
    # url(r'^financ/', 'cotizar.views.financ'),
    url(r'^financiamiento/(\d+)/', 'cotizar.views.financiamiento'),
    url(r'^aseguradoras/', 'cotizar.views.aseguradoras'),
    url(r'^coberturas/', 'cotizar.views.coberturas'),
    url(r'^deducciones/', 'cotizar.views.deducciones'),
    url(r'^clase/', 'cotizar.views.clase'),
    url(r'^add/', 'cotizar.views.add'),
    url(r'^adddeduccion/', 'cotizar.views.adddeduccion'),
    url(r'^man_cob/', 'cotizar.views.man_cob'),
    url(r'^man_serv/', 'cotizar.views.man_serv'),
    url(r'^man_finan/', 'cotizar.views.man_finan'),
    url(r'^man_tasas/', 'cotizar.views.man_tasas'),
    url(r'^man_autos/', 'cotizar.views.man_autos'),
    url(r'^deduc_cob/', 'cotizar.views.deduc_cob'),
    url(r'^addmodalidad/', 'cotizar.views.addmodalidad'),
    url(r'^addaseguradora/', 'cotizar.views.addaseguradora'),
    url(r'^addcobertura/', 'cotizar.views.addcobertura'),
    url(r'^adddeducible/', 'cotizar.views.adddeducible'),
    url(r'^addpoliticagps/', 'cotizar.views.addpoliticagps'),
    url(r'^addpoliticagps2/', 'cotizar.views.addpoliticagps2'),
    url(r'^addfinanciamiento/', 'cotizar.views.addfinanciamiento'),
    url(r'^addtasa/', 'cotizar.views.addtasa'),
    url(r'^adduso/', 'cotizar.views.adduso'),
    url(r'^addriesgo/', 'cotizar.views.addriesgo'),
    url(r'^addclase/', 'cotizar.views.addclase'),
    url(r'^addprograma/', 'cotizar.views.addprograma'),
    url(r'^addservice/', 'cotizar.views.addservice'),
    url(r'^addservicio/', 'cotizar.views.addservicio'),
    url(r'^addfinanz/', 'cotizar.views.addfinanz'),
    url(r'^addfinanzas/', 'cotizar.views.addfinanzas'),
    url(r'^listaservice/', 'cotizar.views.listaservice'),
    url(r'^listafinanciamiento/', 'cotizar.views.listafinanciamiento'),
    url(r'^listafinance/', 'cotizar.views.listafinance'),
    url(r'^listfinanase/', 'cotizar.views.listfinanase'),
    url(r'^listagps/', 'cotizar.views.listagps'),
    url(r'^listagps2/', 'cotizar.views.listagps2'),
    url(r'^listprimas/', 'cotizar.views.listprimas'),
    url(r'^exportarcobertura/(\w+)', 'cotizar.views.exportarcobertura'),
    url(r'^exportardeducible/(\w+)', 'cotizar.views.exportardeducible'),
    url(r'^exportarriesgo/(\w+)', 'cotizar.views.exportarriesgo'),
    url(r'^corrige/', 'cotizar.views.corrige'),
    url(r'^modeloscsv/', 'cotizar.views.modeloscsv'),
    url(r'^pdfx/', 'cotizar.views.pdfx'),
    url(r'^logearse/', 'cotizar.views.logearse'),
    url(r'^estadologin/', 'cotizar.views.estadologin'),
    url(r'^parametros/', 'cotizar.views.parametros'),
    url(r'^categorias/', 'cotizar.views.categorias'),
    url(r'^eliminarcob/', 'cotizar.views.eliminarcob'),
    url(r'^eliminardedu/', 'cotizar.views.eliminardedu'),
    url(r'^eliminarserv/', 'cotizar.views.eliminarserv'),
    url(r'^eliminarfinan/', 'cotizar.views.eliminarfinan'),
    url(r'^eliminartasa/', 'cotizar.views.eliminartasa'),
    url(r'^eliminarprima/', 'cotizar.views.eliminarprima'),
    url(r'^primaneta/(\d+)/(\d+)/(\d+)', 'cotizar.views.primaneta'),
    url(r'^catemodelo/(\d+)/', 'cotizar.views.catemodelo'),
    url(r'^riesgomodelo/(\d+)/', 'cotizar.views.riesgomodelo'),
    url(r'^programas/', 'cotizar.views.programas'),
    url(r'^listmodelo/', 'cotizar.views.listmodelo'),
    url(r'^addauto/', 'cotizar.views.addauto'),
    url(r'^addmarca/', 'cotizar.views.addmarca'),
    url(r'^addmodelo/', 'cotizar.views.addmodelo'),
    url(r'^addclase/', 'cotizar.views.addclase'),
    url(r'^addprima/', 'cotizar.views.addprima'),
    url(r'^eliminarauto/', 'cotizar.views.eliminarauto'),
    url(r'^editauto/', 'cotizar.views.editauto'),
    url(r'^listparametros/', 'cotizar.views.listparametros'),
    url(r'^savecob/', 'cotizar.views.savecob'),
    url(r'^savededu/', 'cotizar.views.savededu'),
    url(r'^saveservicio/', 'cotizar.views.saveservicio'),
    url(r'^savepoliticas/', 'cotizar.views.savepoliticas'),
    url(r'^savefinanc/', 'cotizar.views.savefinanc'),
    url(r'^saveprimas/', 'cotizar.views.saveprimas'),
    url(r'^savetasa/', 'cotizar.views.savetasa'),
    url(r'^riesgosclase/', 'cotizar.views.riesgosclase'),
    url(r'^addriesgoclase/', 'cotizar.views.addriesgoclase'),
    url(r'^eliminarries/', 'cotizar.views.eliminarries'),
    #url(r'^eliminarpolitica/', 'cotizar.views.eliminarpolitica'),
    url(r'^addigv/', 'cotizar.views.addigv'),
    url(r'^asegprogram/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', 'cotizar.views.asegprogram'),
    url(r'^subir/', 'cotizar.views.subir'),
    url(r'^generapdf/', 'cotizar.views.generapdf'),
    url(r'^getgps/(\d+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)', 'cotizar.views.getgps'),
    url(r'^subir/', 'cotizar.views.subir'),
    url(r'^enviaemail', 'cotizar.views.enviaemail'),
    url(r'^fiiiii/', 'cotizar.views.fiiiii'),
    url(r'^tasaadmin/', 'cotizar.views.tasaadmin'),
    url(r'^subirtasas', 'cotizar.views.subirtasas'),
    url(r'^uploadfile', 'cotizar.views.uploadfile'),
    url(r'^marcacsv', 'cotizar.views.marcacsv'),
    url(r'^marcaschinas', 'cotizar.views.marcaschinas'),
    url(r'^excluidospositiva', 'cotizar.views.excluidospositiva'),
    url(r'^excluidosrimac', 'cotizar.views.excluidosrimac'),
    url(r'^gpscsv/(\d+)', 'cotizar.views.gpscsv'),
    url(r'^gpsrimacsubir', 'cotizar.views.gpsrimacsubir'),
    url(r'^coberturacsv/(\d+)', 'cotizar.views.coberturacsv'),
    url(r'^deduciblecsv/(\d+)', 'cotizar.views.deduciblecsv'),
    url(r'^serviciocsv/(\d+)', 'cotizar.views.serviciocsv'),

    




]