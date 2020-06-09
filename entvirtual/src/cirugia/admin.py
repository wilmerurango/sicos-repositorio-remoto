from django.contrib import admin

# Register your models here.
from cirugia.models import *

admin.site.register(tipo_proc)
admin.site.register(procedimiento)
admin.site.register(concepto_honorario)
admin.site.register(nombre_canasta)
admin.site.register(concepto_canasta)
admin.site.register(position)
admin.site.register(canasta)
admin.site.register(honorario)
admin.site.register(constante)
admin.site.register(concepto_salario)
admin.site.register(estancia)
admin.site.register(salario)
admin.site.register(consulta)

