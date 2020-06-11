from django.db import models
from django.utils import timezone
# from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
# Create your models here.

# ============= INICIO LAS TABLAS PARA ESPECIALISTA ==========================================
#=============================================================================================
#=============================================================================================
#=============================================================================================
#=============================================================================================

class especialista(models.Model):
    id_esp = models.CharField('Identificación', max_length=11)
    name_esp = models.CharField('Nombre del Especialista',max_length=50)
    apellidos_esp = models.CharField('Apellidos del Especialista',max_length=70)
    especialidad = models.CharField('Especialidad', max_length=50, default = "No se Registro")
    tel_esp = models.CharField('Telefono',max_length=12, blank =  True)
    dir_esp = models.CharField('Dirección', max_length=100, blank=True)
    mail_esp= models.EmailField('E-mail',max_length=60, blank = True)
    fechafact_esp = models.DateField('Fecha de Registro', default = timezone.now())
    
    def __str__(self):
        return '%s %s' % (self.name_esp, self.apellidos_esp)
    
        
class contrato(models.Model):
    # nombre = models.CharField('Nombre de la Base', null=True, max_length=70)
    especialista=models.ForeignKey(especialista, null=True,blank=False, verbose_name="Nombre del Especialista" , on_delete=models.CASCADE)
    cargo_esp = models.CharField('Cargo del Especialista',max_length=70, null=True)
    valor = models.FloatField('Monto Devengado al mes', default=0, null=True)
    si='SI'
    no = 'NO'
    opcion_choices=[
        (si,'SI'),
        (no,'NO'),
    ]
    info_contrato = models.TextField('Información sobre el contrato', blank = True, null = True)
    razon_social_reglament=models.CharField('Razon Social Reglamentaria',max_length=2,choices=opcion_choices, default=no)
    reten_11=models.CharField('Retención 11%',max_length=2,choices=opcion_choices, default=no)
    reten_art_383=models.CharField('Aplica Retención Art. 383',max_length=2,choices=opcion_choices, default=no)
    dependiente_cargo=models.CharField('Dependiente a Cargo',max_length=2,choices=opcion_choices, default=no)
    reten_10=models.CharField('Retención del 10%',max_length=2,choices=opcion_choices, default=no)
    pension_obligado=models.CharField('Obligado a Cotizar Pension ',max_length=2,choices=opcion_choices, default=no)
    reten_arrindo=models.CharField('Retención por Arriendo',max_length=2,choices=opcion_choices, default=no)
    fecha = models.DateField('Fecha', null =True)
    
    def __str__(self):
        return '%s %s' % (self.especialista.name_esp, self.especialista.apellidos_esp)
    
class cuenta_reten(models.Model):
    contrato = models.ForeignKey(contrato, null = True, on_delete = models.CASCADE, verbose_name ="Base Retención-Especialista")
    name_cuenta = models.CharField('Nombre de Cuenta', max_length=50)
    num_cuenta = models.BigIntegerField('Número de Cuenta', null =True)
    porc_retencion = models.FloatField('Retención en %', null= True, default = 4)
    
    
class Tarifa(models.Model):
    nombre = models.CharField('Tarifa', null = True, blank = False, max_length = 50)
    fecha_inicio = models.DateField('Fecha Inicio', null = True, blank = False)
    fecha_final = models.DateField('Fecha Final', null = True, blank =  True )
    
    def __str__(self):
            return '%s' % (self.nombre)
  
    

class uvt(models.Model):
    tarifa = models.ForeignKey(Tarifa, on_delete = models.CASCADE, verbose_name = "Nombre Tarifa", null  = True)
    # name = models.CharField('Nombre Tarifa',max_length=51, null=True)
    valor_uvt=models.FloatField('Valor del UVT', null=True, default=34270)
    smlv = models.FloatField('Valor Salario Minimo', null=True, default=828116)
    restric_smlv = models.FloatField('Restricción SMLV', null=True, default=0)
    rent_ext_lab = models.FloatField('Renta Extensa Laboral en %', null=True, default=0)#
    tope_deduc_re=models.FloatField('Tope Renta Extensa en %', null=True, default=0)#

    
    def __str__(self):
        return '%s' % (self.name)
  
class reten_383(models.Model):
    tarifa = models.ForeignKey(Tarifa, on_delete = models.CASCADE, verbose_name = "Nombre Tarifa", null = True)
    minimo=models.FloatField('Minimo', null=True, default=0)
    maximo=models.FloatField('Máximo', null=True, default=0)
    resta = models.FloatField('Resta', null=True, default=0)
    porcent=models.FloatField('Porcentaje', null=True, default=0)
    adicion=models.FloatField('Adicion Puntos', null=True, default=0)
    
            
class tipo_fact(models.Model):
    name_fact = models.CharField('Nombre del Tipo de Facturación', max_length=20)

    def __str__(self):
        return '%s' % (self.name_fact)


class especialista_cpp_aux(models.Model):
    contrato = models.ForeignKey(contrato, null=True, blank=False,on_delete=models.CASCADE, verbose_name='Identificación Especialista')
    tipo_fact = models.ForeignKey(tipo_fact, null=True, blank=False, on_delete=models.CASCADE, verbose_name='Tipo Facturacion')
   
    def __str__(self):
        return '%s %s %s' % (self.contrato.especialista.name_esp, self.contrato.especialista.apellidos_esp, self.tipo_fact.name_fact)


class fac_especialista(models.Model):
    tarifa = models.ForeignKey(Tarifa, on_delete = models.CASCADE, verbose_name = "Nombre Tarifa", null  = True)
    # uvt = models.ForeignKey(uvt, null=True, on_delete=models.CASCADE, verbose_name='Nombre Tarifa')
    especialista = models.ForeignKey(especialista, null=True, blank=False, on_delete=models.CASCADE, verbose_name='Identificación')#de aqui se saca el id_esp
    glosa = models.FloatField('Glosa del mes', null=True, default=0)#
    valor = models.FloatField(null=True, blank=False, default=0)
    acum = models.FloatField(null=True, blank=False, default=0)
    
    aport_volun_pension = models.FloatField('Aportes Voluntarios a Pension Max 25% S.', null=True, default=0)#
    int_pre_vivi= models.FloatField('Intereses Prestamo de Vivienda Max 100 UVT ', null=True, default=0)#
    plan_comp_salud = models.FloatField('Plan Complementrio de Salud ', null=True, default=0)#
    
    aport_afc = models.FloatField('Aportes a Cuentas AFC', null=True, default=0)#
    aport_volun_emple = models.FloatField('Aportes Voluntarios del Empleador', null=True, default=0)#
    indem_lab = models.FloatField('Indemnizaciones Laborales', null=True, default=0)#
    rent_exten_lab = models.FloatField('Renta Extensa Laboral', null=True, default=25)#
    top_deduc_rent_exte = models.FloatField('Tope Deducciones + Renta Extensa ', null=True, default=40)#

    fechafac_esp = models.DateField('Fecha')

    def __str__(self):
        return '%s' % (self.id)
    
    class Meta:
        ordering = ['-id']


class centro_costo(models.Model): ##esta es la clase para almacena los centros de costos (SE COMPARTE CON LA TABLA FAC_ARRIRNDO)
    id_centro_costo = models.CharField('Número de Cuenta',max_length=20)
    name_ccos = models.CharField('Nombre del Centro de Costo',max_length=100)

    def __str__(self):
        return '%s' % (self.name_ccos)


class sub_activity(models.Model):#CREAR O REGISTRAR UNA SUB-ACTIVIDAD
    # actividad = models.ForeignKey(actividad, null=True, blank=False, on_delete=models.CASCADE, verbose_name='ID actividad')#de aqui se saca el numero de la cuenta contable de la entidad "actividad"
    # num_cuenta = models.CharField('Numero de Cuenta',max_length=20, null=True, blank=False)#este es el numero de la cuenta de la subactividad
    name_subactivity = models.CharField('Nombre del Grupo de actividades',max_length=70)
    
    def __str__(self):
        return '%s' % (self.name_subactivity)
    
    class Meta:
        ordering = ['name_subactivity']

class actividad(models.Model):
    sub_activity = models.ForeignKey(sub_activity, null=True, blank=False, on_delete=models.CASCADE, verbose_name='Grupo de la Actividad')
    # centro_costo= models.ForeignKey(centro_costo, null=True, blank=False, on_delete=models.CASCADE, verbose_name='Centro de Costo')
    name_act= models.CharField('Nombre de la Actividad',max_length=70)
    # id_cuenta_act = models.CharField('Número de Cuenta',max_length=20)
    # costo = models.FloatField('Costo Actividad', default = 0 , null= True)
    valor_iss = models.FloatField('Valor ISS', default = 0 , null= True)
    pct_iss = models.FloatField('Porcentaje ISS Adicional (%)', default = 25, null= True)
    
    def __str__(self):
        return '%s' % (self.name_act)
    
    class Meta:
        ordering = ['name_act']


class centro_actividad(models.Model):
    centro_costo = models.ForeignKey(centro_costo, null=True, blank=False, on_delete=models.CASCADE, verbose_name='Centro de Costo')
    actividad = models.ForeignKey(actividad, null=True, blank=False, on_delete=models.CASCADE, verbose_name='Actividad')
    cuenta = models.BigIntegerField('N° Cuenta', null = True)
    
    def __str__(self):
        return '%s' % (self.actividad.name_act)
    

class fac_especialista_detalle(models.Model): #REALIZAR EL DETALLE DE LA FACTURA O CPP DE LOS ESPECIALISTAS 
    fac_especialista = models.ForeignKey(fac_especialista, null=True, blank=False, on_delete=models.CASCADE, verbose_name='Codigo de la Factura')
    centro_costo = models.ForeignKey(centro_costo, null=True, blank=False, on_delete=models.CASCADE,verbose_name='Centro de Costo')
    centro_actividad = models.ForeignKey(centro_actividad, null=True, blank=False, on_delete=models.CASCADE,verbose_name='Actividad')
    # sub_activity = models.ForeignKey(sub_activity, null=True, blank=True, on_delete=models.CASCADE,verbose_name='Subactividad')
    tipo_fact = models.ForeignKey(tipo_fact, null=True, blank=False, on_delete=models.CASCADE,verbose_name='Tipo de Factura o CPP' )
    valor = models.FloatField(null=True, blank=False, default=0)
    fechafac_detalle = models.DateField('Fecha', null=True, blank=False)  
    parametrizado = models.BooleanField("¿Pamametrizado?", default=True)


class retencion(models.Model):
    fac_especialista = models.IntegerField('Códido Especialista', null=True, default=0)#
    name_especialista = models.CharField('Nombre Especialista', null=True, max_length=30)#
    honorario= models.FloatField('Honorario', null=True, default=0)
    
    incr_aport_pension = models.FloatField('Aportes a Pension', null=True, default=0)
    incr_solida_pensional=models.FloatField('Solidaridad Pensional', null=True, default=0)
    incr_aport_salud = models.FloatField('Aportes a Salud', null=True, default=0)
    incr_aport_arl = models.FloatField('Aportes a ARL', null=True, default=0)
    incr_aport_vol_pension = models.FloatField('Aportes Voluntarios a Pension', null=True, default=0)
    
    deduc_int_prest_vivienda = models.FloatField('Intereses Prestamo Viviendas', null=True, default=0)
    deduc_plan_comp_salud = models.FloatField('Plan Complementario Salud', null=True, default=0)
    deduc_depen_cargo = models.FloatField('Dependinte de Cargo', null=True, default=0)
    
    aport_cuenta_afc = models.FloatField('Aporte Renta Exenta', null=True, default=0)
    aport_volun_empleador = models.FloatField('Aporte Voluntario Empleador', null=True, default=0)
    indemni_lab = models.FloatField('Indemnizaciones Laborales', null=True, default=0)
    
    re_rent_exent_lab = models.FloatField('Renta Exenta Laboral', null=True, default=0)
    re_deduc_rent_exent = models.FloatField('Total Deducciones + Renta Exenta', null=True, default=0)
    re_tope_rent_exent_lab = models.FloatField('Tope Deducciones + Renta Exenta', null=True, default=0)
    re_total_base_grav_reten = models.FloatField('Total Base Gravable para Retención', null=True, default=0)
    re_base_grav_reten_uvt = models.FloatField('Base Gravable en UVT', null=True, default=0)
    re_fuente_uvt = models.FloatField('Retenccion en la Fuente Expresada en UVT', null=True, default=0)
    re_valor_reten = models.FloatField('Valor Retención', null=True, default=0)
    
# ============= FINAL LAS TABLAS PARA ESPECIALISTA =====================================





#=============================== TABLAS DE ARRIENDOS =========================================
#=============================================================================================
#=============================================================================================
#=============================================================================================
#=============================================================================================

class arriendo(models.Model):
    id_arri = models.CharField('NIT',max_length=11)
    name_arri = models.CharField('Nombre del Tercero',max_length=100)
    # cuenta_reten=models.CharField('Cuenta de Retención', null=True, max_length=60)#numero de cuenta en la que se almacenará la retencion.
    # reten=models.FloatField('Retencion en %', null=True, default=0)#cantidad de dinero que se esta reteniendo.
    tel_arri = models.CharField('Telefono',max_length=12)
    dir_arri = models.CharField('Dirección',max_length=100, null = True, blank = True)
    mail_arri = models.EmailField('E-mail',max_length=60, null = True, blank = True)
    fechafact_arri = models.DateField('Fecha')

    def __str__(self):
        return '%s' % (self.name_arri)

class cpp_arriendo(models.Model):
    arriendo = models.ForeignKey(arriendo, null=True, blank=False, on_delete=models.CASCADE,verbose_name='Nombre del Tercero' )
    valor_cpp_arri = models.FloatField('Valor de la Factura',null=True, blank=False, default=0) # valor por el que viene la factura o CPP
    reten=models.FloatField('Retencion en %', null=True, default=0)#cantidad de dinero que se esta reteniendo.
    valor_cont = models.FloatField('Valor Contabilizado',null=True, blank=False, default=0) # valor que se contabiliza en el sistema 
    fecha_cpp_arri = models.DateField('Fecha', null=True, blank=False)
   
    def __str__(self):
        return '%s' % (self.id)
    
    class Meta:
        ordering = ['-id']

class inductor_arri(models.Model):
    centro_costo = models.ForeignKey(centro_costo, null=True, blank=False, on_delete=models.CASCADE,verbose_name='Centro Costo' )
    cuenta_especific = models.CharField('Cuenta Específica',max_length=20, null=True)
    arriendo =  models.ForeignKey(arriendo, null=True, blank=False, on_delete=models.CASCADE,verbose_name='Nombre del Tercero' )
    induc = models.FloatField('Inductor en %')
    fecha_induc= models.DateField('Fecha de Actualizacion', null=True)
    def __str__(self):
        return '%s %s %s' % (self.centro_costo,'---', self.arriendo)

class cpp_arriendo_detalle(models.Model):
    cpp_arriendo = models.IntegerField('N° Factura', null=True) 
    name_arri = models.CharField('Nombre Empresa',max_length=150, null=True)
    # cuenta_reten=models.CharField('Cuenta Retenedora', null=True, max_length=60)#numero de cuenta en la que se almacenará la retencion.
    centro_costo = models.CharField('Centro de Costo',max_length=100, null=True)
    inductor_arri =  models.FloatField('Inductor', default=0)
    # reten = models.FloatField('Retención', default=0)
    num_cuenta=models.CharField('Cuenta C. Costo',max_length=100, null=True)
    cuenta_especific =models.CharField('Cuenta Especifica',max_length=100, null=True)
    valor_cpp_arri_detal = models.FloatField('Valor', default=0)
    fecha_cpp_arri_detal = models.DateField('Fecha')
    
    
class cuenta_arriendo_aux(models.Model):
    arriendo = models.ForeignKey(arriendo, null = True, blank=False, on_delete=models.CASCADE, verbose_name = "Seleccionar Arriendo")
    name_cuenta = models.CharField('Nombre de la Cuenta', null = True, blank = False, max_length = 50)
    cuenta = models.CharField('Número de la Cuenta', null =True, blank = False, max_length = 50)
    debito='Debito'
    credito = 'Credito'
    opcion_choices=[
    (credito,'Credito'),
    (debito,'Debito'),
    ]
    naturaleza_cuenta =  models.CharField('Naturaleza de la Cuenta',max_length=8,choices=opcion_choices, default=credito)
#=================================== FIN TABLAS ARRIENDOS =====================================================




#=====================INICIO SERVICIOS MEDICOS================================================
#=============================================================================================
#=============================================================================================
#=============================================================================================
#=============================================================================================

class servicio_medico(models.Model):#CREAR O REGISTRAR EL SERVICIO MEDICO
    nit_servm = models.CharField('NIT',max_length=11)
    name_servm = models.CharField('Nombre del Servicio',max_length=100)
    tel_servm = models.CharField('Telefono',max_length=12)
    dir_servm = models.CharField('Dirección',max_length=100)
    mail_servm= models.EmailField('E-mail',max_length=60)
    fechafact_servm = models.DateField('Fecha')

    def __str__(self):
        return '%s' % (self.name_servm)


class cpp_servicio_medico(models.Model):#CREAR UNA NUEVA FACTURA O CPP
    servicio_medico=models.ForeignKey(servicio_medico, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Nit Servicio Medico')
    valor_sm = models.FloatField('Valor',null=False, blank=False, default=0)
    fecha_cpp_sm=models.DateField('Fecha')

    def __str__(self):
        return '%s' % (self.id)


class cpp_servicio_medico_detalle(models.Model):#REALIZAR EL DETALLE DE LA FACTURA O CPP

    cpp_servicio_medico= models.ForeignKey(cpp_servicio_medico, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Codigo Servicio Medico')
    centro_costo=models.ForeignKey(centro_costo, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Cuenta Centro de Costo')
    actividad = models.ForeignKey(actividad, null=True, blank=False, on_delete=models.CASCADE,verbose_name='Actividad')
    sub_activity = models.ForeignKey(sub_activity, null=True, blank=True, on_delete=models.CASCADE,verbose_name='Subactividad')
    valor_sm_detalle = models.FloatField(null=True, blank=False)
    fecha_sm_detalle = models.DateField('Fecha', null=True, blank=False)
#=====================FINAL SERVICIOS MEDICOS====================================================





#=================================== INICIO TABLAS PROVEEDORES================================
#=============================================================================================
#=============================================================================================
#=============================================================================================
#=============================================================================================


class proveedor(models.Model):
    nit_prov= models.CharField('NIT',max_length=11, null=True)
    name_prov = models.CharField('Nombre del Proveedor',max_length=100)
    cuenta_reten = models.CharField('Cuenta de Retención', blank= True, null = True, max_length=20)
    reten = models.FloatField('Retención en %', blank = False,  null=True, default=0)
    si='SI'
    no = 'NO'
    opcion_choices=[
        (si,'SI'),
        (no,'NO'),
    ]
    distri_fija= models.CharField('¿Distribución Porcentual?',max_length=2,choices=opcion_choices, default=no)#se le asigna una distristribucion porcentual fija o se calcula dependinedo el pedido de los productos.
    dir_prov = models.CharField('Dirección',max_length=100)
    tel_prov = models.CharField('Telefono',max_length=12)
    mail_prov= models.EmailField('E-mail',max_length=60)
    fecharegistro_prov = models.DateField('Fecha')

    def __str__(self):
        return '%s' % (self.name_prov)

 
class cuenta_aux(models.Model):
    proveedor = models.ForeignKey(proveedor, null = True, blank=False, on_delete=models.CASCADE, verbose_name = "Seleccionar Proveedor")
    name_cuenta = models.CharField('Nombre de la Cuenta', null = True, blank = False, max_length = 50)
    cuenta = models.CharField('Número de la Cuenta', null =True, blank = False, max_length = 50)
    debito='Debito'
    credito = 'Credito'
    opcion_choices=[
    (credito,'Credito'),
    (debito,'Debito'),
    ]
    naturaleza_cuenta =  models.CharField('Naturaleza de la Cuenta',max_length=8,choices=opcion_choices, default=credito)


#aqui se registrara la categoria del producto . ej: "GAS", "SANGRE", ETC.
class categoria(models.Model):
    nombre = models.CharField('Nombre del Producto', null=True, blank=False, max_length = 70)
    descrip = models.TextField('Descripción', null = True, blank=False)
    
    def __str__(self):
        return '%s' % (self.nombre)


# aqui se registrara el nombre del producto. ej: "OXIGENO", "SANGRE A+",PLAQUETAS", "NITROGENO", ETC.
class producto(models.Model):
    categoria = models.ForeignKey(categoria, null=True, blank = False, verbose_name = "Categoria", on_delete=models.CASCADE)
    nombre = models.CharField('Nombre del Producto', null=True, blank=False, max_length = 70)
    precio = models.FloatField('Precio del Producto', null =True, blank= False, default=0)

    def __str__(self):
        return '%s' % (self.nombre)
    
    class Meta:
        ordering = ['nombre']
    
    
#aqui se registrara la distribucion del producto en cada centro de costo. 
class distribucion(models.Model):
    proveedor = models.ForeignKey(proveedor, null=True, blank = False, verbose_name = "Proveedor", on_delete=models.CASCADE)  
    producto =  models.ForeignKey(producto, null=True, blank = False, verbose_name = "Producto", on_delete=models.CASCADE)  
    centro_costo = models.ForeignKey(centro_costo, null=True, blank = True, verbose_name = "Centro de Costo", on_delete = models.CASCADE)
    nombre_cuenta =  models.CharField('Nombre de la Cuenta', null=True, blank=False, max_length = 70)
    debito='Debito'
    credito = 'Credito'
    opcion_choices=[
        (credito,'Credito'),
        (debito,'Debito'),
    ]
    naturaleza_cuenta =  models.CharField('Naturaleza de la Cuenta',max_length=8,choices=opcion_choices, default=credito)
    cuenta =  models.CharField('Número de Cuenta', null=True, blank=False, max_length = 20)
    distrib =  models.FloatField('% Distribución',null=True, blank=False, default=0)
    si='SI'
    no = 'NO'
    opcion_choices2=[
        (si,'SI'),
        (no,'NO'),
    ]
    meneja_iva = models.CharField('¿Maneja Iva?',max_length=2,null =True, blank=True, choices=opcion_choices2, default=no)
    cuenta_iva = models.CharField('Numero Cuenta de Iva',max_length=20, null=True, blank = True)
    valor_iva = models.FloatField('Porcentaje Iva',null=True, blank=True, default=0)

    def __str__(self):
        return '%s' % (self.producto.nombre)


#aqui se registra la CPP del tercero
class cpp_proveedor(models.Model):
    proveedor = models.ForeignKey(proveedor, null=True, blank=False, on_delete=models.CASCADE,verbose_name='Nit del Proveedor')
    producto =  models.ForeignKey(producto, null=True, blank = True, verbose_name = "Producto", on_delete=models.CASCADE)  
    valor_factura = models.FloatField('Valor Factura', default = 0)
    si='SI'
    no = 'NO'
    opcion_choices=[
        (si,'SI'),
        (no,'NO'),
    ]
    aire_medicinal= models.CharField('¿corresponde a arriendo de aire medicinal?',null =True,blank=True, max_length=2,choices=opcion_choices, default=no)
    reten = models.FloatField('Retención', null= True, blank=False, default=0)
    valor_cpp_prov = models.FloatField('Valor',null=True, blank=False, default=0)
    fecha_cpp_prov = models.DateField('Fecha', null=True, blank=False)
    def __str__(self):
        return '%s' % (self.id)
    
    class Meta:
        ordering = ['-id']

#aqui se capturaran los detalles de cada CPP 
class cpp_proveedor_detalle(models.Model):
    cpp_proveedor = models.ForeignKey(cpp_proveedor, null=True, blank=False, on_delete=models.CASCADE,verbose_name='N° de Factura')
    categoria = models.ForeignKey(categoria, null = True, blank = False, on_delete=models.CASCADE, verbose_name = 'Categoria')
    centro_costo = models.ForeignKey(centro_costo, null=True, blank=True, on_delete=models.CASCADE,verbose_name='Centro de Costo')
    producto = models.ForeignKey(producto, null=True, blank=True, on_delete=models.CASCADE,verbose_name='Producto')
    cant_produc = models.FloatField('Cantidad Productos',null=True, blank=False, default=0)
    valor_produc = models.FloatField('Valor del Producto', null=True, blank=True, default=0)
    cant_flete =  models.FloatField('Cantidad Flete',null=True, blank=False, default=0)
    valor_flete = models.FloatField('Valor Flete',null=True, blank=False, default=0)
    fecha_cpp_prov_detal =  models.DateField('Fecha', null=True, blank=False)
    
#Debido a aque no es posible tener la informacion con un solo detal se hizo necesario crear otro detalle de iguales caracteristicas que el anterior.   
class cpp_proveedor_subdetalle(models.Model):
    cpp_proveedor = models.IntegerField( 'N° de CPP', null=True, blank=False, default = 0)
    centro_costo = models.IntegerField( 'Centro de Costo',null=True, blank=True, default=0)
    proveedor = models.IntegerField('Nit del Proveedor',null=True, blank=False)
    cant_produc = models.FloatField('Cantidad Productos',null=True, blank=False, default=0)
    cant_flete =  models.FloatField('Cantidad Flete',null=True, blank=False, default=0)
    valor_flete = models.FloatField('Valor Flete',null=True, blank=False, default=0)
    nombre_cuenta =  models.CharField('Nombre de la Cuenta', null=True, blank=False, max_length = 70)
    cuenta =  models.CharField('Número de Cuenta', null=True, blank=False, max_length = 20)
    naturaleza_cuenta =  models.CharField('Naturaleza de la Cuenta',max_length=8,null=True, blank=False)
    distrib =  models.FloatField('% Distribución',null=True, blank=False, default=0)
    name_centro_costo = models.CharField('Nombre Centro Costo', null=True, blank=False, max_length = 70)
    costo = models.FloatField('Costo',null=True, blank=False, default=0)
    cuenta_iva = models.CharField('Cuenta Iva', null=True, blank = False, max_length=20)
    valor_iva = models.FloatField('Valor Iva', null=True, blank = False, default=0)
    valor_cuenta_contra = models.FloatField('valor Cuenta Contra', null = True, blank=False, default=0)
    fecha_cpp_prov_detal =  models.DateField('Fecha', null=True, blank=False)
#=================================== FINAL TABLAS PROVEEDORES=====================================================



# ============= INICIO TABLAS SERVICIO GENERAL ==========================================
#=============================================================================================
#=============================================================================================
#=============================================================================================
#=============================================================================================

#RESGISTRAR SERVICIO GENERAL
class servicio_general(models.Model):
    nit_sgen = models.CharField('NIT',max_length=11)
    name_sgen = models.CharField('Nombre el la Empresa',max_length=100)
    tel_sgen = models.CharField('Telefono',max_length=12)
    dir_sgen = models.CharField('Dirección',max_length=100)
    mail_sgen= models.EmailField('E-mail',max_length=60)
    fechafact_sgen = models.DateField('Fecha')



# ============= INICIO TABLAS SERVICIOS=============================================
#=============================================================================================
#=============================================================================================
#=============================================================================================
#=============================================================================================
class tipo_serv(models.Model):
    nombre_tipo = models.CharField('Tipo de Servicio', null=True, blank=False, max_length = 70)
    descrip = models.TextField('Descripción', null = True, blank=False)
    
    def __str__(self):
        return '%s' % (self.nombre_tipo)


class serv_public(models.Model):
    tipo_serv = models.ForeignKey(tipo_serv, null = True, blank = False, on_delete=models.CASCADE, verbose_name = 'Tipo de Servicio' )
    nit = models.CharField('NIT', null = True, blank = False, max_length = 15)
    nombre_tercero =  models.CharField('Nombre Tercero', null = True, blank = False, max_length = 50)
    nombre_serv = models.CharField('Nombre Servicio', null = True, blank = False, max_length = 50)
    direccion = models.CharField('Dirección', null = True, blank = True, max_length = 50)
    tel = models.CharField('Telefono', null = True, blank = True, max_length = 50)
    email = models.EmailField('E-mail', null = True, blank = True, max_length = 50)
    fecha = models.DateField('Fecha', null = True, blank = False)
    
    def __str__(self):
        return '%s' % (self.nombre_tercero)
    

class cpp_serv_public(models.Model):
    serv_public = models.ForeignKey(serv_public, null= True, blank = False, on_delete = models.CASCADE, verbose_name = 'Nombre del Servicio')
    costo = models.FloatField('Valor Factura', null = True, blank = False, default=0)
    iva = models.FloatField('% Iva', null = True, blank = False, default=0)
    reten = models.FloatField('Retención', null = True, blank = False, default=0)
    total = models.FloatField('Costo Total', null = True, blank = False, default=0)
    fecha =  models.DateField('Fecha', null = True, blank = False)
    
class cuenta_aux_serv(models.Model):
    serv_public = models.ForeignKey(serv_public, null=True, blank = False, on_delete=models.CASCADE, verbose_name = 'Nombre del servicio')
    name_cuenta = models.CharField('Nombre Cuenta', null=True, blank = False, max_length = 50)
    num_cuenta = models.CharField('Número Cuenta', null = True, blank = False, max_length = 20 )
    
class distri_serv_public(models.Model):
    centro_costo = models.ForeignKey(centro_costo, null = True, blank = False, on_delete=models.CASCADE, verbose_name= 'Centro de Costo')
    serv_public = models.ForeignKey(serv_public, null= True, blank = False, on_delete = models.CASCADE, verbose_name = 'Nombre del Servicio')
    name_cuenta_especific = models.CharField('Nombre Cuenta Especifica', null=True, blank = False, max_length = 50)
    num_cuenta_especific = models.CharField('Número Cuenta Especifica', null=True, blank = False, max_length = 50)
    distri = models.FloatField('Disctribución (%)',default=0,null=True, blank = False)
    cuenta_iva = models.CharField('Cuenta de Iva', blank=True, max_length = 50, null = True)
    num_cuenta_iva = models.CharField('Num. Cuenta de Iva', blank = True, null = True, max_length = 20)
    fecha_distri = models.DateField('Fecha', null = True, blank = False)

class cpp_servi_detalle(models.Model):
    cpp_serv_public = models.IntegerField('ID CPP', null = True, blank=False)
    id_serv_public = models.IntegerField('ID Servicio Público',null=True, blank=False)
    name_serv_public = models.CharField('Nombre del Tercero',  null =  True, blank=False, max_length = 50)
    id_centro_costo =  models.IntegerField('ID Centro Costo',null=True, blank=False)
    name_ccos = models.CharField('Nombre Centro de Costo',  null =  True, blank=False, max_length = 50)
    distri =  models.FloatField('Disctribución (%)',null=True, blank = False,default=0)
    name_cuenta_aux = models.CharField('Nombre Cuenta', null=True, blank = False, max_length = 50)
    num_cuenta_aux =  models.CharField('Número Cuenta', null = True, blank = False, max_length = 20)
    costo =  models.FloatField('Costo Asignado',null=True, blank = False, default=0)
    num_cuenta_iva = models.CharField('Num. Cuenta de Iva', blank = True, null = True, max_length = 20)
    valor_iva = models.FloatField('Valor del Iva', null=True, default=0, blank=False)
    valor_contra = models.FloatField('Valor Contra', null = True, blank=False, default=0)
    fecha =  models.DateField('Fecha', null = True, blank = False)