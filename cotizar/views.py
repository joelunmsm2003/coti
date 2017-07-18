from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cotizar.models import *
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import View

from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin

from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail
from django.db import connection
from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin

from django.db.models import Count, Min, Sum, Avg
import collections
from datetime import *
from decimal import *
import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os
import pdfkit
import datetime
import pdfcrowd

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin

import simplejson
from django.views.decorators.csrf import csrf_exempt
import xlrd



from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, landscape

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


from django.http import HttpResponse


def tipousosubir(request):

	xls_name = '/home/tipousos.xls'



	book = xlrd.open_workbook(xls_name)

	sh = book.sheet_by_index(0)

	for rx in range(sh.nrows):

		for col in range(sh.ncols):

			if col == 3:

				tipo= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

			if col == 4:

				uso = str(sh.row(rx)[col]).split(':')[1].split('.')[0]

		Tipouso(tipo_id=tipo,uso_id=uso).save()	



	return HttpResponse('nologeado', content_type="application/json")

def marcaschinas(request):

	xls_name = '/home/chinas.xls'



	book = xlrd.open_workbook(xls_name)

	sh = book.sheet_by_index(0)

	for rx in range(sh.nrows):

		for col in range(sh.ncols):

			if rx>0:

				if col==0:

					marca= str(sh.row(rx)[col]).split("'")[1]

					marc= Marca.objects.get(name_marca=marca)

				if col==1:

					origen= str(sh.row(rx)[col]).split("'")[1]

					if origen=='Chino':
					
						marc.origen='Chino'
						
				if col ==2:

					orden = str(sh.row(rx)[col]).split(':')[1].split('.')[0]

					marc.orden = orden
					marc.save()

	return HttpResponse('nologeado', content_type="application/json")

def excluidospositiva(request):

	xls_name = '/home/excluidos_positiva.xls'


	book = xlrd.open_workbook(xls_name)

	sh = book.sheet_by_index(0)

	for rx in range(sh.nrows):

		for col in range(sh.ncols):



			if rx>0:

				if col==0:

					id= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

					a = AutoValor.objects.get(id=id)

				if col==5:


				
					if str(sh.row(rx)[col]).split("'")[1] == 'No permitido':

						a.permitido = 'No Permitido'
						a.save()


	return HttpResponse('nologeado', content_type="application/json")

def excluidoshdi(request):

	xls_name = '/home/excluidoshdi.xls'



	book = xlrd.open_workbook(xls_name)

	sh = book.sheet_by_index(0)

	for rx in range(sh.nrows):

		for col in range(sh.ncols):


			if rx>0:

				if col==0:

					id= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

					a = AutoValor.objects.get(id=id)


				if col==5:




					if str(sh.row(rx)[col]).split("'")[1] == 'x':

						a.excluidohdi = 'Si'
						a.save()


	return HttpResponse('nologeado', content_type="application/json")

def gpsrimacsubir(request):

	xls_name = '/home/gpspacificosubir.xls'

	book = xlrd.open_workbook(xls_name)

	sh = book.sheet_by_index(0)

	Gps.objects.filter(id_aseg_id=2).delete()

	for rx in range(sh.nrows):

		for col in range(sh.ncols):

			if rx>0:

				if col==0:

					id= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

					a = AutoValor.objects.get(id=id)

				# if col==4:

				# 	if str(sh.row(rx)[col]).split("'")[1] == 'x':

				# 		Gps(id_auto_id=a.id,value='Si',id_aseg_id=4).save()

				# if col==5:

				# 	if str(sh.row(rx)[col]).split("'")[1] == 'x':

				# 		Gps(id_auto_id=a.id,value='Si',id_aseg_id=5).save()

				# if col==6:

				# 	if str(sh.row(rx)[col]).split("'")[1] == 'x':

				# 		Gps(id_auto_id=a.id,value='Si',id_aseg_id=3).save()

				# if col==7:

				# 	if str(sh.row(rx)[col]).split("'")[1] == 'x':

				# 		Gps(id_auto_id=a.id,value='Si',id_aseg_id=1).save()

				if col==8:

					if str(sh.row(rx)[col]).split("'")[1] == 'x':

						Gps(id_auto_id=a.id,value='Si',id_aseg_id=2).save()



	return HttpResponse('nologeado', content_type="application/json")


def excluidosrimac(request):

	xls_name = '/home/excluidorimac.xls'



	book = xlrd.open_workbook(xls_name)

	sh = book.sheet_by_index(0)

	for rx in range(sh.nrows):

		for col in range(sh.ncols):

			print rx,col

			if rx>0:

				if col==0:

					id= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

					a = AutoValor.objects.get(id=id)


				if col==5:



					if str(sh.row(rx)[col]).split("'")[1] == 'x':

						a.excluidorimac = 'Si'
						a.save()


	return HttpResponse('nologeado', content_type="application/json")



def riesgohdi(request,aseguradora):

	xls_name = '/home/riesgosubirhdi.xls'



	book = xlrd.open_workbook(xls_name)

	sh = book.sheet_by_index(0)

	RiesgAseg.objects.filter(aseguradora_id=3).delete()

	for rx in range(sh.nrows):

		for col in range(sh.ncols):

			print rx,col

			if rx>0:

				if col==0:

					asegu = str(sh.row(rx)[col]).split("'")[1]

				if asegu =='HDI':

					if col==1:

						if str(sh.row(rx)[col]).split(':')[0]=='number':

							modelo = str(sh.row(rx)[col]).split(':')[1].split('.')[0]

						else:

							modelo = str(sh.row(rx)[col]).split("'")[1]

					if col==2:

						marca = str(sh.row(rx)[col]).split("'")[1]



						if AutoValor.objects.filter(id_marca__name_marca=marca,id_modelo__name_model=modelo).count()>0:

							id_auto_valor = AutoValor.objects.filter(id_marca__name_marca=marca,id_modelo__name_model=modelo).values('id')[0]['id']


					
					if col==3:

						riesgo = str(sh.row(rx)[col]).split("'")[1]

						if AutoValor.objects.filter(id_marca__name_marca=marca,id_modelo__name_model=modelo).count()>0:

							id_riesgo = Riesgo.objects.get(tipo_riesgo=riesgo).id_riesgo

	

							RiesgAseg(id_model_id=id_auto_valor,aseguradora_id=3,id_riesg_id=id_riesgo).save()


	return HttpResponse('nologeado', content_type="application/json")


def riesgosubir(request,aseguradora):

	xls_name = '/home/riesgosubir.xls'

	print xls_name

	book = xlrd.open_workbook(xls_name)

	sh = book.sheet_by_index(0)

	RiesgAseg.objects.filter(aseguradora_id=2).delete()

	for rx in range(sh.nrows):

		for col in range(sh.ncols):

			print rx,col

			if rx>0:

				if col==0:

					asegu = str(sh.row(rx)[col]).split("'")[1]

				if asegu =='Pacifico':

					if col ==1:

						id_auto_valor= str(sh.row(rx)[col]).split(':')[1].split('.')[0]



					if col==6:

						n_riesgo = str(sh.row(rx)[col]).split("'")[1]


						if n_riesgo!='No Aplica':

							id_riesgo = Riesgo.objects.get(tipo_riesgo=n_riesgo).id_riesgo

							RiesgAseg(aseguradora_id=2,id_model_id=id_auto_valor,id_riesg_id=id_riesgo).save()

					

					#if col==1:

						# if str(sh.row(rx)[col]).split(':')[0]=='number':

						# 	modelo = str(sh.row(rx)[col]).split(':')[1].split('.')[0]

						# else:

						# 	modelo = str(sh.row(rx)[col]).split("'")[1]

					# if col==2:

					# 	marca = str(sh.row(rx)[col]).split("'")[1]

					# 	print marca,modelo

					# 	if AutoValor.objects.filter(id_marca__name_marca=marca,id_modelo__name_model=modelo).count()>0:

					# 		id_auto_valor = AutoValor.objects.filter(id_marca__name_marca=marca,id_modelo__name_model=modelo).values('id')[0]['id']

					# 		print 'id_auto_valor',id_auto_valor

					
					# if col==3:

					# 	riesgo = str(sh.row(rx)[col]).split("'")[1]

					# 	if AutoValor.objects.filter(id_marca__name_marca=marca,id_modelo__name_model=modelo).count()>0:

					# 		id_riesgo = Riesgo.objects.get(tipo_riesgo=riesgo).id_riesgo

					# 		print id_riesgo

					# 		RiesgAseg(id_model_id=id_auto_valor,aseguradora_id=aseguradora,id_riesg_id=id_riesgo).save()


	return HttpResponse('nologeado', content_type="application/json")



def uploadfile(request):

	if request.method == 'POST':

		process_file = request.FILES['file']

		Lote(file=process_file).save()

		id_lote = Lote.objects.all().values('id').order_by('-id')[0]['id']

		process_file = Lote.objects.get(id=id_lote).file

		xls_name = '/var/www/html/'+str(process_file)

		book = xlrd.open_workbook(xls_name)

		# sh = book.sheet_by_index(0)

		# TasaAsegur.objects.filter(id_aseg_id=5).delete()

		# print 'Rimac'

		# for rx in range(sh.nrows):

		# 	for col in range(sh.ncols):

		# 		if rx>4 and rx <24 :

		# 			if col==0:

		# 				ant= str(sh.row(rx)[col]).split(' ')[0].split("u'")[1]

		# 			if col > 0:

		# 				print rx,col,str(sh.row(rx)[col])

		# 				if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 					valor= str(sh.row(rx)[col]).split('number:')[1]

		# 					print valor
						
		# 					# Corporativo Rimac

		# 					if col==1:

		# 						TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=6,anio=ant,programa_id=2).save()

		# 					if col==2:

		# 						TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=7,anio=ant,programa_id=2).save()

		# 					if col==3:

		# 						TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=4,anio=ant,programa_id=2).save()

		# 					if col==4:

		# 						TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=5,anio=ant,programa_id=2).save()

		# 					if col==5:

		# 						TasaAsegur(id_aseg_id=5,value=valor,tipo_id=6,anio=ant,programa_id=2).save()

		# 					# Rimac 4x4


		# 					if col==6:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,tipo_id=6,id_uso_id=1,programa_id=7).save() # Rural

		# 					if col==7:

		# 						TasaAsegur(id_aseg_id=5,value=valor,tipo_id=7,anio=ant,id_uso_id=2,programa_id=7).save()

		# 					# Rimac Vehicular Pick Up

		# 					if col==8:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=6,id_uso_id=1).save()

		# 					if col==9:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=6,id_uso_id=6).save()

		# 					if col==10:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=6,id_uso_id=2).save()

		# 					# Rimac Chinos e Indios

		# 					if col==11:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=10,tipo_id=1).save()

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=10,tipo_id=3).save()

		# 					if col==12:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=10,tipo_id=6).save()

		# 					# Rimac Taxi Urbano

		# 					if col==13:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=11,tipo_id=1).save()

		# 					if col==14:

		# 						mo = AutoValor.objects.filter(id_modelo__name_model__in=['Yaris','Sail'])

		# 						for m in mo:

		# 							TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=11,modelo_id=m.id_modelo.id_model).save()

		# 					if col==15:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,origen='Chino',programa_id=11).save()

		# 					# Rimac Transporte Personal, Escolar, Turismo y Paneles

		# 					if col==16:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=12,ubicacion='Lima').save()

		# 					if col==17:

		# 						mo = AutoValor.objects.filter(id_modelo__name_model='H1')

		# 						for m in mo:

		# 							TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=12,modelo_id=m.id_modelo.id_model).save()

		# 					if col==18:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=12,tipo_id=7,id_uso_id=2,origen='No Chinas').save()

		# 					# Rimac pesados

		# 					if col==19:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=13,tipo_id=2).save()

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=13,tipo_id=21).save()

		# 					if col==20:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=13,tipo_id=20).save()

		# 					if col==21:

		# 						TasaAsegur(id_aseg_id=5,value=valor,anio=ant,programa_id=13,tipo_id=24).save()

		# 		if rx >= 24 and rx < 43:

		# 			if col==0:

		# 				ant= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

		# 				print ant

		# 			if col > 0:

		# 				print rx,col,str(sh.row(rx)[col]).split("'")[1]


		# 				valor= str(sh.row(rx)[col]).split("'")[1]


		# 				if col==1:

		# 					TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=6,anio=ant,programa_id=26).save()

		# 				if col==2:

		# 					TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=7,anio=ant,programa_id=26).save()

		# 				if col==3:

		# 					TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=4,anio=ant,programa_id=26).save()

		# 				if col==4:

		# 					TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=5,anio=ant,programa_id=26).save()


		# 		if rx >= 43:

		# 			if col==0:

		# 				ant= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

		# 			if col > 0:

		# 				print rx,col

		# 				valor= str(sh.row(rx)[col]).split("'")[1]

		# 				if col==1:

		# 					TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=6,anio=ant,programa_id=25).save()

		# 				if col==2:

		# 					TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=7,anio=ant,programa_id=25).save()

		# 				if col==3:

		# 					TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=4,anio=ant,programa_id=25).save()

		# 				if col==4:

		# 					TasaAsegur(id_aseg_id=5,value=valor,riesgo_id=5,anio=ant,programa_id=25).save()








			
		# print 'Mapfre'

		# TasaAsegur.objects.filter(id_aseg_id=4).delete()

		# sh = book.sheet_by_index(1)

		# for rx in range(sh.nrows):

		# 	for col in range(sh.ncols):

				

		# 		if rx>4:

		# 			if col==0:

		# 				ant= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

		# 				print ant

		# 			if col > 0:




						

		# 				if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 					valor= str(sh.row(rx)[col]).split('number:')[1]

		# 				#Corporativo Mapfre

		# 				if col==1:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=3,anio=ant,programa_id=1).save()

		# 				if col==2:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=2,anio=ant,programa_id=1).save()

		# 				if col==3:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=1,anio=ant,programa_id=1).save()

		# 				if col==4:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,origen='Chino',anio=ant,programa_id=1).save()

		# 				# MAPFRE Dorada Pick Up

		# 				if col==5:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,id_uso_id=1,anio=ant,programa_id=22).save()

		# 				if col==6:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,id_uso_id=2,anio=ant,programa_id=22).save()

		# 				if col==7:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,id_uso_id=6,programa_id=22).save() # Rural

		# 				if col==8:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,origen='Chino',id_uso_id=1,anio=ant,programa_id=22).save()

		# 				if col==9:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,origen='Chino',anio=ant,id_uso_id=2,programa_id=22).save()

		# 				if col==10:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,origen='Chino',id_uso_id=6,programa_id=22).save()

		# 				# Mapfre Dorada Economica

		# 				if col==11:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=3,anio=ant,programa_id=5).save()


		# 				if col==12:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=2,anio=ant,programa_id=5).save()

		# 				if col==13:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=1,anio=ant,programa_id=5).save()

		# 				if col==14:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,origen='Chino',programa_id=5).save()

		# 				if col==15:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 					 TasaAsegur(id_aseg_id=4,value=valor,anio=ant,tipo_id=6,programa_id=5).save()

		# 				#Mapfre 0 Km

		# 				if col==16:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=1,anio=ant,programa_id=27).save()

		# 				if col==17:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,origen='Chino',programa_id=27).save()

		# 				if col==18:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 					 TasaAsegur(id_aseg_id=4,value=valor,anio=ant,tipo_id=6,programa_id=27).save()

		# 				# Mapfre 0 KM x 2

		# 				if col==20:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=3,anio=ant,programa_id=14).save()

		# 				if col==21:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=2,anio=ant,programa_id=14).save()

		# 				if col==22:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,riesgo_id=1,anio=ant,programa_id=14).save()

		# 				if col==23:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,tipo_id=6,programa_id=14).save()

		# 				#Mapfre Camiones A

		# 				if col==24:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,tipo_id=2,programa_id=15).save()

		# 				if col==25:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,tipo_id=8,programa_id=15).save()

		# 				if col==26:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,tipo_id=25,programa_id=15).save()

		# 				# Mapfre Camiones menores A

		# 				if col==27:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,programa_id=16,tipo_id=2).save()

		# 				# MAPFRE Perdida Total Livianos

		# 				if col==28:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,programa_id=17).save()

		# 				# MAPFRE Plateada

		# 				if col==29:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,programa_id=18).save()

		# 				if col==30:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,programa_id=18).save()

		# 				# MAPFRE Serv. Turistico/Personal

		# 				if col==31:

		# 					print rx,col,str(sh.row(rx)[col])

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,ubicacion='Lima',programa_id=19).save()

		# 				#MAPFRE VIP Mujer

		# 				if col==32:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,riesgo_id=3,programa_id=20).save()


		# 				if col==33:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,riesgo_id=2,programa_id=20).save()


		# 				if col==34:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,riesgo_id=1,programa_id=20).save()

		# 				# Mapfre Taxi

		# 				if col==35:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,riesgo_id=3,programa_id=21).save()


		# 				if col==36:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,riesgo_id=1,programa_id=21).save()


		# 				if col==37:

		# 					if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 						TasaAsegur(id_aseg_id=4,value=valor,anio=ant,origen='Chino',programa_id=21).save()


		# TasaAsegur.objects.filter(id_aseg_id=3).delete()

		# print 'Hdi'

		# sh = book.sheet_by_index(2)

		# for rx in range(sh.nrows):

		# 	for col in range(sh.ncols):

		# 		if rx>4:

		# 			if col==0:

		# 				ant= str(sh.row(rx)[col]).split(' ')[0].split("u'")[1]

		# 			if col > 0:

		# 				print rx,col

		# 				if str(sh.row(rx)[col])!="text:u'No aplica'":

		# 					valor= str(sh.row(rx)[col]).split('number:')[1]

		# 					if col==1:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=5,anio=ant,programa_id=3).save()

		# 					if col==2:


		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=6,anio=ant,programa_id=3).save()

		# 					if col==3:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=7,anio=ant,programa_id=3).save()

		# 					if col==4:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=8,anio=ant,programa_id=3).save()

		# 					if col==5:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=9,anio=ant,programa_id=3).save()

		# 					if col==6:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=10,anio=ant,programa_id=3).save()

		# 					if col==7:

		# 						TasaAsegur(id_aseg_id=3,value=valor,anio=ant,categoria_id=11,programa_id=3).save() # Rural

		# 					if col==8:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=12,anio=ant,programa_id=3).save()

		# 					if col==9:

		# 						TasaAsegur(id_aseg_id=3,value=valor,anio=ant,categoria_id=13,programa_id=3).save()

		# 					if col==10:

		# 						TasaAsegur(id_aseg_id=3,value=valor,anio=ant,categoria_id=14,programa_id=3).save()

		# 					if col==11:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=15,anio=ant,programa_id=3).save()

		# 					if col==12:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=16,anio=ant,programa_id=3).save()

		# 					if col==13:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=17,anio=ant,programa_id=3).save()

		# 					if col==14:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=18,anio=ant,programa_id=3).save()

		# 					if col==15:

		# 						TasaAsegur(id_aseg_id=3,value=valor,categoria_id=19,anio=ant,programa_id=3).save()



		TasaAsegur.objects.filter(id_aseg_id=1).delete()
		
		print 'Positiva'

		sh = book.sheet_by_index(3)

		for rx in range(sh.nrows):

			for col in range(sh.ncols):

				if rx>4:

					if col==0:

						ant= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

					if col > 0:

						print rx,col,str(sh.row(rx)[col])

						if str(sh.row(rx)[col])!="text:u'No aplica'":

							valor= str(sh.row(rx)[col]).split('number:')[1]


							if col==1:

								TasaAsegur(id_aseg_id=1,value=valor,riesgo_id=3,anio=ant,programa_id=4).save()

							if col==2:

								TasaAsegur(id_aseg_id=1,value=valor,riesgo_id=2,anio=ant,programa_id=4).save()

							if col==3:

								TasaAsegur(id_aseg_id=1,value=valor,riesgo_id=1,anio=ant,programa_id=4).save()

							if col==4:

								TasaAsegur(id_aseg_id=1,value=valor,origen='Chino',anio=ant,programa_id=4).save()

							if col==5:

								TasaAsegur(id_aseg_id=1,value=valor,timon='Cambiado',anio=ant,programa_id=4).save()

							if col==6:

								TasaAsegur(id_aseg_id=1,value=valor,tipo_id=6,anio=ant,programa_id=4).save()

							if col==7:

								TasaAsegur(id_aseg_id=1,value=valor,tipo_id=6,origen='Chino',anio=ant,programa_id=4).save()


							###Uso Comercial

							if col == 8:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=2,riesgo_id=3,programa_id=28,anio=ant).save()

							if col==9:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=2,riesgo_id=2,programa_id=28,anio=ant).save()

							if col==10:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=2,riesgo_id=1,programa_id=28,anio=ant).save()

							if col==11:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=2,riesgo_id=1,programa_id=28,anio=ant).save()

							if col==13:

								TasaAsegur(id_aseg_id=1,value=valor,tipo_id=6,id_uso_id=2,programa_id=28,anio=ant).save()

							if col==14:

								TasaAsegur(id_aseg_id=1,value=valor,origen='Chino',id_uso_id=2,programa_id=28,anio=ant).save()

							#Uso Urbano Taxi

							if col==15:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=20,programa_id=29,riesgo_id=3,anio=ant).save()

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=20,programa_id=29,riesgo_id=2,anio=ant).save()

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=20,programa_id=29,riesgo_id=1,anio=ant).save()

							if col==16:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=20,origen='Chino',programa_id=29,anio=ant).save()

							#Uso ubano Publico

							if col==17:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=20,tipo_id=4,programa_id=30,anio=ant).save()

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=20,tipo_id=5,programa_id=30,anio=ant).save()

							#Uso Carga

							if col==18:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=17,tipo_id=2,programa_id=31,anio=ant).save()

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=17,tipo_id=21,programa_id=31,anio=ant).save()


							if col==19:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=17,tipo_id=20,programa_id=32,anio=ant).save()

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=17,tipo_id=18,programa_id=32,anio=ant).save()

							if col==20:

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=17,tipo_id=8,programa_id=32,anio=ant).save()

								TasaAsegur(id_aseg_id=1,value=valor,id_uso_id=17,tipo_id=19,programa_id=32,anio=ant).save()





		TasaAsegur.objects.filter(id_aseg_id=2).delete()

		### Pacifico

		sh = book.sheet_by_index(4)

		for rx in range(sh.nrows):

			for col in range(sh.ncols):

				

				if rx>3:

					if int(col)==0:

						ant= str(sh.row(rx)[col]).split(':')[1].split('.')[0]

					if int(col) > 0:

						

						if str(sh.row(rx)[col])!="text:u'No aplica'":

							valor= str(sh.row(rx)[col]).split('number:')[1]

							print rx,col


							if col==1:

								TasaAsegur(id_aseg_id=2,value=valor,riesgo_id=6,anio=ant,programa_id=4).save()

							if col==2:

								TasaAsegur(id_aseg_id=2,value=valor,riesgo_id=7,anio=ant,programa_id=4).save()

							if col==3:

								TasaAsegur(id_aseg_id=2,value=valor,riesgo_id=2,anio=ant,programa_id=4).save()

							if col==4:

								TasaAsegur(id_aseg_id=2,value=valor,riesgo_id=1,anio=ant,programa_id=4).save()

							if col==5:

								TasaAsegur(id_aseg_id=2,value=valor,origen='Chino',anio=ant,programa_id=4).save()

							if col==6:

								TasaAsegur(id_aseg_id=2,value=valor,tipo_id=6,anio=ant,programa_id=4).save()




		data_json = simplejson.dumps('nn')

		return HttpResponse(data_json, content_type="application/json")


def subirtasas(request):



	return render(request, 'subirtasas.html',{})


class Perfil(JSONWebTokenAuthMixin, View):

	def get(self, request):

		id =request.user.id

		print 'ID',id

		return HttpResponse(id, content_type="application/json")


def hello(c):
	from reportlab.lib.units import inch

	#First Example

	c.setFont("Helvetica", 6) #choose your font type and font size
  
def pdfout(request):
 
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

	p = canvas.Canvas(response)

	p.setFillColorRGB(0,0,0)


	logo = "/var/www/cotizacion/frontend/img/logo-hermes.png"

	p.drawImage(logo, 20, 800,width=80,height=22,mask='auto');

	hello(p)
	j=50

	r = requests.get('http://cotizador.hermes.pe:800/html/cotiza.json')
	c = requests.get('http://cotizador.hermes.pe:800/html/coberturas.json')
	d = requests.get('http://cotizador.hermes.pe:800/html/deducibles.json')
	s = requests.get('http://cotizador.hermes.pe:800/html/servicios.json')
	g = requests.get('http://cotizador.hermes.pe:800/html/gps.json')
	cl = requests.get('http://cotizador.hermes.pe:800/html/cliente.json')
	f = requests.get('http://cotizador.hermes.pe:800/html/financiamiento.json')

	a = json.loads(r.text)
	c= json.loads(c.text)
	d= json.loads(d.text)
	s= json.loads(s.text)
	g= json.loads(g.text)
	cl= json.loads(cl.text)
	cl= cl[0]
	fi= json.loads(f.text)


	#'id_cliente','fullname','email','celular','chose_marca__name_marca','chose_modelo__name_model','chose_tipo__clase','chose_timon__name_tipo','chose_modalid__name_modalidad','chose_uso__uso','chose_anio__anio_antig','chose_ubicl','chose_ubicp','chose_informat','value');
	

	# Draw things on the PDc. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.

	columna = 780
	es=0

	p.drawString(20, columna, "Datos Cliente")
	p.drawString(70+j, columna,str(cl['id_cliente'] ))
	p.drawString(120+j*2, columna,'Nombre: '+str(cl['fullname'] ))
	p.drawString(170+j*3, columna,'Email: '+str(cl['email'] ))


	et=2
	p.setFillColorRGB(0,0,0)
	p.rect(20,columna-13*et,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(13,10,101)
	p.drawString(22, columna-13*et+3,'Marca: ' )
	p.drawString(70+j, columna-13*et+3,'Modelo: ')
	p.drawString(120+j*2, columna-13*et+3,'Clase: ')
	p.drawString(170+j*3, columna-13*et+3,'Anio: ')
	p.drawString(220+j*4, columna-13*et+3,'Precio: ')


	et=3
	p.setFillColorRGB(0,0,0)

	p.drawString(20, columna-12*et,str(cl['chose_marca__name_marca']))
	p.drawString(70+j, columna-12*et,str(cl['chose_modelo__name_model'] ))
	p.drawString(120+j*2, columna-12*et,str(cl['chose_tipo__clase'] ))
	p.drawString(170+j*3, columna-12*et,str(cl['chose_anio__anio_antig'] ))
	p.drawString(220+j*4, columna-12*et,str(cl['value'] ))

	

	#et=4
	
	#p.drawString(70+j, columna-13*et+3,'MAPFRE ')
	#p.drawString(120+j*2, columna-13*et+3,'LA POSITIVA ')
	#p.drawString(170+j*3, columna-13*et+3,'RIMAC: ')
	#p.drawString(220+j*4, columna-13*et+3,'PACIFICO: ')
	#p.drawString(250+j*5, columna-13*et+3,'Marca: ' )

	et = 4
	#p.drawString(20, columna-15*et, "GPS")

	p.drawString(70+j, columna-13*et,'GPS: '+g['gpsmapfre'] )
	p.drawString(120+j*2, columna-13*et,'GPS: '+g['gpspositiva'] )
	p.drawString(170+j*3, columna-13*et,'GPS: '+g['gpsrimac'] )
	p.drawString(220+j*4, columna-13*et,'GPS: '+g['gpspacifico'])
	p.drawString(250+j*5, columna-13*et,'GPS: '+g['gpshdi'] )


	et=5
	p.setFillColorRGB(0,0,0)
	p.rect(20,columna-15*et,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(13,10,101)
	p.drawString(250, columna-15*et+3, "Financiamiento")

	fi[0]['financiamiento'] = fi[0]['financiamiento'].encode('ascii','ignore').encode('ascii','replace')
	fi[0]['mapfre'] = fi[0]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
	fi[0]['positiva']= fi[0]['positiva'].encode('ascii','ignore').encode('ascii','replace')
	fi[0]['rimac']= fi[0]['rimac'].encode('ascii','ignore').encode('ascii','replace')
	fi[0]['hdi']= fi[0]['hdi'].encode('ascii','ignore').encode('ascii','replace')

	fi[1]['financiamiento'] = fi[1]['financiamiento'].encode('ascii','ignore').encode('ascii','replace')
	fi[1]['mapfre'] = fi[1]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
	fi[1]['positiva']= fi[1]['positiva'].encode('ascii','ignore').encode('ascii','replace')
	fi[1]['rimac']= fi[1]['rimac'].encode('ascii','ignore').encode('ascii','replace')
	fi[1]['hdi']= fi[1]['hdi'].encode('ascii','ignore').encode('ascii','replace')

	fi[2]['financiamiento'] = fi[2]['financiamiento'].encode('ascii','ignore').encode('ascii','replace')
	fi[2]['mapfre'] = fi[2]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
	fi[2]['positiva']= fi[2]['positiva'].encode('ascii','ignore').encode('ascii','replace')
	fi[2]['rimac']= fi[2]['rimac'].encode('ascii','ignore').encode('ascii','replace')
	fi[2]['hdi']= fi[2]['hdi'].encode('ascii','ignore').encode('ascii','replace')


	et =6
	p.drawString(20, columna-15*et, str(fi[0]['financiamiento']))
	p.drawString(70+j, columna-15*et, str(fi[0]['mapfre']))
	p.drawString(120+j*2, columna-15*et, str(fi[0]['positiva']))
	p.drawString(170+j*3, columna-15*et, str(fi[0]['rimac']))
	p.drawString(220+j*4, columna-15*et, str(fi[0]['pacifico']))
	p.drawString(250+j*5, columna-15*et, str(fi[0]['hdi']))

	et=7
	p.drawString(20, columna-15*et, str(fi[1]['financiamiento']))
	p.drawString(70+j, columna-15*et, str(fi[1]['mapfre']))
	p.drawString(120+j*2, columna-15*et, str(fi[1]['positiva']))
	p.drawString(170+j*3, columna-15*et, str(fi[1]['rimac']))
	p.drawString(220+j*4, columna-15*et, str(fi[1]['pacifico']))
	p.drawString(250+j*5, columna-15*et, str(fi[1]['hdi']))

	et=8
	p.drawString(20, columna-15*et, str(fi[2]['financiamiento'])[0:30])
	p.drawString(70+j, columna-15*et, str(fi[2]['mapfre']))
	p.drawString(120+j*2, columna-15*et, str(fi[2]['positiva']))
	p.drawString(170+j*3, columna-15*et, str(fi[2]['rimac']))
	p.drawString(220+j*4, columna-15*et, str(fi[2]['pacifico']))
	p.drawString(250+j*5, columna-15*et, str(fi[2]['hdi']))
	

	et=9

	p.drawString(20, columna-15*et, "Aseguradoras")
	p.drawString(70+j, columna-15*et, "Mapfre")
	p.drawString(120+j*2, columna-15*et, "La Positiva")
	p.drawString(170+j*3, columna-15*et, "Rimac")
	p.drawString(220+j*4, columna-15*et, "Pacifico")
	p.drawString(250+j*5, columna-15*et, "HDI")

	et =10
	p.drawString(20, columna-15*et, "Tasa")
	p.drawString(70+j, columna-15*et, str(a['tasamapfre']))
	p.drawString(120+j*2, columna-15*et, str(a['tasapositiva']))
	p.drawString(170+j*3, columna-15*et, str(a['tasarimac']))
	p.drawString(220+j*4, columna-15*et, str(a['tasapacifico']))
	p.drawString(250+j*5, columna-15*et, str(a['tasahdi']))

	et=11
	p.drawString(20, columna-15*et, "Prima Neta")
	p.drawString(70+j, columna-15*et, str(a['mapfre']))
	p.drawString(120+j*2, columna-15*et, str(a['positiva']))
	p.drawString(170+j*3, columna-15*et, str(a['rimac']))
	p.drawString(220+j*4, columna-15*et, str(a['pacifico']))
	p.drawString(250+j*5, columna-15*et, str(a['hdi']))

	et=12
	p.drawString(20, columna-15*et, "Prima Comercial")
	p.drawString(70+j, columna-15*et, str(a['mapfresubtotal']))
	p.drawString(120+j*2, columna-15*et, str(a['positivasubtotal']))
	p.drawString(170+j*3, columna-15*et, str(a['rimacsubtotal']))
	p.drawString(220+j*4, columna-15*et, str(a['pacificosubtotal']))
	p.drawString(250+j*5, columna-15*et, str(a['phdisubtotal']))
	
	et=13

	p.drawString(20, columna-15*et, "Total")
	p.drawString(70+j, columna-15*et, str(a['mapfresubtotal']))
	p.drawString(120+j*2, columna-15*et, str(a['positivatotal']))
	p.drawString(170+j*3, columna-15*et, str(a['rimactotal']))
	p.drawString(220+j*4, columna-15*et, str(a['pacificototal']))
	p.drawString(250+j*5, columna-15*et, str(a['phditotal']))

	columna = columna -40



	p.setFillColorRGB(1,0.54902,0)
	p.rect(20,columna-140,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(0,0,0)
	p.drawString(122, columna-140+3, "Coberturas")

	for i in range(0,18):

		c[i]['descripcion'] = c[i]['descripcion'].encode('ascii','ignore').encode('ascii','replace')
		c[i]['mapfre'] = c[i]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
		c[i]['positiva']= c[i]['positiva'].encode('ascii','ignore').encode('ascii','replace')
		c[i]['rimac']= c[i]['rimac'].encode('ascii','ignore').encode('ascii','replace')

		#c[i]['pacifico']= c[i]['pacifico'].encode('ascii','ignore').encode('ascii','replace')
		c[i]['hdi']= c[i]['hdi'].encode('ascii','ignore').encode('ascii','replace')
		
		p.drawString(20, columna-160-15*i, str(c[i]['descripcion'])[0:30])
		p.drawString(70+50, columna-160-15*i, str(c[i]['mapfre'])[0:30])
		p.drawString(120+50*2, columna-160-15*i, str(c[i]['positiva'])[0:30])
		p.drawString(170+50*3, columna-160-15*i, str(c[i]['rimac'])[0:30])
		#p.drawString(250+50*4, 700-15*i, str(c[i]['pacifico']))
		p.drawString(250+50*5, columna-160-15*i, str(c[i]['hdi'])[0:30])

	columna =columna-15*i


	p.setFillColorRGB(1,0.54902,0)
	p.rect(20,columna-180,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(0,0,0)
	p.drawString(22, columna-180+3, "Deducibles")
	
	for k in range(0,14):


		d[k]['deducible'] = d[k]['deducible'].encode('ascii','ignore').encode('ascii','replace')
		d[k]['mapfre'] = d[k]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
		d[k]['positiva']= d[k]['positiva'].encode('ascii','ignore').encode('ascii','replace')
		d[k]['rimac']= d[k]['rimac'].encode('ascii','ignore').encode('ascii','replace')
		#d[i]['pacifico']= d[i]['pacifico'].encode('ascii','ignore').encode('ascii','replace')
		d[k]['hdi']= d[k]['hdi'].encode('ascii','ignore').encode('ascii','replace')

		p.drawString(20, columna-200-15*k, str(d[k]['deducible'])[0:30])
		p.drawString(70+50, columna-200-15*k, str(d[k]['mapfre'])[0:30])
		p.drawString(120+50*2, columna-200-15*k, str(d[k]['positiva'])[0:30])
		p.drawString(170+50*3, columna-200-15*k, str(d[k]['rimac'])[0:30])
		#p.drawString(250+50*4, 320-15*i, str(d[i]['pacifico']))
		p.drawString(250+50*5, columna-200-15*k, str(d[k]['hdi'])[0:30])

	columna = columna-15*k


	p.setFillColorRGB(1,0.54902,0)
	p.rect(20,columna-220,7.5*inch,.15*inch, fill=1)
	p.setFillColorRGB(0,0,0)
	p.drawString(22, columna-220+3, "Servicios")
	

	for sk in range(0,5):


		s[sk]['services'] = s[sk]['services'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['mapfre'] = s[sk]['mapfre'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['positiva']= s[sk]['positiva'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['rimac']= s[sk]['rimac'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['pacifico']= s[sk]['pacifico'].encode('ascii','ignore').encode('ascii','replace')
		s[sk]['hdi']= s[sk]['hdi'].encode('ascii','ignore').encode('ascii','replace')

		p.drawString(20, columna-240-15*sk, str(s[sk]['services'])[0:30])
		p.drawString(70+50, columna-240-15*sk, str(s[sk]['mapfre'])[0:30])
		p.drawString(120+50*2, columna-240-15*sk, str(s[sk]['positiva'])[0:30])
		p.drawString(170+50*3, columna-240-15*sk, str(s[sk]['rimac'])[0:30])
		p.drawString(220+50*4, columna-240-15*sk, str(s[sk]['pacifico'])[0:25])
		p.drawString(250+50*5, columna-240-15*sk, str(s[sk]['hdi'])[0:30])


	

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response

@csrf_exempt
def recibetasas(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/cotiza.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def recibecliente(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/cliente.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def recibeservicios(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/servicios.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def marcacsv(request):

	ri = Marca.objects.all()

	response = HttpResponse(content_type='text/xls')

	response['Content-Disposition'] = 'attachment; filename="Marcas.xls"'

	writer = csv.writer(response)

	data = 'Marca','Origen'

	writer.writerow(data)

	for r in ri:

		datos= r.name_marca,r.origen

		writer.writerow(datos)

	return response

@csrf_exempt
def gpscsv(request,aseguradora):

	g=Gps.objects.filter(id_aseg=aseguradora)



	response = HttpResponse(content_type='text/xls')

	response['Content-Disposition'] = 'attachment; filename="Gps.xls"'

	writer = csv.writer(response)

	data = 'Marca','Modelo','Tipo','Value'

	writer.writerow(data)

	for r in g:

		print r.id_auto_id

		datos= r.id_auto_id,r.id_auto.id_marca.name_marca,r.id_auto.id_modelo.name_model,r.id_auto.id_tipo.clase,r.value


		writer.writerow(datos)

	return response



@csrf_exempt
def riesgocsv(request,aseguradora):

	ri = RiesgAseg.objects.filter(aseguradora=aseguradora)

	#values('id_model_id','id_model__id_modelo__name_model','id_model__id_marca__name_marca','id_riesg__tipo_riesgo')

	response = HttpResponse(content_type='text/xls')

	response['Content-Disposition'] = 'attachment; filename="Riesgos.xls"'



	writer = csv.writer(response)

	data = 'Aseguradora','Id','Modelo','Marca','Riesgo','Riesgo'

	writer.writerow(data)

	for r in ri:

		modelo = None
		marca= None
		riesgo= None
		aseguradora = None
		programa = None

		if r.aseguradora_id:

			aseguradora = r.aseguradora.name_asegurad

		if r.id_model_id:

			if AutoValor.objects.filter(id=r.id_model_id).count()>0:

				modelo = r.id_model.id_modelo.name_model

				if Marca.objects.filter(id_marca=r.id_model.id_marca_id).count()>0:

					marca = r.id_model.id_marca.name_marca

		if r.id_riesg_id:

			riesgo = r.id_riesg.tipo_riesgo


		if r.programa_id:

			programa = r.programa.program


		datos= aseguradora,r.id_model_id,modelo,marca,riesgo

		writer.writerow(datos)

		# print r

		# if AutoValor.objects.filter(id=r['id_model_id']).count()>0:


		# 	datos = r['id_model__id_modelo__name_model'],r['id_model__id_marca__name_marca'],r['id_riesg__tipo_riesgo']


		# 	print datos


		# 	# datos = x['id'],x['tipo__clase'],x['antigued'],x['programa__program'],x['id_cob__descripcion'],x['id_aseg__name_asegurad'],x['id_uso__uso'],x['modalidad__name_modalidad'],x['value']
			
		# 	writer.writerow(datos)

	return response

@csrf_exempt
def coberturacsv(request,aseguradora):

	ta = CobertAsegur.objects.all()

	response = HttpResponse(content_type='text/xls')

	response['Content-Disposition'] = 'attachment; filename="Coberturas.csv"'

	writer = csv.writer(response)

	data = 'Cobertura','Programa'

	writer.writerow(data)

	for r in ta:

		print r.id_cob_id

		if r.id_cob_id:

			r.id_cob.descripcion = r.id_cob.descripcion.encode('ascii','ignore')

			r.id_cob.descripcion = r.id_cob.descripcion.encode('ascii','replace')

		r.value = r.value.encode('ascii','ignore')

		r.value = r.value.encode('ascii','replace')


		data = r.id_cob_id,'|',r.id_cob.descripcion,'|',r.programa.program,'|',r.tipo.clase,'|',r.value


		#data = t.id_aseg.name_asegurad,programa,riesgo,uso,tipo,marca,modelo,categoria,t.origen,t.ubicacion,t.anio,t.value

		writer.writerow(data)

	return response



@csrf_exempt
def deduciblecsv(request,aseguradora):

	ta = DeducAsegur.objects.filter(id_aseg=aseguradora)

	response = HttpResponse(content_type='text/xls')

	response['Content-Disposition'] = 'attachment; filename="Deducible.csv"'

	writer = csv.writer(response)

	data = 'Cobertura','Programa'

	writer.writerow(data)

	for r in ta:
		print 'ooo',r.id,r.id_deduc_id

		if r.id_deduc_id:

			r.id_deduc.deducible = r.id_deduc.deducible.encode('ascii','ignore')

			r.id_deduc.deducible = r.id_deduc.deducible.encode('ascii','replace')

		r.value = r.value.encode('ascii','ignore')

		r.value = r.value.encode('ascii','replace')

		r.programa.program = r.programa.program.encode('ascii','ignore')

		r.programa.program = r.programa.program.encode('ascii','replace')

		r.tipo.clase= r.tipo.clase.encode('ascii','ignore')

		r.tipo.clase= r.tipo.clase.encode('ascii','replace')

		r.riesgo.tipo_riesgo= r.riesgo.tipo_riesgo.encode('ascii','ignore')

		r.riesgo.tipo_riesgo= r.riesgo.tipo_riesgo.encode('ascii','replace')


		data = r.id_deduc_id,'@',r.id_deduc.deducible,'@',r.programa.program,'@',r.tipo.clase,'@',r.riesgo.tipo_riesgo,'@',r.id_uso.uso,'@',r.value


		#data = t.id_aseg.name_asegurad,programa,riesgo,uso,tipo,marca,modelo,categoria,t.origen,t.ubicacion,t.anio,t.value

		writer.writerow(data)

	return response

@csrf_exempt
def serviciocsv(request,aseguradora):

	ta = ServicAsegur.objects.filter(id_aseg=aseguradora)

	response = HttpResponse(content_type='text/xls')

	response['Content-Disposition'] = 'attachment; filename="Coberturas.csv"'

	writer = csv.writer(response)

	data = 'Cobertura','Programa'

	writer.writerow(data)

	for r in ta:

		if r.id_serv_id:

			r.id_serv.services = r.id_serv.services.encode('ascii','ignore')

			r.id_serv.services = r.id_serv.services.encode('ascii','replace')

		r.value = r.value.encode('ascii','ignore')

		r.value = r.value.encode('ascii','replace')


		data = r.id_serv_id,'|',r.id_serv.services,'|',r.id_program.program,'|',r.tipo.clase,'|',r.value


		#data = t.id_aseg.name_asegurad,programa,riesgo,uso,tipo,marca,modelo,categoria,t.origen,t.ubicacion,t.anio,t.value

		writer.writerow(data)

	return response

@csrf_exempt
def tasascsv(request,aseguradora):

	ta = TasaAsegur.objects.filter(id_aseg=aseguradora,programa_id=19)

	response = HttpResponse(content_type='text/xls')

	response['Content-Disposition'] = 'attachment; filename="Tasas.xls"'

	writer = csv.writer(response)

	data = 'Aseguradora','Programa','Riesgo','Uso','Tipo','Marca','Modelo','Caegoria','Origen','Ubicacion','Anio','Valor'

	writer.writerow(data)

	for t in ta:

		riesgo=None
		uso=None
		programa=None
		tipo=None
		modelo=None
		categoria=None
		marca=None




		if t.riesgo_id:

			t.riesgo.tipo_riesgo = t.riesgo.tipo_riesgo.encode('ascii','ignore')

			t.riesgo.tipo_riesgo = t.riesgo.tipo_riesgo.encode('ascii','replace')

			riesgo=t.riesgo.tipo_riesgo

		if t.id_uso_id:

			t.id_uso.uso = t.id_uso.uso.encode('ascii','ignore')

			t.id_uso.uso = t.id_uso.uso.encode('ascii','replace')

			uso = t.id_uso.uso

		if t.programa_id:

			t.programa.program = t.programa.program.encode('ascii','ignore')

			t.programa.program = t.programa.program.encode('ascii','replace')

			programa= t.programa.program

		if t.tipo_id:

			t.tipo.clase = t.tipo.clase.encode('ascii','ignore')

			t.tipo.clase = t.tipo.clase.encode('ascii','replace')

			tipo=t.tipo.clase

		if AutoValor.objects.filter(id=t.modelo_id).count()>0:

			if t.modelo_id:

				marca = t.modelo.id_marca.name_marca.encode('ascii','ignore')

				marca = marca.encode('ascii','replace')

			if t.modelo_id:

				t.modelo.id_modelo.name_model = t.modelo.id_modelo.name_model.encode('ascii','ignore')

				t.modelo.id_modelo.name_model = t.modelo.id_modelo.name_model.encode('ascii','replace')

				modelo=t.modelo.id_modelo.name_model

		if t.categoria_id:

			t.categoria.categoria = t.categoria.categoria.encode('ascii','ignore')

			t.categoria.categoria = t.categoria.categoria.encode('ascii','replace')

			categoria=t.categoria.categoria


		data = t.id_aseg.name_asegurad,t.id_aseg.name_asegurad,programa,riesgo,uso,tipo,marca,modelo,categoria,t.origen,t.ubicacion,t.anio,t.value

		# datos = str(data).encode('ascii','ignore')

		# datos = datos.encode('ascii','replace')


		writer.writerow(data)

	return response


@csrf_exempt
def modeloscsv(request):

	ri = AutoValor.objects.all().values('id','id_modelo__name_model','id_marca__name_marca','id_tipo__clase','traccion').order_by('id_tipo__clase')

	response = HttpResponse(content_type='text/xls')

	response['Content-Disposition'] = 'attachment; filename="Modelos.xls"'

	datos = 'id','modelo','marca','clase','traccion'
		
	writer = csv.writer(response)

	writer.writerow(datos)

	for r in ri:

		modelo = r['id_modelo__name_model'].encode('ascii','ignore')

		modelo = modelo.encode('ascii','replace')

		marca = r['id_marca__name_marca'].encode('ascii','ignore')

		marca = marca.encode('ascii','replace')

		clase = r['id_tipo__clase'].encode('ascii','ignore')

		clase = clase.encode('ascii','replace')

		datos = r['id'],modelo,marca,clase,r['traccion']

		# datos = x['id'],x['tipo__clase'],x['antigued'],x['programa__program'],x['id_cob__descripcion'],x['id_aseg__name_asegurad'],x['id_uso__uso'],x['modalidad__name_modalidad'],x['value']
			
		writer.writerow(datos)

	return response

@csrf_exempt
def corrige(request):

	mo=Clase.objects.all()

	for m in mo:

		m.clase = m.clase.encode('ascii','ignore')

		m.clase = m.clase.encode('ascii','replace')

		m.clase

		m.save()

	return HttpResponse('nologeado', content_type="application/json")


@csrf_exempt
def recibecoberturas(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/coberturas.json', 'w')
	f.write(data)
	f.close()



	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def recibegps(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/gps.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")


@csrf_exempt
def recibefinanciamiento(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/financiamiento.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")

@csrf_exempt
def recibededucibles(request):

	data = json.loads(request.body)

	data = json.dumps(data)

	f = open('/var/www/html/deducibles.json', 'w')
	f.write(data)
	f.close()

	return HttpResponse('nologeado', content_type="application/json")



@csrf_exempt
def subir(request):

	send_mail('Hermes','Evento Enviado','cotiza@hermes.pe', ['joelunmsm@gmail.com'], fail_silently=False)

	return HttpResponse('mmmmmmmmm', content_type="application/json")

def generapdf(request):
	# Create the HttpResponse object with the appropriate PDF headers.

	for i in range(0,27):

		TasaAsegur.objects.filter(anio=28-i).update(anio=0+i)
	


	return HttpResponse('total', content_type="application/json")



@csrf_exempt
def estadologin(request):

	if request.user.is_authenticated():

		return HttpResponse('logeado', content_type="application/json")

	else:

		return HttpResponse('nologeado', content_type="application/json")




@csrf_exempt
def exportarcobertura(request,data):



			cobertura = str(data).split('a')[0].split('x')

			aseguradora = str(data).split('a')[1].split('x')


			#['1'] ['1', '1'] <type 'list'> <type 'list'>

			
			c =CobertAsegur.objects.filter(programa_id__in=cobertura,id_aseg_id__in=aseguradora).values('id','tipo__clase','antigued','programa__program','id_cob__descripcion','id_aseg__name_asegurad','id_uso__uso','modalidad__name_modalidad','value').order_by('-id')
			
			response = HttpResponse(content_type='text/csv')
			
			response['Content-Disposition'] = 'attachment; filename="Coberturas.csv"'

			writer = csv.writer(response)


			for x in c:

				#x['text_message'] = x['text_message'].encode('ascii','ignore')

				# x['text_message'] = x['text_message'].encode('ascii','replace')

				datos = x['id'],x['tipo__clase'],x['antigued'],x['programa__program'],x['id_cob__descripcion'],x['id_aseg__name_asegurad'],x['id_uso__uso'],x['modalidad__name_modalidad'],x['value']
				
				writer.writerow([datos])



			return response


@csrf_exempt
def exportarriesgo(request,data):

		auto = AutoValor.objects.all().values('id','id_modelo','id_modelo__name_model','id_marca__name_marca')

		for i in range(len(auto)):

			auto[i]['riesgo'] = ''

			auto[i]['aseguradora'] = ''

			if RiesgAseg.objects.filter(aseguradora_id=data,id_model_id=auto[i]['id_modelo']).values('id_riesg__tipo_riesgo').count()>0:

				auto[i]['riesgo'] = RiesgAseg.objects.filter(aseguradora_id=data,id_model_id=auto[i]['id_modelo']).values('id_riesg__tipo_riesgo')[0]['id_riesg__tipo_riesgo']

				auto[i]['aseguradora'] = RiesgAseg.objects.filter(aseguradora_id=data).values('aseguradora__name_asegurad')[0]['aseguradora__name_asegurad']



		response = HttpResponse(content_type='text/csv')
		
		response['Content-Disposition'] = 'attachment; filename="Riesgos.csv"'

		writer = csv.writer(response)


		for a in auto:


			datos = a['id'],a['riesgo'],a['id_modelo__name_model'],a['id_marca__name_marca'],a['aseguradora']
			
			writer.writerow([datos])



		return response



@csrf_exempt
def exportardeducible(request,data):

	

			cobertura = str(data).split('a')[0].split('x')

			aseguradora = str(data).split('a')[1].split('x')

			
			c =DeducAsegur.objects.filter(id_deduc_id__in=cobertura,id_aseg_id__in=aseguradora).values('riesgo__tipo_riesgo','programa__program','id_deduc__deducible','id_aseg__name_asegurad','id_uso__uso','tipo__clase','value','modalidad__name_modalidad','value').order_by('-id')

			response = HttpResponse(content_type='text/csv')
			
			response['Content-Disposition'] = 'attachment; filename="Deducible.csv"'

			writer = csv.writer(response)


			for x in c:

				#x['text_message'] = x['text_message'].encode('ascii','ignore')

				# x['text_message'] = x['text_message'].encode('ascii','replace')

				datos = x['riesgo__tipo_riesgo'],x['programa__program'],x['id_deduc__deducible'],x['id_aseg__name_asegurad'],x['id_uso__uso'],x['tipo__clase'],x['value'],x['modalidad__name_modalidad'],x['value']


				writer.writerow([datos])



			return response

@csrf_exempt
def tasaadmin(request):


		if request.method == 'POST':


			demision = Parametros.objects.get(id=1).d_emision

			igv = Parametros.objects.get(id=1).igv

			monto = json.loads(request.body)['monto']['precio']
			data = json.loads(request.body)['data']



			tasahdi = data['tasahdi']
			tasarimac = data['tasarimac']
			tasapositiva = data['tasapositiva']
			tasapacifico = data['tasapacifico']
			tasamapfre = data['tasamapfre']

			aseguradora = Aseguradora.objects.all().values('id_asegurad','name_asegurad').order_by('name_asegurad')

			for i in range(len(aseguradora)):

				if aseguradora[i]['id_asegurad'] == 3:

					aseguradora[i]['tasahdi'] = round(float(tasahdi),2)

					aseguradora[i]['hdi'] = round(float(tasahdi)/100*float(monto),2)
					
					aseguradora[i]['phdisubtotal'] = round((100+float(demision))*float(aseguradora[i]['hdi'])/100,2)

					aseguradora[i]['phditotal'] = round((100+float(igv))*aseguradora[i]['phdisubtotal']/100,2)


				if aseguradora[i]['id_asegurad'] == 1:

					aseguradora[i]['tasapositiva'] = round(float(tasapositiva),2)

					aseguradora[i]['positiva'] = round(float(tasapositiva)/100*float(monto),2)

					aseguradora[i]['positivasubtotal'] = round((100+float(demision))*aseguradora[i]['positiva']/100,2)

					aseguradora[i]['positivatotal'] = round((100+float(igv))*aseguradora[i]['positivasubtotal']/100,2)
			
				if aseguradora[i]['id_asegurad'] == 2:

	
					aseguradora[i]['tasapacifico'] = round(float(tasapacifico),2)

					aseguradora[i]['pacifico'] = round(float(tasapacifico)/100*float(monto),2)

					aseguradora[i]['pacificosubtotal'] = round((100+float(demision))*aseguradora[i]['pacifico']/100,2)

					aseguradora[i]['pacificototal'] = round((100+int(igv))*aseguradora[i]['pacificosubtotal']/100,2)
			


				else:

					aseguradora[i]['pacifico'] = 'Consultar en la URL:'

					aseguradora[i]['pacificosubtotal'] = 'http://pacifico.com'

					aseguradora[i]['pacificototal'] = ''


				if aseguradora[i]['id_asegurad'] == 4:


						aseguradora[i]['tasamapfre'] = round(float(tasamapfre),2)

						aseguradora[i]['mapfre'] = round(float(tasamapfre)/100*float(monto),2)

						aseguradora[i]['mapfresubtotal'] = round((100+float(demision))*aseguradora[i]['mapfre']/100,2)

						aseguradora[i]['mapfretotal'] = round((100+float(igv))*aseguradora[i]['mapfresubtotal']/100,2)



				if aseguradora[i]['id_asegurad'] == 5:

						
						aseguradora[i]['tasarimac'] = round(float(tasarimac),2)

						# Bajo Riesgo



						aseguradora[i]['rimac'] = round(float(tasarimac)/100*float(monto),2)

						aseguradora[i]['rimacsubtotal'] = round((100+float(demision))*aseguradora[i]['rimac']/100,2)

						aseguradora[i]['rimactotal'] = round((100+float(igv))*aseguradora[i]['rimacsubtotal']/100,2)



			data_dict = ValuesQuerySetToDict(aseguradora)

			data = json.dumps(data_dict)


			return HttpResponse(data, content_type="application/json")



	


@csrf_exempt
def logearse(request):

	if request.user.is_authenticated():

		return HttpResponse('logeado', content_type="application/json")

	else:

		if request.method == 'POST':

			data = json.loads(request.body)

			user = json.loads(request.body)['username']
			
			psw = json.loads(request.body)['password']

			user = authenticate(username=user, password=psw)

			if user is not None:

				if user.is_active:

					login(request, user)

					return HttpResponse('logeado', content_type="application/json")

			else:
					
					return HttpResponse('noautorizado', content_type="application/json")
		


		return HttpResponse('nologeado', content_type="application/json")


@csrf_exempt
def parametros(request):

	data = request.body


	igv = data['igv']
	demision = data['demision']

	Parametros(igv=igv,d_emision=demision).save()

	return HttpResponse('data', content_type="application/json")


	fullname = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=50, blank=True)
	chose_informat = models.IntegerField()


@csrf_exempt
def customers(request):

	d=Clientes.objects.all().values('id_cliente','fullname','email','chose_informat').order_by('id_cliente')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def listparametros(request):

	p= Parametros.objects.all().values('igv','d_emision').order_by('-id')

	data_dict = ValuesQuerySetToDict(p)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listprimas(request):

	p= Primas.objects.all().values('id','aseguradora__name_asegurad','riesgo__tipo_riesgo','programa__program','primaminima').order_by('-id')

	data_dict = ValuesQuerySetToDict(p)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def addigv(request):

	data =  json.loads(request.body)

	igv = data['igv']
	demision = data['demision']

	p = Parametros.objects.get(id=1)
	p.igv = igv
	p.d_emision = demision
	p.save()

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def asegprogram(request,aseguradora,modelo,uso,marca,tipo,precio):


	aseg = ProgAseg.objects.filter(id_aseg_id=aseguradora).values('id_prog','id_prog__program').order_by('id_prog__program')

	tiponame = AutoValor.objects.get(id_modelo_id=modelo,id_marca_id=marca,id_tipo_id=tipo).id_tipo.clase

	id_auto_valor = AutoValor.objects.get(id_modelo_id=modelo,id_marca_id=marca,id_tipo_id=tipo).id

	origenname = Marca.objects.get(id_marca=marca).origen

	usoname = Uso.objects.get(id_uso=uso).uso

	marcaname = Marca.objects.get(id_marca=marca).name_marca

	restringido =False

	if int(aseguradora)==5:

		progrimac =[]



		traccion = AutoValor.objects.filter(id_modelo_id=modelo,id_marca_id=marca,id_tipo_id=tipo,traccion=1).count()

		if traccion>0 and usoname=='Particular':

			progrimac.append(7)


		if int(uso) == 1: #Particular

			progrimac.append(2)

			progrimac.append(25)

			progrimac.append(26)

		if tiponame=='Pick-UP':

			progrimac.append(6)

			progrimac.remove(2)

			progrimac.remove(25)

			progrimac.remove(26)

		if int(uso) == 20: # Taxis

			progrimac.append(11)

		if origenname =='Chino':

			progrimac.append(10)

		if usoname=='Taxi/Publico':

			progrimac.append(11)

		if usoname=='Transporte de Personal, Turistico, Escolar':

			progrimac.append(12)

		if usoname =='Panel' and origenname=='Chino':

		 	progrimac.remove(12)

		if AutoValor.objects.filter(id=id_auto_valor,excluidorimac='Si').count()>0:

			restringido =True


		if (int(precio) >= 75000 and int(precio)<=4000) or origenname=='Chino' or restringido==True or (tiponame=='Van' and usoname=='Particular'):


			progrimac.remove(2)

			progrimac.remove(25)

			progrimac.remove(26)

		if int(precio)>60000 and tiponame=='Pick-UP':

			progrimac.remove(6)

		if int(precio)>60000 and int(precio)<=4000 or origenname=='Chino' :

			if 7 in progrimac:

				progrimac.remove(7)

		if (tiponame =='Microbus' or tiponame=='Omnibus' or tiponame=='Camion' or usoname=='Taxi/Publico' or int(precio)>=60000) and origenname=='Chino':

			progrimac.remove(10)

		aseg = ProgAseg.objects.filter(id_aseg_id=aseguradora,id_prog_id__in=progrimac).values('id_prog','id_prog__program')

	if int(aseguradora)==1: #Positiva

		prog =[]

		prog.append(4)

		#Comercial

		if usoname=='Comercial':

			prog.append(28)

			prog.remove(4)

		if usoname =='Taxi/Publico':

			prog.append(29)

			prog.remove(4)

		if usoname=='Carga':

			prog.append(31)

			prog.remove(4)

		if usoname=='Transporte de Personal, Turistico, Escolar':

			prog.append(30)

			prog.remove(4)


		aseg = ProgAseg.objects.filter(id_aseg_id=aseguradora,id_prog_id__in=prog).values('id_prog','id_prog__program')




	if int(aseguradora)==4: #Mapfre

		prog = []

		#### Dorada

		if tiponame=='Auto' and usoname=='Particular':

			prog.append(1)

			prog.append(24)

		if tiponame=='Rural' and usoname=='Particular':

			prog.append(1)

			prog.append(24)

		if origenname=='Chino':

			prog.append(1)

			prog.append(24)

		if origenname=='Pick-UP':


			prog.remove(1)

			prog.remove(24)

		## Dorada Economica

		if marcaname == 'TOYOTA' or marcaname =='NISSAN' or marcaname=='KIA' or marcaname=='CHEVROLET' or marcaname =='GEELY' or marcaname=='LIFAN' or marcaname=='CHERY' or marcaname=='GREAT WALL' or marcaname=='JAC' or marcaname=='INCAPOWER' or marcaname=='BYD' or marcaname=='CHANGE' or marcaname=='HAFEI':

			if (tiponame=='Auto' and usoname=='Particular') or (tiponame=='Station Wagon' and usoname=='Particular') or (tiponame=='Rural' and usoname=='Particular') :

				prog.append(5)

			if origenname=='Pick-UP':

				prog.append(5)

			if origenname=='Chino':

				prog.append(5)

		## Dorada Pickup

		if (tiponame == 'Pick-UP' and usoname =='Particular') or usoname=='Comercial' or usoname =='Transporte de Personal, Turistico, Escolar':

			prog.append(22)

		## Taxi Individual

		if(tiponame=='Rural' and usoname=='Taxi/Publico') or (tiponame=='Auto' and usoname=='Taxi/Publico') or (tiponame=='Station Wagon' and usoname=='Taxi/Publico') or (origenname=='Chino' and usoname=='Taxi/Publico'):

			prog.append(21)

		if tiponame == 'Pick-UP' and usoname=='Taxi/Publico':


			prog.remove(21)

		## Program Transporte Personal

		if (tiponame == 'Rural' or tiponame == 'Omnibus' or tiponame=='Microbus') and usoname=='Transporte de Personal, Turistico, Escolar':

			prog.append(19)





		aseg = ProgAseg.objects.filter(id_aseg_id=aseguradora,id_prog_id__in=prog).values('id_prog','id_prog__program')



	data_dict = ValuesQuerySetToDict(aseg)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def pdfx(request):

	urlx = request.body



	f = open('/var/www/pdf.txt', 'a')
	f.write(str(urlx)+'\n')
	f.close()


	os.system('wkhtmltopdf '+urlx+' /var/www/html/output.pdf')

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def marca(request):

	d=Marca.objects.all().values('id_marca','name_marca','orden').order_by('orden')

	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def modelo(request,id_marca):

	d=AutoValor.objects.filter(id_marca_id=id_marca).values('id_modelo','id_modelo__name_model','id_marca').annotate(model=Max('id_modelo__name_model')).order_by('id_modelo__name_model')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listmodelo(request):

	d=Modelo.objects.all().values('id_model','name_model').order_by('-id_model');
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def clase(request):
	
	d=Clase.objects.all().values('id_clase','clase').order_by('id_clase')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def usos(request,tipo):
	
	d=Tipouso.objects.filter(tipo_id=tipo).values('id','uso__uso','uso')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def catemodelo(request,modelo):


	modelos = AutoValor.objects.filter(id_modelo=modelo).values('id_modelo','id_modelo__name_model','id_marca__name_marca')

	for i in range(len(modelos)):

		if modelos[i]['id_marca__name_marca'] == 'Toyota' or modelos[i]['id_marca__name_marca'] == 'Nissan' :

			cat = 2

		else:

			cat = 1

	return HttpResponse(cat, content_type="application/json")


@csrf_exempt
def claseModelo(request,id_model):

	d=AutoValor.objects.filter(id_modelo=id_model).values('id','id_tipo','id_tipo__clase','id_modelo')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def riesgosclase(request):

	d = RiesgAseg.objects.all().values('aseguradora__name_asegurad','id_model__id_marca__name_marca','id_model__id_tipo__clase','id_riesg__tipo_riesgo','id_model__id_modelo__name_model','id').order_by('-id');
	
	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def datosfiltro(request,id_cliente):

	d = Clientes.objects.filter(id_cliente=id_cliente).values('id_cliente','fullname','email','celular','chose_marca__name_marca','chose_modelo__name_model','chose_tipo__clase','chose_modalid__name_modalidad','chose_uso__uso','chose_anio__anio_antig','chose_ubicl','chose_ubicp','chose_informat','value');
	
	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def categorias(request):

	d=Categorias.objects.all().values('id_categ','categoria').order_by('id_categ')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def anio(request):

	d=Anio.objects.all().values('id_anio','anio_antig').order_by('-id_anio')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def programas(request):

	d=Programa.objects.all().values('id_program','program').order_by('id_program')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def aseguradoras(request):

	d=Aseguradora.objects.all().values('id_asegurad','name_asegurad').order_by('id_asegurad')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def coberturas(request):

	d=Cobertura.objects.all().values('id_cobert','descripcion').order_by('id_cobert')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def deducciones(request):

	d=Deducibles.objects.all().values('id_deduc','deducible').order_by('id_deduc')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def financiamiento(request):

	d=FinanAsegu.objects.values('id','id_finan','id_finan__financiamiento','id_aseg','id_aseg__name_asegurad','cuota','tea')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


def pdfmargarita(request):


	return render(request, 'pdfmargarita.html')



def generate_pdf_view(request):

	try:
		# create an API client instance
		client = pdfcrowd.Client("username", "apikey")

		# convert an HTML file
		output_file = open('file.pdf', 'wb')
		client.convertFile('/var/www/cotizacion/frontend/resultadofiltro.html', output_file)
		output_file.close()

	except pdfcrowd.Error, why:
		print('Failed: {}'.format(why))

	return HttpResponse(output_file, content_type="application/json")

@csrf_exempt
def fiiiii(request):

	data = json.loads(request.body)


	primarimac = data['mapfretotal']
	primahdi = data['hditotal']
	primapacifico = data['pacificototal']
	primapositiva = data['positivatotal']
	primamapfre =data['mapfretotal']

	#{u'orderId': u'865', u'anio': u'29', u'tipo': u'1', u'uso': u'1', u'precio': u'250', u'marca': u'90', u'modelo': u'6800', u'programa': u'1z2z4z9', u'modalidad': u'2'}

	financiamiento = Financiamiento.objects.all().values('id_financ','financiamiento').order_by('id_financ')


	demision = Parametros.objects.get(id=1).d_emision

	igv = Parametros.objects.get(id=1).igv


	for i in range(len(financiamiento)):

		



		# Mapfre

		f=FinanAsegu.objects.get(id_finan_id=financiamiento[i]['id_financ'],id_aseg_id=4)

		valor = round((primamapfre*f.tea/100+primamapfre)/int(f.cuota),2)

		financiamiento[i]['mapfre'] = str(f.cuota) +' '+str('cuotas de $/.')+str(valor)

		#Rimac

		f=FinanAsegu.objects.get(id_finan_id=financiamiento[i]['id_financ'],id_aseg_id=5)

		valor = round((primarimac*f.tea/100+primarimac)/int(f.cuota),2)

		financiamiento[i]['rimac'] = str(f.cuota) +' '+str('cuotas de $/.')+str(valor)

		#Postiva

		f=FinanAsegu.objects.get(id_finan_id=financiamiento[i]['id_financ'],id_aseg_id=1)

		if int(f.cuota)>0:

			valor = round((primapositiva*f.tea/100+primapositiva)/int(f.cuota),2)

			financiamiento[i]['positiva'] = str(f.cuota) +' '+str('cuotas de $/.')+str(valor)

		else:


			financiamiento[i]['positiva']='No Aplica'


		#Pacifico

		f=FinanAsegu.objects.get(id_finan_id=financiamiento[i]['id_financ'],id_aseg_id=2)

		valor = round((primapacifico*f.tea/100+primapacifico)/int(f.cuota),2)

		financiamiento[i]['pacifico'] = str(f.cuota) +' '+str('cuotas de $/.')+str(valor)


		#HDI

		f=FinanAsegu.objects.get(id_finan_id=financiamiento[i]['id_financ'],id_aseg_id=3)

		valor = round((primahdi*f.tea/100+primahdi)/int(f.cuota),2)

		financiamiento[i]['hdi'] = str(f.cuota) +' '+str('cuotas de $/.')+str(valor)




	data_dict = ValuesQuerySetToDict(financiamiento)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def primaneta(request,descuento):

	data = json.loads(request.body)

	# PrimaNeta {u'orderId': u'618', u'anio': u'29', u'uso': u'1', u'precio': u'212', u'modelo': u'5506', u'programa': u'4z13z25z', u'modalidad': u'1'}

	monto = data['precio']

	marca=data['marca']

	orderId = data['orderId']

	uso = data['uso']

	usoname = Uso.objects.get(id_uso=uso).uso

	modelo = data['modelo']

	a = AutoValor.objects.get(id_marca_id=marca,id_modelo_id=modelo,id_tipo_id=data['tipo'])

	id_auto_valor = a.id

	origenname = a.id_marca.origen

	tiponame= a.id_tipo.clase

	modelname =a.id_modelo.name_model


	# for m in a:

	# 	tipo = m.id_tipo.id_clase

	modalidad = data['modalidad']

	anio = data['anio']

	programa = data['programa'].split('z')

	programarimac= programa[1]

	programamapfre = programa[0]

	programapositiva = programa[2]



	riesgohdi = 3
	riesgorimac= 7
	riesgopositiva = 3
	riesgomapfre = 3
	riesgopacifico = 6
	nameriesgomapfre = 'Bajo Riesgo'
	nameriesgorimac = 'Bajo Riesgo II'
	nameriesgopositiva = 'Bajo Riesgo'
	nameriesgohdi='Cat. I S/.700'
	nameriesgopacifico = 'Bajo Riesgo I'


	if RiesgAseg.objects.filter(id_model_id=id_auto_valor,aseguradora_id=3):

		t =RiesgAseg.objects.filter(id_model_id=id_auto_valor,aseguradora_id=3).values('id_riesg__tipo_riesgo')[0]['id_riesg__tipo_riesgo'].split(' ')[1]

		if t == 'I':

			if int(monto) <= 40000:

				nameriesgohdi = 'Cat. I S/.700'

			if int(monto) > 40000:

				nameriesgohdi = 'Alta Gama S/.2,500'

		if t == 'II':

			if int(monto) <= 40000:

				nameriesgohdi = 'Cat. II S/.700'

		if t=='Gama':

			nameriesgohdi = 'Alta Gama S/.2,500'

		if t=='Up':

			nameriesgohdi = 'Pick Up S/.1,100'


	if RiesgAseg.objects.filter(aseguradora_id=5,id_model_id=id_auto_valor):

		riesgorimac = RiesgAseg.objects.get(aseguradora_id=5,id_model_id=id_auto_valor).id_riesg.id_riesgo

		nameriesgorimac = RiesgAseg.objects.get(aseguradora_id=5,id_model_id=id_auto_valor).id_riesg.tipo_riesgo

		if int(monto)>50000:

			riesgorimac= 4

			nameriesgorimac ='Alto Riesgo I'

	if RiesgAseg.objects.filter(aseguradora_id=4,id_model_id=id_auto_valor):

		riesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=id_auto_valor).id_riesg.id_riesgo

		nameriesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=id_auto_valor).id_riesg.tipo_riesgo

		print 'riesgomapfre',riesgomapfre

	if RiesgAseg.objects.filter(aseguradora_id=1,id_model_id=id_auto_valor):

		riesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=id_auto_valor).id_riesg.id_riesgo

		nameriesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=id_auto_valor).id_riesg.tipo_riesgo

	print 'id_auto_valor',id_auto_valor

	if RiesgAseg.objects.filter(aseguradora_id=2,id_model_id=id_auto_valor):

		riesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=id_auto_valor).id_riesg.id_riesgo

		nameriesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=id_auto_valor).id_riesg.tipo_riesgo

	anio = int(Anio.objects.get(id_anio=anio).anio_antig)

	anioact = int(datetime.datetime.now().year)

	anio = anioact - anio

	demision = Parametros.objects.get(id=1).d_emision

	igv = Parametros.objects.get(id=1).igv

	aseguradora = Aseguradora.objects.all().values('id_asegurad','name_asegurad').order_by('name_asegurad')

	for i in range(len(aseguradora)):

		if aseguradora[i]['id_asegurad'] == 1:

			tasa = None



			## Programa Taxi

			if int(programapositiva) ==29:

				if usoname=='Taxi/Publico':

					tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),id_uso__uso=usoname,riesgo_id=riesgopositiva)

			## Comercial

			if int(programapositiva) ==28:

				tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),riesgo_id=riesgopositiva,programa_id=programapositiva)

				if origenname=='Chino':

					tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),origen='Chino',programa_id=programapositiva)

				if tiponame == 'Pick-UP':

					tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),tipo__clase='Pick-UP',programa_id=programapositiva)

					if origenname=='Chino':

						tasa = TasaAsegur.objects.get(id_aseg_id=1,tipo__clase='Pick-UP',origen='Chino',anio=int(anio),programa_id=programapositiva)

			#Uso Urbano Taxi

			if int(programapositiva) ==29:

				tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),riesgo_id=riesgopositiva,programa_id=programapositiva)

				if origenname =='Chino':

					tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),origen='Chino',programa_id=programapositiva)

			#Uso Urbano 

			if int(programapositiva) ==30:

				tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),programa_id=programapositiva)

			#Uso Carga

			if int(programapositiva) ==31:

				tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),id_uso__uso=usoname,programa_id=programapositiva)


			## Corporativo

			if int(programapositiva) ==4:

				tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),riesgo_id=riesgopositiva,programa_id=4)

				if origenname == 'Chino' and tiponame != 'Pick-UP':

					tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),origen='Chino',tipo__isnull=True,programa_id=4)

				if origenname == 'Chino' and tiponame == 'Pick-UP':

					tasa = TasaAsegur.objects.get(id_aseg_id=1,anio=int(anio),origen='Chino',tipo__clase='Pick-UP',programa_id=4)

				if origenname != 'Chino' and tiponame == 'Pick-UP':

					tasa = TasaAsegur.objects.filter(id_aseg_id=1,anio=int(anio),tipo__clase='Pick-UP',programa_id=4).exclude(origen='Chino')[0]

			if AutoValor.objects.filter(id=id_auto_valor,permitido='No Permitido').count()>0:

				tasa = None

			if tasa !=None:

				aseguradora[i]['tasapositiva'] = round(float(tasa.value),2)
				
				aseguradora[i]['positiva'] = round(aseguradora[i]['tasapositiva']*float(monto)/100,2)

				aseguradora[i]['positivasubtotal'] = round((aseguradora[i]['positiva'] + 3*aseguradora[i]['positiva']/100),2)

				aseguradora[i]['positivatotal'] = round((aseguradora[i]['positivasubtotal']+18*aseguradora[i]['positivasubtotal']/100),2)

				aseguradora[i]['riesgopositiva'] = nameriesgopositiva

				aseguradora[i]['idriesgopositiva'] = riesgopositiva

			else:

				aseguradora[i]['positiva']='No Aplica'

		if aseguradora[i]['id_asegurad'] == 2:

			tasa = None


			if TasaAsegur.objects.filter(id_aseg_id=2,anio=int(anio),riesgo_id=riesgopacifico).count()>0:

				tasa = TasaAsegur.objects.get(id_aseg_id=2,anio=int(anio),riesgo_id=riesgopacifico)

			if origenname == 'Chino':

				tasa = TasaAsegur.objects.get(id_aseg_id=2,anio=int(anio),origen=origenname)

			if usoname=='Taxi/Publico':

				tasa = None

			if tasa !=None:

				aseguradora[i]['tasapacifico'] = round(float(tasa.value),2)
				
				aseguradora[i]['pacifico'] = round(aseguradora[i]['tasapacifico']*float(monto)/100,2)

				aseguradora[i]['pacificosubtotal'] = round((aseguradora[i]['pacifico'] + 3*aseguradora[i]['pacifico']/100),2)

				aseguradora[i]['pacificototal'] = round((aseguradora[i]['pacificosubtotal']+18*aseguradora[i]['pacificosubtotal']/100),2)

				aseguradora[i]['riesgopacifico'] = nameriesgopacifico

				aseguradora[i]['idriesgopacifico'] = riesgopacifico

			else:

				aseguradora[i]['pacifico']='No Aplica'

		if aseguradora[i]['id_asegurad'] == 3:

			tasa=None

			e = AutoValor.objects.get(id=id_auto_valor).excluidohdi

			if e !='Si':

				tasa = TasaAsegur.objects.get(id_aseg_id=3,anio=int(anio),categoria__categoria=nameriesgohdi)

			if usoname=='Taxi/Publico':

				tasa = None

			if tasa !=None:

				aseguradora[i]['tasahdi'] = round(float(tasa.value),2)
				
				aseguradora[i]['hdi'] = round(aseguradora[i]['tasahdi']*float(monto)*3.25/100,2)

				aseguradora[i]['hdisubtotal'] = round((aseguradora[i]['hdi'] + 3*aseguradora[i]['hdi']/100),2)

				aseguradora[i]['hditotal'] = round((aseguradora[i]['hdisubtotal']+18*aseguradora[i]['hdisubtotal']/100),2)

				aseguradora[i]['riesgohdi'] = nameriesgohdi

				aseguradora[i]['idriesgohdi'] = riesgohdi

			else:

				aseguradora[i]['hdi']='No Aplica'

		##### Primas mapfre ######
		
		if aseguradora[i]['id_asegurad'] == 4:

			tasa = None

			if int(programamapfre)==1:

				if TasaAsegur.objects.filter(id_aseg_id=4,anio=int(anio),riesgo_id=riesgomapfre,programa_id=programamapfre).count()>0:

					tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),riesgo_id=riesgomapfre,programa_id=programamapfre)

				if origenname == 'Chino':

					tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),origen='Chino',programa_id=programamapfre)

			if int(programamapfre)==22:

				print 'usoname,programamapfre,origen',usoname,programamapfre

				tasa = TasaAsegur.objects.filter(id_aseg_id=4,anio=int(anio),id_uso__uso=usoname,programa_id=programamapfre).exclude(origen='Chino')[0]

				print tasa

				if origenname == 'Chino':

					tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),origen='Chino',id_uso__uso=usoname,programa_id=programamapfre)
				
			if int(programamapfre)==5:

				tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),riesgo_id=riesgomapfre,programa_id=programamapfre)

				if origenname == 'Chino':

					tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),origen='Chino',programa_id=programamapfre)

				if tiponame =='Pick-UP':

					tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),tipo__clase=tiponame,programa_id=programamapfre)

			if int(programamapfre)==14:

				tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),riesgo_id=riesgomapfre,programa_id=programamapfre)

				if tiponame =='Pick-UP':

					tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),tipo__clase=tiponame,programa_id=programamapfre)
				
			if int(programamapfre)==15:

				tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),tipo__clase=tiponame,programa_id=programamapfre)
				
			if int(programamapfre)==16:

				tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),tipo__clase=tiponame,programa_id=programamapfre)
				
			if int(programamapfre)==17:

				print 'Consultar'
				
			if int(programamapfre)==18:

				print 'Consultar'
				
			if int(programamapfre)==19:

				print 'Consultar'
				
			if int(programamapfre)==20:

				tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),riesgo_id=riesgomapfre,programa_id=programamapfre)
				
			if int(programamapfre)==21:

				if riesgomapfre == 2:

					riesgomapfre=3

				tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),riesgo_id=riesgomapfre,programa_id=programamapfre)

				if origenname == 'Chino':

					tasa = TasaAsegur.objects.get(id_aseg_id=4,anio=int(anio),origen='Chino',programa_id=programamapfre)

			if tasa !=None:

				aseguradora[i]['tasamapfre'] = round(float(tasa.value),2)
				
				aseguradora[i]['mapfre'] = round(aseguradora[i]['tasamapfre']*float(monto)/100,2)

				aseguradora[i]['mapfresubtotal'] = round((aseguradora[i]['mapfre'] + 3*aseguradora[i]['mapfre']/100),2)

				aseguradora[i]['mapfretotal'] = round((aseguradora[i]['mapfresubtotal']+18*aseguradora[i]['mapfresubtotal']/100),2)

				aseguradora[i]['riesgomapfre'] = nameriesgomapfre

				aseguradora[i]['idriesgomapfre'] = riesgomapfre

			else:

				aseguradora[i]['mapfre']='No Aplica'

		if int(aseguradora[i]['id_asegurad']) == 5:

			tasa = None

			if int(programarimac) == 2: # Corporativa Rimac

				if tiponame != 'Pick-UP':

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),riesgo_id=riesgorimac,programa_id=programarimac)

				if tiponame == 'Pick-UP' and anio >= 3:

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),tipo__clase=tiponame,programa_id=programarimac)

					nameriesgorimac ='Pick-UP'

				if tiponame == 'Pick-UP' and anio < 3:

					tasa = None

			if int(programarimac) == 25: # Corporativa Rimac comision 12.5

				tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),riesgo_id=riesgorimac,programa_id=programarimac)

			if int(programarimac) == 26: # Corporativa Rimac comision 15

				tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),riesgo_id=riesgorimac,programa_id=programarimac)


			if int(programarimac) == 7: # Programa 4x4


				tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),id_uso__uso=usoname,programa_id=programarimac)

				nameriesgorimac = 'Pick-UP '+usoname

			if int(programarimac) == 6: # Rimac Vehicular Pick Up

				if TasaAsegur.objects.filter(id_aseg_id=5,anio=int(anio),id_uso__uso=usoname,programa_id=programarimac).count()>0:

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),id_uso__uso=usoname,programa_id=programarimac)

					nameriesgorimac = usoname
				
				else:

					tasa =None

					nameriesgopositiva = None


			if int(programarimac) == 10:

				tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),tipo__clase=tiponame,programa_id=programarimac)

			if int(programarimac) == 11: # Programa taxi urbano

				if tiponame =='Auto':

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),tipo__clase='Auto',programa_id=programarimac)

				if 'Yaris' in modelname:

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),modelo__name_model__contains='Yaris',programa_id=programarimac)

				if 'Sail' in modelname:

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),modelo__name_model__contains='Sail',programa_id=programarimac)

				if origenname == 'Chino':

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),origen='Chino',programa_id=programarimac)

			if int(programarimac) == 12:

				if 'H1' in modeloname:

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),modelo__name_model__contains='H1',programa_id=programarimac)

				if tiponame == 'Panel':

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),tipo__clase='Panel',programa_id=programarimac)

			if int(programarimac) == 13:

				if tiponame =='Camion':

					tasa = TasaAsegur.objects.get(id_aseg_id=5,anio=int(anio),tipo__clase='Camion',programa_id=programarimac)



			if tasa != None:

				aseguradora[i]['tasarimac'] = round(float(tasa.value)*int(descuento)/100,2)
				
				aseguradora[i]['rimac'] = round(aseguradora[i]['tasarimac']*float(monto)/100,2)

				if int(monto) <= 350:

					if nameriesgorimac =='Bajo Riesgo I' or nameriesgorimac=='Bajo Riesgo II' or nameriesgorimac =='Alto Riesgo I':

						aseguradora[i]['rimac']= 350

					if nameriesgorimac =='Alto Riesgo II':

						aseguradora[i]['rimac']= 350

				if nameriesgorimac =='Pick-UP' and monto <= 375:

					aseguradora[i]['rimac']= 375

				aseguradora[i]['rimacsubtotal'] = round((aseguradora[i]['rimac'] + 3*aseguradora[i]['rimac']/100),2)

				aseguradora[i]['rimactotal'] = round((aseguradora[i]['rimacsubtotal']+18*aseguradora[i]['rimacsubtotal']/100),2)

				aseguradora[i]['riesgo'] = nameriesgorimac

				aseguradora[i]['idriesgo'] = riesgorimac

			else:

				aseguradora[i]['rimac'] = 'No Aplica'

				if AutoValor.objects.filter(id=id_auto_valor,excluidorimac='Si').count()>0:

					aseguradora[i]['rimac'] = 'Modelo Restringido'



			# 		print programarimac




	data_dict = ValuesQuerySetToDict(aseguradora)

	data = json.dumps(data_dict)


	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def riesgomodelo(request,modelo):

	data=RiesgAseg.objects.filter(id_model=modelo).values('aseguradora__name_asegurad','id_model__id_modelo__name_model','id_model','id_riesg_id')

	data_dict = ValuesQuerySetToDict(data)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")





@csrf_exempt
def riesgos(request):

	d=Riesgo.objects.all().values('id_riesgo','tipo_riesgo').order_by('tipo_riesgo');

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def listagps2(request):


	d=Gps.objects.filter(value=1).values('sumaminima','id','id_aseg__name_asegurad','id_prog__program','value').order_by('-id')[:10]



	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listagps(request):


	d=Gps.objects.all().exclude(value=1).values('sumaminima','id','id_aseg__name_asegurad','id_prog__program','id_auto__id_modelo__name_model','id_auto__id_marca__name_marca','id_auto__id_modelo__name_model','id_uso__uso','anio_antig','value','anio_antig__anio_antig').order_by('-id')[:10]


	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def riesgomodelo(request,modelo):

	data=RiesgAseg.objects.filter(id_model=modelo).values('aseguradora__name_asegurad','id_model__id_modelo__name_model','id_model','id_riesg_id')

	data_dict = ValuesQuerySetToDict(data)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def getgps(request,modelo,marca,tipo,uso,monto,anio,programa):


	gpspositiva = 'No'
	gpsrimac = 'No'
	gpspacifico = 'No'
	gpsmapfre = 'No'
	gpshdi = 'No'


	auto =AutoValor.objects.get(id_modelo_id=modelo,id_marca_id=marca,id_tipo_id=tipo)

	id_auto = auto.id

	today = date.today()

	anio = Anio.objects.get(id_anio=anio).anio_antig

	difanio =  int(today.year)-int(anio)

	if Gps.objects.filter(id_auto =id_auto,id_aseg=1).count() > 0 :

		gpspositiva = 'Si'

	## Gps Rimac

	yaris =[1369,1370,1371,1372,1454,1455,1456,1457,1493,1495,1519,1520,1521,8448]


	if Gps.objects.filter(id_auto =id_auto,id_aseg=5).count() > 0 and int(difanio)<3:

		gpsrimac = 'Si'

	if  (int(difanio)<5 and int(id_auto)==8376) or (int(difanio)<5 and str(id_auto in yaris) == 'True') :

		gpsrimac = 'Si'

	if int(monto) >=50000:

		gpsrimac = 'Si'

	## Gps Mapfre

	## Dorada 

	progmapfre = programa.split('z')[0]

	print 'progmapfre',progmapfre

	if int(progmapfre)==5 or int(progmapfre)==1 or int(progmapfre)==24:

		if (str(id_auto in yaris) == 'True' and  int(difanio)<4) or (int(id_auto)==8376 and int(difanio)<4):

			gpsmapfre = 'Si'

		if Gps.objects.filter(id_auto=id_auto,id_aseg=4).count()>0 and int(difanio)<3:

			gpsmapfre = 'Si' 

		if int(monto) >=50000:

			gpsmapfre = 'Si'

	## Dorada Pickup

	pickma= [7669,7815,7817,7814]

	if int(progmapfre)== 22:

		if int(id_auto)==8376 and int(difanio)<4:

			gpsmapfre = 'Si'

		if str(id_auto in pickma) == 'True' and int(difanio)<3:

			gpsmapfre = 'Si'

	if int(progmapfre)== 19:

		if int(id_auto)==8376 and int(difanio)<3:

			gpsmapfre = 'Si'

	if int(progmapfre)== 21:

		gpsmapfre = 'Si'

	# Gps Positiva

	tipop=[1,3,17,6]

	if str(tipo in tipop) == 'True' and int(monto)>=50000:

		gpspositiva = 'Si'

	if tipo==6:

		gpspositiva = 'Si'

	if Gps.objects.filter(id_auto=id_auto,id_aseg=1).count()>0  and int(difanio)<3:

		gpspositiva = 'Si'

	if int(monto)>=50000:

		gpspositiva = 'Si'

	## Gps Hdi 

	if Gps.objects.filter(id_auto=id_auto,id_aseg=3).count()>0 :

		gpshdi= 'Si'

	## Gps Pacifico

	if Gps.objects.filter(id_auto=id_auto,id_aseg=2).count()>0 :

		gpspacifico = 'Si'


	data = {'gpshdi':gpshdi,'gpsmapfre':gpsmapfre,'gpsrimac':gpsrimac,'gpspacifico':gpspacifico,'gpspositiva':gpspositiva}

	data = json.dumps(data)
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def cobertura(request,orden_id,uso,anio,modalidad,programa,modelo):


	tipo = AutoValor.objects.filter(id_modelo_id=modelo)

	for t in tipo:

		tipo = t.id_tipo_id

	pro = programa.split('z')

	promapfre = pro[0]
	propositiva = pro[2]
	prorimac = pro[1]

	body = ''

	today = date.today()

	anio = Anio.objects.get(id_anio=anio).anio_antig

	difanio =  int(today.year)-int(anio)


	anioset = 10
	

	if difanio <= 10 :

		anioset = 10

	if difanio > 10 and difanio <= 15:

		anioset = 15

	if difanio > 15 and difanio <= 20:

		anioset = 20
	

	if RiesgAseg.objects.filter(aseguradora_id=1,id_model_id=modelo):

		riesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=2,id_model_id=modelo):

		riesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=modelo).id_riesg__tipo_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=4,id_model_id=modelo):
	
		riesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=modelo).id_riesg__tipo_riesgo
	


	cobertura = Cobertura.objects.all().values('id_cobert','descripcion').order_by('id_cobert')

	lista = []

	cober = []


	for i in range(len(cobertura)):

		cober.append(i)

		if CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=3).count()==1:

			lista.append(i)

			cobertura[i]['hdi'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=3).value
			
		if CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=1).count()==1:

			lista.append(i)

			cobertura[i]['positiva'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=1).value

		if CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=2).count()==1:

			lista.append(i)

			cobertura[i]['pacifico'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=2).value

		if CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=4,programa_id=promapfre).count()==1:
		
			lista.append(i)

			cobertura[i]['mapfre'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=4,programa_id=promapfre).value
		
		if CobertAsegur.objects.filter(id_cob=cobertura[i]['id_cobert'],id_aseg_id=5,programa_id=prorimac).count()==1:

			lista.append(i)
			
			cobertura[i]['rimac'] = CobertAsegur.objects.get(id_cob=cobertura[i]['id_cobert'],id_aseg_id=5,programa_id=prorimac).value


	data_dict = ValuesQuerySetToDict(cobertura)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def deducible(request,orden_id,uso,anio,modalidad,programa,modelo):

	print 'modelo',modelo

	tipo = AutoValor.objects.get(id_modelo_id=modelo)

	id_auto_valor = AutoValor.objects.get(id_modelo_id=modelo).id

	riesgorimac = 3

	if RiesgAseg.objects.filter(aseguradora_id=1,id_model_id=id_auto_valor):

		riesgopositiva = RiesgAseg.objects.get(aseguradora_id=1,id_model_id=id_auto_valor).id_riesg.id_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=2,id_model_id=id_auto_valor):

		riesgopacifico = RiesgAseg.objects.get(aseguradora_id=2,id_model_id=id_auto_valor).id_riesg.id_riesgo

	if RiesgAseg.objects.filter(aseguradora_id=4,id_model_id=id_auto_valor):

		riesgomapfre = RiesgAseg.objects.get(aseguradora_id=4,id_model_id=id_auto_valor).id_riesg.id_riesgo
	
	if RiesgAseg.objects.filter(aseguradora_id=5,id_model_id=id_auto_valor):

		riesgorimac = RiesgAseg.objects.get(aseguradora_id=5,id_model_id=id_auto_valor).id_riesg.id_riesgo




	tipo = tipo.id_tipo.id_clase

	pro = programa.split('z')


	promapfre = pro[0]
	propositiva = pro[2]
	prorimac = pro[1]


	
	deducible = Deducibles.objects.all().values('id_deduc','deducible').order_by('id_deduc')
	
	anio = int(Anio.objects.get(id_anio=anio).anio_antig)

	lista = []

	cober = []

	for i in range(len(deducible)):


		if DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=3,id_uso=uso,tipo__id_clase=tipo).count()>0:

			deducible[i]['hdi'] = DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=3,id_uso=uso,tipo__id_clase=tipo).values('value')[0]['value']

			#deducible[i]['hdi'] = DeducAsegur.objects.get(riesgo_id=riesgohdi,id_deduc=deducible[i]['id_deduc'],id_aseg_id=3,id_uso=uso,tipo__id_clase=tipo).value

		# p= DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=1,id_uso=uso,modalidad_id=modalidad,programa_id=propositiva,tipo_id=tipo).values('id_deduc__deducible')

		# if p.count()==1:

		# 	deducible[i]['positiva'] = DeducAsegur.objects.get(id_deduc=deducible[i]['id_deduc'],id_aseg_id=1,id_uso=uso,modalidad_id=modalidad,programa_id=propositiva,tipo_id=tipo).value


		# if DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=2).count()==1:

		# 	deducible[i]['pacifico'] = DeducAsegur.objects.get(id_deduc=deducible[i]['id_deduc'],id_aseg_id=2).value


		# p = DeducAsegur.objects.filter(id_deduc=deducible[i]['id_deduc'],id_aseg_id=4,programa_id=promapfre,id_uso_id=uso,riesgo_id=riesgomapfre,tipo_id=tipo).values('id_deduc__deducible')

		
		## Mapfre

		if int(promapfre) == 1:

			if DeducAsegur.objects.filter(riesgo_id=riesgomapfre,id_deduc_id=deducible[i]['id_deduc'],id_aseg_id=4,programa_id=promapfre).count()>0:

			 	deducible[i]['mapfre'] = DeducAsegur.objects.get(riesgo_id=riesgomapfre,id_deduc_id=deducible[i]['id_deduc'],tipo__id_clase=tipo,id_aseg_id=4,programa_id=promapfre).value
			

		## Deducible rimac

		if int(prorimac) == 2:

			if DeducAsegur.objects.filter(riesgo_id=riesgorimac,id_deduc_id=deducible[i]['id_deduc'],id_aseg_id=5,tipo__id_clase=tipo,programa_id=prorimac).count()>0:
			
				deducible[i]['rimac'] = DeducAsegur.objects.get(riesgo_id=riesgorimac,id_deduc_id=deducible[i]['id_deduc'],id_aseg_id=5,tipo__id_clase=tipo,programa_id=prorimac).value
			
			if int(tipo)==6:

				if DeducAsegur.objects.filter(riesgo_id=riesgorimac,id_deduc_id=deducible[i]['id_deduc'],id_aseg_id=5,tipo__id_clase=tipo,programa_id=prorimac).count()==1:
				
					deducible[i]['rimac'] = DeducAsegur.objects.get(id_deduc_id=deducible[i]['id_deduc'],id_aseg_id=5,tipo__id_clase=tipo,programa_id=prorimac).value
				



	data_dict = ValuesQuerySetToDict(deducible)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def servic(request):

	

	servicio = Servicios.objects.all().values('id_serv','services').order_by('id_serv')


	lista = []

	cober = []

	for i in range(len(servicio)):

		cober.append(i)

		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=3).count()==1:

			lista.append(i)

			servicio[i]['hdi'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=3).valor


		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=1).count()==1:

			lista.append(i)

			servicio[i]['positiva'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=1).valor


		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=2).count()==1:

			lista.append(i)

			servicio[i]['pacifico'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=2).valor


		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=5).count()==1:

			lista.append(i)

			servicio[i]['rimac'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=5).valor


		if ServicAsegur.objects.filter(id_serv=servicio[i]['id_serv'],id_aseg_id=4).count()==1:

			lista.append(i)

			servicio[i]['mapfre'] = ServicAsegur.objects.get(id_serv=servicio[i]['id_serv'],id_aseg_id=4).valor

	data_dict = ValuesQuerySetToDict(servicio)


	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")




@csrf_exempt
def servicio(request):

	d=ServicAsegur.objects.values('id','id_serv','id_serv__services','id_aseg__name_asegurad','valor')

	data_dict = ValuesQuerySetToDict(d)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


# @csrf_exempt
# def postin(request):

# 	if request.method == 'POST':

# 		print json.loads(request.body)

# 	return HttpResponse('xxxxx', content_type="application/json")


@csrf_exempt
def precio(request,id_model,anio):

	precioact =AutoValor.objects.get(id_modelo=id_model).valor


	return HttpResponse(precioact, content_type="application/json")


@csrf_exempt
def preciodreprecio(request,precio):

	precio = float(precio)

	precio = '{0:.2f}'.format(precio)


	return HttpResponse(precio, content_type="application/json")

@csrf_exempt
def listaservice(request):

	d=Servicios.objects.all().values('id_serv','services').order_by('id_serv')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listfinanase(request):

	d=FinanAsegu.objects.all().values('id','id_finan','id_finan__financiamiento','id_aseg__name_asegurad','cuota','tea').order_by('-id')

	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listafinance(request):

	d=FinanAsegu.objects.all().values('id_finan','id_aseg','cuota','tea').order_by('id_finan')

	data_dict = ValuesQuerySetToDict(d)	
	
	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def listafinanciamiento(request):

	d=Financiamiento.objects.all().values('id_financ','financiamiento').order_by('id_financ')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def uso(request):

	d=Uso.objects.all().values('id_uso','uso').order_by('id_uso')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def timon(request):

	d=Timon.objects.all().values('id_timon','name_tipo').order_by('id_timon')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def modalidad(request):

	d=Modalidad.objects.all().values('id_modalidad','name_modalidad').order_by('id_modalidad')
	
	data_dict = ValuesQuerySetToDict(d)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def date_handler(obj):

	return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def ValuesQuerySetToDict(vqs):
	return [item for item in vqs]


@csrf_exempt
def add(request):

	if request.method == 'POST':

		data =  json.loads(request.body)
#		


		#{u'categoria': {u'categoria': u'I', u'id_categ': 1}, u'igv': 18, u'clase': [{u'clase': u'Cami\xf3n', u'id_clase': 2}], u'anio': {u'id_anio': 16, u'anio_antig': 2004}, u'uso': {u'uso': u'Particular', u'id_uso': 1}, u'cobertura': [{u'descripcion': u'Riesgos de la Naturaleza', u'id_cobert': 20}], u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'marca': {u'id_marca': 178, u'name_marca': u'LADA'}, u'value': u'111', u'demision': 3, u'aniox': 0, u'modelo': {u'id_model': 8062, u'name_model': u'C-61'}, u'programa': [{u'id_program': 3, u'program': u'Corporativo HDI'}], u'ubicacion': {u'id': 1, u'label': u'Lima'}, u'modalidad': [{u'id_modalidad': 2, u'name_modalidad': u'Todo Riesgo'}], u'aseguradora': {u'id_asegurad': 2, u'name_asegurad': u'Pacifico'}}


		cobertura = data['cobertura']
		aseguradora = data['aseguradora']
		programa = data['programa']
		modalidad = data['modalidad']
		uso = data['uso']
		clase = data['clase']
		#anio = data['anio']
		value = data['value']

		
		if type(cobertura) == dict:

			cobertura=[cobertura]

		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		if type(programa) == dict:

			programa=[programa]

		if type(modalidad) == dict:

			modalidad=[modalidad]

		if type(uso) == dict:

			uso=[uso]

		if type(clase) == dict:

			clase=[clase]

		# if type(anio) == dict:

		# 	anio=[anio]


		for c in cobertura:

			for a in aseguradora:

				for p in programa:

					for m in modalidad:

						for u in uso:

							for cl in clase:

								#for an in anio:
						
								CobertAsegur(tipo_id = int(cl['id_clase']),programa_id=int(p['id_program']),id_cob_id=int(c['id_cobert']),id_aseg_id=int(a['id_asegurad']),id_uso_id=int(u['id_uso']),value=value,modalidad_id=int(m['id_modalidad'])).save()



		data = json.dumps('data_dict')

		return HttpResponse(data, content_type="application/json")

@csrf_exempt
def addservice(request):

	if request.method == 'POST':

		data =  json.loads(request.body)



		aseguradora = data['aseguradora']['id_asegurad']
		value = data['valor']
		servicio = data['servicio']['id_serv']


		uso = data['uso']['id_uso']
		programa = data['programa']['id_program']

		ServicAsegur(id_aseg_id=aseguradora,id_serv_id=servicio,valor=value,id_uso_id=uso,id_program_id=programa).save()

		return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addfinanz(request):

	if request.method == 'POST':

		data =  json.loads(request.body)



		aseguradora = data['aseguradora']['id_asegurad']
		cuota = data['cuota']
		tea = data['tea']
		financiamiento = data['financiamiento']['id_financ']
		FinanAsegu(id_aseg_id=aseguradora,id_finan_id=financiamiento,cuota=cuota,tea=tea).save()

		return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addfinanciamiento(request):

	if request.method == 'POST':

		data =  json.loads(request.body)



		Financiamiento(financiamiento=data['financiamiento']).save()


		return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addtasa(request):

	if request.method == 'POST':

		data =  json.loads(request.body)

		# uso = data['uso']['id_uso']
		# aseguradora = data['aseguradora']['id_asegurad']
		# modalidad = data['modalidad']['id_modalidad']
		# anio = data['anio']['id_anio']
		# value = data['value']
		# categoria = data['categoria']['id_categ']
		# riesgo = data['riesgo']['id_riesgo']
		# programa = data['programa']['id_program']
		# ubicacion = data['ubicacion']['id']
		# clase_id = data['clase']['id_clase']

		uso = data['uso']
		aseguradora = data['aseguradora']
		modalidad = data['modalidad']
		anio = data['anio']
		value = data['value']
		riesgo = data['riesgo']
		programa = data['programa']
		ubicacion = data['ubicacion']
		clase = data['clase']

		if type(uso) == dict:

			uso=[uso]
	
		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		if type(modalidad) == dict:

			modalidad=[modalidad]

		if type(programa) == dict:

			programa=[programa]

		if type(anio) == dict:

			anio=[anio]


		if type(clase) == dict:

			clase=[clase]

		if type(riesgo) == dict:

			riesgo=[riesgo]

		if type(ubicacion) == dict:

			ubicacion=[ubicacion]


		for a in aseguradora:

			for p in programa:

				for m in modalidad:

					for u in uso:

						for r in riesgo:

							for an in anio:

								for cl in clase:

									for ub in ubicacion:

										TasaAsegur(ubicacion=ub['id'],riesgo_id=r['id_riesgo'],id_aseg_id=a['id_asegurad'],id_uso_id=u['id_uso'],tipo_id=cl['id_clase'],modalidad_id=m['id_modalidad'],value=value,anio_id=an['id_anio'],programa_id=p['id_program']).save()


		
			
		return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addriesgoclase(request):

	if request.method == 'POST':

		data =  json.loads(request.body)

		#{u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'aseguradora': {u'id_asegurad': 2, u'name_asegurad': u'Pacifico'}}

		#{u'modelos': [[{u'id_modelo__name_model': u'ACURA', u'model': u'ACURA', u'id_modelo': 6372, u'checkmodel': True}, {u'id_modelo__name_model': u'COMPACT', u'model': u'COMPACT', u'id_modelo': 5183, u'checkmodel': True}, {u'id_modelo__name_model': u'INTEGRA', u'model': u'INTEGRA', u'id_modelo': 8101, u'checkmodel': True}, {u'id_modelo__name_model': u'LEGEND', u'model': u'LEGEND', u'id_modelo': 5184, u'checkmodel': True}, {u'id_modelo__name_model': u'MDX', u'model': u'MDX', u'id_modelo': 5185, u'checkmodel': True}, {u'id_modelo__name_model': u'RSX', u'model': u'RSX', u'id_modelo': 5186, u'checkmodel': True}, {u'id_modelo__name_model': u'TL', u'model': u'TL', u'id_modelo': 5187, u'checkmodel': True}, {u'id_modelo__name_model': u'VIGOR', u'model': u'VIGOR', u'id_modelo': 5188, u'checkmodel': True}]], u'datax': {u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'aseguradora': {u'id_asegurad': 3, u'name_asegurad': u'HDI'}}}

		riesgo = data['datax']['riesgo']['id_riesgo']

		aseguradora = data['datax']['aseguradora']['id_asegurad']


		for m in data['modelos'][0]:

			for i in m:

				if i=='checkmodel':

					if m['checkmodel'] == True:


						#print 'modelo', AutoValor.objects.filter(id_modelo=m['id_modelo']).values('id','id_marca','id_modelo')

						id_modelo=AutoValor.objects.filter(id_modelo_id=m['id_modelo']).values('id','id_marca','id_modelo')[0]['id']



						RiesgAseg(id_riesg_id=int(riesgo),id_model_id=id_modelo,aseguradora_id=int(aseguradora)).save()




				
		data = json.dumps('data_dict')

		return HttpResponse(data, content_type="application/json")

@csrf_exempt
def addprima(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		
		#{u'categoria': {u'categoria': u'I', u'id_categ': 1}, u'igv': 18, u'anio': {u'id_anio': 16, u'anio_antig': 2004}, u'uso': {u'uso': u'Particular', u'id_uso': 1}, u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'marca': {u'id_marca': 178, u'name_marca': u'LADA'}, u'demision': 3, u'aniox': 0, u'modelo': {u'id_model': 8062, u'name_model': u'C-61'}, u'programa': {u'id_program': 2, u'program': u'Corporativo RIMAC'}, u'valor': u'145', u'ubicacion': {u'id': 1, u'label': u'Lima'}, u'modalidad': {u'id_modalidad': 3, u'name_modalidad': u'Responsabilidad Civil'}, u'aseguradora': {u'id_asegurad': 1, u'name_asegurad': u'Positiva'}}

		riesgo = data['riesgo']['id_riesgo']
		aseguradora = data['aseguradora']['id_asegurad']
		programa = data['programa']['id_program']
		primaminima = data['valor']



		Primas(riesgo_id=riesgo,aseguradora_id=aseguradora,primaminima=primaminima,programa_id=programa).save()


	return HttpResponse('data', content_type="application/json")



@csrf_exempt
def adddeduccion(request):



	if request.method == 'POST':

		data =  json.loads(request.body)
#		

		#{u'categoria': {u'categoria': u'I', u'id_categ': 1}, u'igv': 18, u'clase': [{u'clase': u'Cami\xf3n', u'id_clase': 2}], u'anio': {u'id_anio': 16, u'anio_antig': 2004}, u'uso': {u'uso': u'Particular', u'id_uso': 1}, u'cobertura': [{u'descripcion': u'Riesgos de la Naturaleza', u'id_cobert': 20}], u'riesgo': {u'id_riesgo': 153, u'tipo_riesgo': u'Alta Gama I S/.1700'}, u'marca': {u'id_marca': 178, u'name_marca': u'LADA'}, u'value': u'111', u'demision': 3, u'aniox': 0, u'modelo': {u'id_model': 8062, u'name_model': u'C-61'}, u'programa': [{u'id_program': 3, u'program': u'Corporativo HDI'}], u'ubicacion': {u'id': 1, u'label': u'Lima'}, u'modalidad': [{u'id_modalidad': 2, u'name_modalidad': u'Todo Riesgo'}], u'aseguradora': {u'id_asegurad': 2, u'name_asegurad': u'Pacifico'}}


		cobertura = data['deduccion']
		aseguradora = data['aseguradora']
		programa = data['programa']
		modalidad = data['modalidad']
		uso = data['uso']
		clase = data['clase']
		#anio = data['anio']
		value = data['value']
		riesgo =data['riesgo']

		
		if type(cobertura) == dict:

			cobertura=[cobertura]

		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		if type(programa) == dict:

			programa=[programa]

		if type(modalidad) == dict:

			modalidad=[modalidad]

		if type(uso) == dict:

			uso=[uso]

		if type(clase) == dict:

			clase=[clase]

		if type(clase) == dict:

			clase=[clase]

		if type(riesgo) == dict:

			riesgo=[riesgo]

		# if type(anio) == dict:

		# 	anio=[anio]


		for c in cobertura:

			for a in aseguradora:

				for p in programa:

					for m in modalidad:

						for u in uso:

							for r in riesgo:

								for cl in clase:

									DeducAsegur(riesgo_id=int(r['id_riesgo']),tipo_id = int(cl['id_clase']),programa_id=int(p['id_program']),id_deduc_id=int(c['id_deduc']),id_aseg_id=int(a['id_asegurad']),id_uso_id=int(u['id_uso']),value=value,modalidad_id=int(m['id_modalidad'])).save()



		data = json.dumps('data_dict')

		return HttpResponse(data, content_type="application/json")


@csrf_exempt
def addauto(request):

	data =  json.loads(request.body)

	model = json.loads(request.body)['model']


	tipo=model['clase']['id_clase']

	marca= model['marca']['id_marca']

	modelo= model['modelo']['id_model']

	# if type(clase) == dict:

	# 	clase=[clase]

	# for i in data['item'][0]:

	# 	for c in clase:

	AutoValor(id_tipo_id=tipo,id_modelo_id=modelo,id_marca_id=marca).save()	


	return HttpResponse(json.dumps(request.body), content_type="application/json")


@csrf_exempt
def addmarca(request):

	data =  json.loads(request.body)

	marca = data['data']
	
	Marca(name_marca=marca).save()

	return HttpResponse(marca, content_type="application/json")

@csrf_exempt
def addservicio(request):

	data =  json.loads(request.body)

	ser = data['data']
	
	Servicios(services=ser).save()

	return HttpResponse(marca, content_type="application/json")

@csrf_exempt
def addfinanzas(request):

	data =  json.loads(request.body)

	finan = data['data']

	Financiamiento(financiamiento=finan).save()

	return HttpResponse(marca, content_type="application/json")

@csrf_exempt
def editauto(request):

	data =  json.loads(request.body)
	tipo = data['clase']['id_clase']
	marca = data['name_marca']['id_marca']
	modelo = data['name_model']['id_model']
	auto = AutoValor.objects.get(id=data['id'])	
	auto.id_tipo_id=tipo
	auto.id_marca_id=marca
	auto.id_modelo_id=modelo
	auto.save()

	return HttpResponse('marca', content_type="application/json")


@csrf_exempt
def addmodelo(request):

	data =  json.loads(request.body)

	modelo = data['data']
	
	Modelo(name_model=modelo).save()

	return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def addriesgo(request):

	data =  json.loads(request.body)

	riesgo = data['data']
	
	Riesgo(tipo_riesgo=riesgo).save()

	return HttpResponse(json.dumps(request.body), content_type="application/json")

@csrf_exempt
def man_tasas(request):

	coberturas = TasaAsegur.objects.all().values('id_aseg','tipo','id','programa','riesgo','modalidad','id_uso','ubicacion','programa__program','riesgo__tipo_riesgo','id','id_aseg__name_asegurad','id_uso__uso','tipo__clase','modalidad__name_modalidad','value','anio','anio__anio_antig').order_by('-id')

	data_dict = ValuesQuerySetToDict(coberturas)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def man_autos(request):

	autos = AutoValor.objects.all().values('id','id_tipo__clase','id_modelo__name_model','id_marca__name_marca').order_by('-id')

	data_dict = ValuesQuerySetToDict(autos)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def man_cob(request):

	coberturas = CobertAsegur.objects.all().values('id','tipo__clase','antigued','id_cob','programa','programa__program','id_aseg','modalidad','id_cob__descripcion','id_aseg__name_asegurad','id_uso','id_uso__uso','modalidad__name_modalidad','value').order_by('-id')

	data_dict = ValuesQuerySetToDict(coberturas)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

	
def man_serv(request):

	servicios = ServicAsegur.objects.all().values('id','id_serv','id_aseg','id_serv__services','id_aseg__name_asegurad','valor','id_uso__uso','id_program__program').order_by('-id')

	data_dict = ValuesQuerySetToDict(servicios)	

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

def man_finan(request):

	financiamiento = FinanAsegu.objects.all().values('id','id_finan','id_finan__financiamiento','id_aseg','id_aseg__name_asegurad','cuota','tea').order_by('-id')

	data_dict = ValuesQuerySetToDict(financiamiento)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


# @csrf_exempt
# def financiamiento(request):

# 	financiamiento = FinanAsegu.objects.all().values('id','id_finan','id_finan__financiamiento','id_aseg','id_aseg__name_asegurad','cuota','tea').order_by('-id')

# 	data_dict = ValuesQuerySetToDict(financiamiento)

# 	data = json.dumps(data_dict)

# 	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def deduc_cob(request):

	deducib = DeducAsegur.objects.all().values('riesgo__tipo_riesgo','id_aseg','id_uso','tipo','modalidad','id','programa','id_deduc','programa__program','id','id_deduc__deducible','id_aseg__name_asegurad','id_uso__uso','tipo__clase','value','modalidad__name_modalidad','value').order_by('-id')

	data_dict = ValuesQuerySetToDict(deducib)

	data = json.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarries(request):



	data = json.loads(request.body)

	RiesgAseg.objects.get(id=data['id']).delete()

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def eliminarcob(request):


	data = json.loads(request.body)

	CobertAsegur.objects.get(id=data['id']).delete()

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminardedu(request):

	data = json.loads(request.body)

	DeducAsegur.objects.get(id=data['id']).delete()

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarpolitica(request):

	data = json.loads(request.body)

	Gps.objects.get(id=data['id']).delete()

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarserv(request):

	data = json.loads(request.body)

	ServicAsegur.objects.get(id=data['id']).delete()
	
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarprima(request):

	data = json.loads(request.body)

	Primas.objects.get(id=data['id']).delete()
	
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarfinan(request):

	data = json.loads(request.body)
	FinanAsegu.objects.get(id=data['id']).delete()
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminartasa(request):

	data = json.loads(request.body)

	TasaAsegur.objects.get(id=data['id']).delete()
	
	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def eliminarauto(request):

	data = json.loads(request.body)

	AutoValor.objects.get(id=data['id']).delete()
	
	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def addaseguradora(request):

	data = json.loads(request.body)['data']

	Aseguradora(name_asegurad=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def addmodalidad(request):

	data = json.loads(request.body)['data']

	Modalidad(name_modalidad=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def adduso(request):

	data = json.loads(request.body)['data']

	Uso(uso=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def addclase(request):

	clase = json.loads(request.body)['data']


	Clase(clase=clase).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def addprograma(request):

	program = json.loads(request.body)['data']

	Programa(program=program).save()

	return HttpResponse('data', content_type="application/json")




@csrf_exempt
def addcobertura(request):

	data = json.loads(request.body)['data']

	Cobertura(descripcion=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def adddeducible(request):

	data = json.loads(request.body)['data']
	
	Deducibles(deducible=data).save()

	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def addpoliticagps(request):

	if request.method == 'POST':

		data = json.loads(request.body)['gps']


		modelitos = json.loads(request.body)['modelitos']

		# uso = data['uso']
		aseguradora = data['aseguradora']
		programa = data['programa']
		# modalidad=data['modalidad']
		value = data['value']
		ubicacion = data['ubicacion']['id']
		anio=data['anio']


		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		# if type(modalidad) == dict:

		# 	modalidad=[modalidad]

		if type(modelitos) == dict:

			modelitos=[modelitos]

		if type(programa) == dict:

			programa=[programa]

		# if type(uso) == dict:

		# 	uso=[uso]

		if type(anio) == dict:

			anio=[anio]


		for a in aseguradora:

			for p in programa:

				# for u in uso:

				for an in anio:

					for m in modelitos[0]:

						for i in m:

							if i=='checkmodel':

								if m['checkmodel'] == True:


	

									
									# precio = AutoValor.objects.filter(id_modelo_id=m['id_modelo']).values('id','id_marca','id_modelo','valor')[0]

									# precio = AutoValor.objects.filter(id_modelo_id=m['id_modelo']).values('id','id_marca','id_modelo','valor')[0]['valor']
									
									# value = 'No'

									# if precio > 5000:

									# 	value = 'Si'

									# riesgo = RiesgAseg.objects.filter(id_model_id=id_modelo).values('id_riesg__tipo_riesgo')[0]('id_riesg__tipo_riesgo')

									# if 'Alt' in riesgo:

									# 	value = 'Si'

									
									Gps(id_uso_id=1,anio_antig_id=an['id_anio'],id_prog_id=p['id_program'],id_auto_id=m['id_modelo'],value='Si',id_aseg_id=a['id_asegurad']).save()

		return HttpResponse(data, content_type="application/json")



@csrf_exempt
def addpoliticagps2(request):

	if request.method == 'POST':

		data = json.loads(request.body)
		gps = data['gps']


		aseguradora = gps['aseguradora']
		programa = gps['programa']
		sumaminima = gps['sumaminima']

		if type(aseguradora) == dict:

			aseguradora=[aseguradora]

		if type(programa) == dict:

			programa=[programa]

		for a in aseguradora:

			for p in programa:


				Gps(sumaminima=sumaminima,id_prog_id=p['id_program'],id_aseg_id=a['id_asegurad'],id_auto_id=1,id_riesg_id=1,anio_antig_id=1,id_uso_id=1,region=1,value=1).save()





		return HttpResponse('data', content_type="application/json")
	
@csrf_exempt
def cotiSave(request):

	if request.method == 'POST':



		dato = json.loads(request.body)['dato']
		precio = json.loads(request.body)['precio']
		name =''
		cel = ''
		email = ''
	
		for i in dato:

			if i == 'name':
				name=dato['name']

			if i == 'cel':
				cel=dato['cel']

			if i == 'email':
				email=dato['email']


		#timon=dato['timon']['id_timon']
		anio=dato['anio']['id_anio']
		uso=dato['uso']
		marca=dato['marca']['id_marca']
		modelo=dato['claseModelo']['id_modelo']
		modalidad=dato['modalidad']['id_modalidad']
		tipo=dato['claseModelo']['id_tipo']

		statuscheck=dato['statuscheck']
		statusubicL=dato['statusubicL']
		statusubicP=dato['statusubicP']

		
	
		Clientes(fullname=name,email=email,celular=cel,chose_tipo_id=int(tipo),chose_marca_id=int(marca),chose_anio_id=int(anio),chose_modelo_id=int(modelo),chose_modalid_id=int(modalidad),chose_uso_id=int(uso),value=float(precio),chose_ubicl=int(statusubicL),chose_ubicp=int(statusubicP),chose_informat=int(statuscheck)).save()



		id_cliente =  Clientes.objects.all().values('id_cliente').order_by('-id_cliente')[0]['id_cliente']


	return HttpResponse(json.dumps(id_cliente), content_type="application/json")


@csrf_exempt
def enviaemail(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		#go.db.models.query.ValuesQuerySet'>
		#{u'orderId': u'425', u'anio': u'28', u'uso': u'1', u'precio': u'4444', u'modelo': u'6372', u'programa': u'3', u'modalidad': u'2'}

		orderId = data['orderId']

		cli = Clientes.objects.get(id_cliente=orderId)

		name = cli.fullname

		email = cli.email

		modelo = data['modelo']

		cli = data['orderId']

		precio = data['precio']

		a = AutoValor.objects.filter(id_modelo_id=modelo)

		#url = data['urld']

		for m in a:

			marca = m.id_marca.name_marca
			tipo = m.id_tipo.clase
			modelo = m.id_modelo.name_model

		msj = 'Estimado cliente '+ str(name) +' , el siguiente link detalla la cotizacion del auto ' + str(marca) +' '+ str(modelo)+ ' valorizado en ' +str(precio)+'. Adjunto el link: '+ str('http://cotizador.hermes.pe:800/html/pdfout.pdf')

		
		id = Clientes.objects.get(id_cliente=cli).id_cliente

		flag  = Clientes.objects.get(id_cliente=id).chose_informat

		if flag == 1:


			f = open('/var/www/html/email.txt', 'a')
			f.write(str(email)+'\n')
			f.close()

			#send_mail('Hermes',msj,'cotiza@hermes.pe', [email], fail_silently=False)

		
	return HttpResponse(json.dumps('id_cliente'), content_type="application/json")


@csrf_exempt
def savecob(request):

	data = json.loads(request.body)



	clase = data['clase']['id_clase']

	uso = data['uso']['id_uso']
	##anio = data['antigued']
	aseguradora = data['aseguradora']['id_asegurad']
	modalidad = data['modalidad']['id_modalidad']
	programa = data['programa']['id_program']
	valor = data['value']

	c = CobertAsegur.objects.get(id=data['id'])
	
	c.tipo_id=clase

	c.id_aseg_id=aseguradora
	c.modalidad_id=modalidad
	c.programa_id=programa
	

	c.id_uso_id=uso
	##c.antigued=anio
	
	c.value = valor
	c.save()

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def saveprimas(request):

	data = json.loads(request.body)



	primaminima = data['primaminima']
	programa = data['programa']['id_program']
	aseguradora = data['aseguradora']['id_asegurad']
	riesgo= data['riesgo']['id_riesgo']

	prima = Primas.objects.get(id=data['id'])
	
	prima.aseguradora_id = aseguradora
	prima.riesgo_id = riesgo
	prima.programa_id=programa
	prima.primaminima = primaminima
	prima.save()


	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def savededu(request):

	data = json.loads(request.body)


	clase = data['clase']['id_clase']
	
	uso = data['uso']['id_uso']
	#anio = data['anio']['id_anio']
	aseguradora = data['aseguradora']['id_asegurad']
	modalidad = data['modalidad']['id_modalidad']
	programa = data['programa']['id_program']
	valor = data['value']
	riesgo = data['riesgo']['id_riesgo']

	c = DeducAsegur.objects.get(id=data['id'])
	c.tipo_id=clase
	c.id_aseg_id=aseguradora
	c.modalidad_id=modalidad
	c.programa_id=programa
	c.anio_id=anio
	c.id_uso_id=uso
	c.value = valor
	c.riesgo_id=riesgo
	c.save()


	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def saveservicio(request):



	if request.method == 'POST':

		data = json.loads(request.body)



		servicio = data['servicio']['id_serv']

		value = data['valor']

		aseguradora = data['aseguradora']['id_asegurad']
		
		c = ServicAsegur.objects.get(id=data['id'])
		c.id_aseg_id=aseguradora
		c.id_serv_id = servicio
		c.valor=value
		c.save()

		return HttpResponse(data, content_type="application/json")


@csrf_exempt
def savefinanc(request):

	data = json.loads(request.body)


	#{u'id_aseg__name_asegurad': u'Positiva', u'id_finan__financiamiento': u'Cuotas Sin Interes', u'clase': {u'clase': u'Auto', u'id_clase': 1}, u'tea': 676, u'cuota': u'787', u'riesgo': {u'id_riesgo': 84, u'tipo_riesgo': u'Alta Gama hasta $40k'}, u'aseguradora': {u'id_asegurad': 1, u'name_asegurad': u'Positiva'}}

	cuota = data['cuota']
	tea = data['tea']
	fi = data['id_finan']
	id=data['id']

	aseguradora = data['aseguradora']['id_asegurad']

	c = FinanAsegu.objects.get(id=id)
	c.id_finan_id=fi
	c.id_aseg_id=aseguradora
	c.cuota=cuota
	c.tea=tea
	c.save()


	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def savetasa(request):

	data = json.loads(request.body)


	clase = data['clase']['id_clase']
	uso = data['uso']['id_uso']
	anio = data['anio']['id_anio']
	aseguradora = data['aseguradora']['id_asegurad']
	modalidad = data['modalidad']['id_modalidad']
	programa = data['programa']['id_program']
	riesgo=data['riesgo']['id_riesgo']
	valor = data['value']


	c = TasaAsegur.objects.get(id=data['id'])

	c.tipo_id=clase
	c.id_aseg_id=aseguradora
	c.modalidad_id=modalidad
	c.id_uso_id=uso
	c.programa_id=programa
	c.anio_id=anio
	c.riesgo_id=riesgo
	c.value=valor

	c.save()


	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def savepoliticas(request):

	data = json.loads(request.body)



	anio = data['anio']['id_anio']
	aseguradora = data['aseguradora']['id_asegurad']
	programa = data['programa']['id_program']
	valor = data['value']


	c = Gps.objects.get(id=data['id'])

	c.id_aseg_id=aseguradora
	c.programa_id=programa
	c.anio_antig_id=anio
	c.value=valor

	c.save()


	return HttpResponse(data, content_type="application/json")
