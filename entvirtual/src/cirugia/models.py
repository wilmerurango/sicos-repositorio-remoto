from django.db import models

# Create your models here.
class tipo_proc(models.Model):
    nombre_tipo_proc = models.CharField('Nombre de la Especialidad', null = True, max_length = 80)
    # archivo = models.FileField(blank = True, null= True, upload_to ="chapters/%Y/%m/%D/")
    
    def __str__(self):
        return '%s' % (self.nombre_tipo_proc)
    
    class Meta:
        ordering = ['nombre_tipo_proc']

class procedimiento(models.Model):
    cod = models.CharField('Código', null = True, max_length = 20, blank = True)
    tipo_proc = models.ForeignKey(tipo_proc,verbose_name = 'Especialidad', null = True, on_delete=models.CASCADE)
    nombre_proc = models.CharField('Nombre del Procedimiento', null = True, max_length = 190)
    duracion_proc = models.FloatField('Duración del Procedimiento', null = True)
    uvr =  models.FloatField('UVR', null = True, blank = True, default = 0)

    
    def __str__(self):
        return '%s' % (self.nombre_proc)
    
    # class Meta:
    #     ordering = ['nombre_proc']

# class tiempo_proc(models.Model):
#     tipo_proc = models.ForeignKey(tipo_proc,verbose_name = 'Tipo Procedimiento', null = True, on_delete=models.CASCADE)
#     procedimiento = models.ForeignKey(procedimiento,verbose_name = 'Nombre del Procedimiento', null = True, on_delete=models.CASCADE)
#     duracion_proc = models.FloatField('Duración del Procedimiento', null = True)
    
class concepto_honorario(models.Model):
    nombre_concep_hon = models.CharField('Nombre del Concepto', null = True, max_length = 30)
    
    def __str__(self):
        return '%s' % (self.nombre_concep_hon)
    
    class Meta:
        ordering = ['nombre_concep_hon']

class nombre_canasta(models.Model):
    nombre_canasta = models.CharField('Nombre de la Canasta', null = True, max_length = 85)
    
    def __str__(self):
        return '%s' % (self.nombre_canasta)
    
    class Meta:
        ordering = ['nombre_canasta']

class concepto_canasta(models.Model):
    nombre_canasta = models.CharField('Nombre de la Canasta', null = True, max_length = 85)
    
    def __str__(self):
        return '%s' % (self.nombre_canasta)
    
    class Meta:
        ordering = ['nombre_canasta']

class position(models.Model):#aqui se escribe a q actividad pertenece el salario (entrada, ciruria, postcirugia, salida , etc)
    nombre_act = models.CharField('lugar del proceso donde se ubica', null = True, max_length = 20)
    
    def __str__(self):
        return '%s' % (self.nombre_act)
    
    class Meta:
        ordering = ['nombre_act']

class canasta(models.Model):
    # tipo_proc = models.ForeignKey(tipo_proc, verbose_name ='Especialidad', on_delete = models.CASCADE,  null = True, max_length = 50)
    nombre_canasta = models.ForeignKey(nombre_canasta, verbose_name ='Nombre de la Canasta', on_delete=models.CASCADE, null = True)
    concepto_canasta =   models.ForeignKey(concepto_canasta,verbose_name = 'Concepto', null = True, on_delete = models.CASCADE)
    position =  models.ForeignKey(position, verbose_name ='Ubicación', null = True,blank=True, max_length = 20, on_delete = models.CASCADE)
    nombre_insumo = models.CharField('Nombre Insumo', null = True, max_length = 120)
    presentacion  = models.CharField('Presentación', null = True, blank=True, max_length = 20)
    cantidad =  models.IntegerField('Cantidad', null = True, default = 1)
    costo_und =  models.FloatField('Costo Unitario', null = True)
    costo_tot =  models.FloatField('Costo Subtotal', null = True, default=0)#este campo es calculado
    


class honorario(models.Model):
    tipo_proc = models.ForeignKey(tipo_proc,verbose_name = 'Especialidad', null = True, on_delete=models.CASCADE)
    procedimiento = models.ForeignKey(procedimiento,verbose_name = 'Nombre del Procedimiento', null = True, on_delete=models.CASCADE)
    nombre_canasta = models.ForeignKey(nombre_canasta,verbose_name = 'Canasta', null = True, on_delete=models.CASCADE)
    concepto_honorario = models.ForeignKey(concepto_honorario,verbose_name = 'Concepto', null = True, on_delete=models.CASCADE)
    # duracion = models.FloatField('Duración', null = True)
    # uvr =  models.FloatField('UVR', null = True)
    info = models.TextField('Información', null = True)
    costo = models.FloatField('Costo no Paramertrizado', null = True, blank = True, default=0)
    # subtotal = models.FloatField('Subtotal', null = True)
    
    
class constante(models.Model):
    iss_adicional = models.FloatField('Porcentaje Ganancia', null = True)
    valor_uvt = models.FloatField('Valor UVT Especialistas', null = True, default = 0)
    
    
    def __str__(self):
        return '%s' % (self.iss_adicional)
    
    class Meta:
        ordering = ['iss_adicional']
    
class concepto_salario(models.Model):
    nombre_concep_sal = models.CharField('Concepto', null = True, max_length = 30)
    
    def __str__(self):
        return '%s' % (self.nombre_concep_sal)
    
    class Meta:
        ordering = ['nombre_concep_sal']
    

class rubro(models.Model):
    nombre_rubro = models.CharField('Rubro', null = True, max_length = 40)
    
    def __str__(self):
        return '%s' % (self.nombre_rubro)
    
    class Meta:
        ordering = ['nombre_rubro']
    
class salario(models.Model):
    tipo_proc = models.ForeignKey(tipo_proc,verbose_name = 'Tipo Procedimiento', null = True, on_delete=models.CASCADE)
    procedimiento = models.ForeignKey(procedimiento, verbose_name = 'Nombre del Procedimiento', null = True, on_delete = models.CASCADE)
    # nombre_canasta = models.ForeignKey(nombre_canasta,verbose_name = 'Canasta', null = True, on_delete=models.CASCADE)
    # rubro = models.ForeignKey(rubro,verbose_name = 'Rubro', null = True, on_delete=models.CASCADE)
    concepto_salario = models.ForeignKey(concepto_salario,verbose_name = 'Concepto', null = True, on_delete=models.CASCADE)
    position = models.ForeignKey(position,verbose_name = 'Ubicación Concepto', null = True, on_delete=models.CASCADE)
    # duracion = models.FloatField('Duración', null = True)
    costo = models.FloatField('Costo', null = True)
    # subtotal =  models.FloatField('Subtotal', null = True)
    
    