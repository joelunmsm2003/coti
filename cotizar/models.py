
from __future__ import unicode_literals

from django.db import models


class Anio(models.Model):
    id_anio = models.AutoField(primary_key=True)
    anio_antig = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anio'



class Aseguradora(models.Model):
    id_asegurad = models.AutoField(primary_key=True)
    name_asegurad = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'aseguradora'

    def __unicode__(self):
        return self.name_asegurad


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class Modelo(models.Model):
    id_model = models.AutoField(primary_key=True)
    name_model = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'modelo'
        verbose_name = 'Modelo'

    def __unicode__(self):
        return self.name_model



class AutoValor(models.Model):
    id_marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='id_marca')
    id_modelo = models.ForeignKey('Modelo', models.DO_NOTHING, db_column='id_modelo')
    id_tipo = models.ForeignKey('Clase', models.DO_NOTHING, db_column='id_tipo')
    traccion = models.IntegerField()
    permitidopositiva = models.CharField(max_length=100)
    excluidohdi = models.CharField(max_length=100)
    categoriahdi = models.CharField(max_length=100)
    excluidorimac = models.CharField(max_length=100)
    mapfretaxialto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auto_valor'
        verbose_name = 'Marca / Modelo'

    def __unicode__(self):


        return str(self.id)





class Categorias(models.Model):
    id_categ = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'categorias'


class Clase(models.Model):
    id_clase = models.AutoField(primary_key=True)
    clase = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'clase'

    def __unicode__(self):
        return self.clase


class Riesgo(models.Model):
    id_riesgo = models.AutoField(primary_key=True)
    tipo_riesgo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'riesgo'

    def __unicode__(self):
        return self.tipo_riesgo


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    chose_marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='chose_marca')
    chose_modelo = models.ForeignKey('Modelo', models.DO_NOTHING, db_column='chose_modelo')
    chose_tipo = models.ForeignKey(Clase, models.DO_NOTHING, db_column='chose_tipo')
    chose_timon = models.ForeignKey('Timon', models.DO_NOTHING, db_column='chose_timon')
    chose_modalid = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='chose_modalid')
    chose_uso = models.ForeignKey('Uso', models.DO_NOTHING, db_column='chose_uso')
    chose_anio = models.ForeignKey(Anio, models.DO_NOTHING, db_column='chose_anio')
    chose_ubicl = models.IntegerField(db_column='chose_ubicL')  # Field name made lowercase.
    chose_ubicp = models.IntegerField(db_column='chose_ubicP')  # Field name made lowercase.
    chose_informat = models.IntegerField()
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'clientes'


class Cobertura(models.Model):
    id_cobert = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'cobertura'

    def __unicode__(self):
        return self.descripcion


class CobertAsegur(models.Model):
    id_cob = models.ForeignKey('Cobertura', models.DO_NOTHING, db_column='id_cob')
    id_aseg = models.ForeignKey('Aseguradora', models.DO_NOTHING, db_column='id_aseg')
    id_uso = models.ForeignKey('Uso', models.DO_NOTHING, db_column='id_uso')
    value = models.CharField(db_column='Value', max_length=15000)  # Field name made lowercase.
    antigued = models.IntegerField(blank=True, null=True)
    #modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad')
    riesg_auto = models.ForeignKey('Riesgo', models.DO_NOTHING, db_column='riesg_auto',null=True)
    programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='programa')
    tipo = models.ForeignKey(Clase, models.DO_NOTHING, db_column='tipo')

    class Meta:
        managed = False
        db_table = 'cobert_asegur'
        verbose_name = 'Cobertura / Aseguradora'


    def __unicode__(self):
        return self.id_cob.descripcion



class Deducibles(models.Model):
    id_deduc = models.AutoField(primary_key=True)
    deducible = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'deducibles'

    def __unicode__(self):
        return self.deducible

        
class DeducAsegur(models.Model):
    id_deduc = models.ForeignKey('Deducibles', models.DO_NOTHING, db_column='id_deduc')
    id_aseg = models.ForeignKey('Aseguradora', models.DO_NOTHING, db_column='id_aseg')
    id_uso = models.ForeignKey('Uso', models.DO_NOTHING, db_column='id_uso')
    tipo = models.ForeignKey(Clase, models.DO_NOTHING, db_column='tipo')
    #modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad')
    programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='programa')
    riesgo = models.ForeignKey('Riesgo', models.DO_NOTHING, db_column='riesgo')
    value = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'deduc_asegur'
        verbose_name = 'Deducible / Aseguradora'




class Departments(models.Model):
    name_depart = models.CharField(max_length=100)
    ubic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'departments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FinanAsegu(models.Model):
    id_finan = models.ForeignKey('Financiamiento', models.DO_NOTHING, db_column='id_finan')
    id_aseg = models.ForeignKey(Aseguradora, models.DO_NOTHING, db_column='id_aseg')
    cuota = models.CharField(db_column='Cuota', max_length=10)  # Field name made lowercase.
    tea = models.FloatField(db_column='TEA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finan_asegu'


class Financiamiento(models.Model):
    id_financ = models.AutoField(primary_key=True)
    financiamiento = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'financiamiento'


class Gps(models.Model):
    id_aseg = models.ForeignKey(Aseguradora, models.DO_NOTHING, db_column='id_aseg')
    id_prog = models.ForeignKey('Programa', models.DO_NOTHING, db_column='id_prog')
    id_auto = models.ForeignKey('AutoValor', models.DO_NOTHING, db_column='id_auto')
    id_uso = models.ForeignKey('Uso', models.DO_NOTHING, db_column='id_uso')
    id_riesg = models.ForeignKey('Riesgo', models.DO_NOTHING, db_column='id_riesg')
    anio_antig = models.ForeignKey('Anio', models.DO_NOTHING, db_column='anio_antig')
    region = models.CharField(max_length=110, blank=True, null=True)
    value = models.CharField(max_length=11, blank=True, null=True)
    sumaminima = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gps'


class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    name_marca = models.CharField(max_length=20)
    origen = models.CharField(max_length=2000)
    permitido = models.CharField(max_length=100)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'

    def __unicode__(self):
        return self.name_marca





class Modalidad(models.Model):
    id_modalidad = models.AutoField(primary_key=True)
    name_modalidad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'modalidad'





class Parametros(models.Model):
    igv = models.IntegerField(blank=True, null=True)
    d_emision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros'


class Primas(models.Model):
    aseguradora = models.ForeignKey(Aseguradora, models.DO_NOTHING, db_column='aseguradora', blank=True, null=True)
    modalidad = models.IntegerField(blank=True, null=True)
    uso = models.IntegerField(blank=True, null=True)
    riesgo = models.ForeignKey('Riesgo', models.DO_NOTHING, db_column='riesgo', blank=True, null=True)
    programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='programa', blank=True, null=True)
    ubicacion = models.IntegerField(blank=True, null=True)
    primaminima = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'primas'


class ProgAseg(models.Model):
    id_prog = models.ForeignKey('Programa', models.DO_NOTHING, db_column='id_prog')
    id_aseg = models.ForeignKey(Aseguradora, models.DO_NOTHING, db_column='id_aseg')

    class Meta:
        managed = False
        db_table = 'prog_aseg'
        verbose_name = 'Programa / Aseguradora'


class Programa(models.Model):
    id_program = models.AutoField(primary_key=True)
    program = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'programa'
        verbose_name = 'Programa'

    def __unicode__(self):
        return self.program



class RiesgAseg(models.Model):
    id_riesg = models.ForeignKey('Riesgo', models.DO_NOTHING, db_column='id_riesg')
    id_model = models.ForeignKey('AutoValor', models.DO_NOTHING, db_column='id_model')
    aseguradora = models.ForeignKey('Aseguradora', models.DO_NOTHING, db_column='aseguradora')
    programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='programa')



    class Meta:
        managed = False
        db_table = 'riesg_aseg'
        verbose_name = 'Riesgo / Aseguradora'


class Servicios(models.Model):
    id_serv = models.AutoField(primary_key=True)
    services = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'servicios'

    def __unicode__(self):
        return self.services


class ServicAsegur(models.Model):
    id_serv = models.ForeignKey('Servicios', models.DO_NOTHING, db_column='id_serv')
    id_aseg = models.ForeignKey(Aseguradora, models.DO_NOTHING, db_column='id_aseg')
    id_uso = models.ForeignKey('Uso', models.DO_NOTHING, db_column='uso')
    id_program = models.ForeignKey('Programa', models.DO_NOTHING, db_column='programa')

    valor = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'servic_asegur'
        verbose_name = 'Servicio / Aseguradora'





class TasaAsegur(models.Model):
    id_aseg = models.ForeignKey('Aseguradora', models.DO_NOTHING, db_column='id_aseg')
    id_uso = models.ForeignKey('Uso', models.DO_NOTHING, db_column='id_uso')
    value = models.CharField(db_column='Value', max_length=150)  # Field name made lowercase.
    tipo = models.ForeignKey(Clase, models.DO_NOTHING, db_column='tipo')
    modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad')
    riesgo = models.ForeignKey('Riesgo', models.DO_NOTHING, db_column='riesgo')
    programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='programa')
    anio = models.CharField(max_length=500)
    ubicacion = models.CharField(max_length=500)
    modelo = models.ForeignKey('AutoValor', models.DO_NOTHING, db_column='modelo')
    origen = models.CharField(max_length=500)
    categoria = models.ForeignKey('Categorias', models.DO_NOTHING, db_column='categoria')
    timon = models.CharField(max_length=500)


    class Meta:
        managed = False
        db_table = 'tasa_asegur'
        verbose_name = 'Tasas / Aseguradora'


class Timon(models.Model):
    id_timon = models.AutoField(primary_key=True)
    name_tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'timon'

    def __unicode__(self):
        return self.name_tipo


class Uso(models.Model):
    id_uso = models.AutoField(primary_key=True)
    uso = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uso'

    def __unicode__(self):
        return self.uso




        
class Lote(models.Model):
    file =models.FileField(upload_to='static')

    class Meta:
        managed = False
        db_table = 'lote'

class Tipouso(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo = models.ForeignKey('Clase', db_column='tipo')
    uso = models.ForeignKey('Uso', db_column='uso')


    class Meta:
        managed = False
        db_table = 'tipouso'
