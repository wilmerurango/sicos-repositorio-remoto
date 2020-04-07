from django.contrib import admin
# Register your models here.

from facturacion.models import *

admin.site.register(especialista)
admin.site.register(fac_especialista)
admin.site.register(especialista_cpp_aux)
admin.site.register(fac_especialista_detalle)
admin.site.register(contrato)
admin.site.register(uvt) 
admin.site.register(reten_383)
admin.site.register(retencion)
admin.site.register(cuenta_reten)

admin.site.register(arriendo)
admin.site.register(cpp_arriendo)
admin.site.register(cpp_arriendo_detalle)
admin.site.register(inductor_arri)

admin.site.register(servicio_medico)
admin.site.register(cpp_servicio_medico)
admin.site.register(cpp_servicio_medico_detalle)

admin.site.register(centro_costo)
admin.site.register(tipo_fact)
admin.site.register(actividad)
admin.site.register(centro_actividad)
admin.site.register(sub_activity)

admin.site.register(proveedor)  
admin.site.register(categoria) 
admin.site.register(producto) 
admin.site.register(distribucion) 
admin.site.register(cpp_proveedor)  
admin.site.register(cpp_proveedor_detalle)   
admin.site.register(cpp_proveedor_subdetalle)  
admin.site.register(cuenta_aux)   

admin.site.register(servicio_general)

admin.site.register(serv_public)
admin.site.register(cpp_serv_public)
admin.site.register(cuenta_aux_serv)
admin.site.register(distri_serv_public)
admin.site.register(cpp_servi_detalle)
admin.site.register(tipo_serv)
admin.site.register(Tarifa)
