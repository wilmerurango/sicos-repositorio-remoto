from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.models import User

#exportar excel
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from openpyxl import Workbook

#importar modelos y fomularios
from cirugia.models import * 
from cirugia.forms import * 
from cirugia.funciones.calculos import *

#para importar libreria de excel
import numpy as np
import xlrd
from copy import copy

# REPORTE EN EXCEL DE LOS PROCEDIMINETOS 
class Reporte_proc_excel(TemplateView):
    
    def get(self, request, *args, **kwargs):
        procedimient = procedimiento.objects.all()
        wb = Workbook()
        ws = wb.active
        ws['A1'] = 'REPORTE DETALLADO DE LAS CPP CORRESPONDIENTES A ARRIENDOS'
        
        ws['A2']= 'ID'
        ws['B2']= 'Nombre_Procedimiento'
        ws['C2']='Nombre Especialidad'
        
        cont = 3
        for proced in procedimient:
            ws.cell(row=cont, column = 1).value = proced.id
            ws.cell(row=cont, column = 2).value = proced.nombre_proc
            ws.cell(row=cont, column = 3).value = proced.tipo_proc.nombre_tipo_proc
            cont +=1
        
        nombre_reporte = "Reporte_procedimientos_excel.xlsx"
        response = HttpResponse(content_type="application/ms-excel")
        content = "attachment; filename = {0}".format(nombre_reporte)
        response['content-Disposition'] = content
        wb.save(response)
        return response


#vista de consulta de datos
def consulta_info(request):
    consul = consulta.objects.all()#eso tambien es un dato de entrada como los que estan dentro del IF de abajo

    if request.method == 'POST' :
        form = consultaform(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('consulta_info')
    else:
        form = consultaform()
    
    if consul.count() != 0:
        consul_ultimo = consul.last()
        
        #DATOS DE ENTRADA
        name_cansta = nombre_canasta.objects.all()
        honora = honorario.objects.all()
        canast = canasta.objects.all()
        salar = salario.objects.all()
        
        #FUNCION
        datos = calculo(name_cansta,honora, consul, canast, salar)
        datos.resultado()
        
        print(datos.resultado()[1])
        
        return render(request,'cirugia/consulta_info.html',{'form':form, 
                                                            'consul_ultimo':consul_ultimo,
                                                            'canasta':datos.resultado()[0].nombre_canasta,
                                                            'valor_canasta':datos.resultado()[1],
                                                            'desechable':datos.resultado()[2],
                                                            'medicamento':datos.resultado()[3],
                                                            'dispositivos':datos.resultado()[4],
                                                            'paquete_desechable':datos.resultado()[5],
                                                            'otro':datos.resultado()[6],
                                                            'papeleria':datos.resultado()[7],
                                                            'salario':datos.resultado()[8],
                                                            })
    else:
        return render(request,'cirugia/consulta_info.html',{'form':form})

def limpiar_consulta(request):
    consult = consulta.objects.all()
    consult.delete()
    return redirect('consulta_info')

def data_proc_url(request):
    tipo_proc = request.GET.get('tipo_proc')
    procedimiento1 = procedimiento.objects.filter(tipo_proc=tipo_proc).order_by('nombre_proc')
    return render(request,'cirugia/consulta_lista_proc.html',{'procedimientos':procedimiento1})

    
#tipos de procedimietos
def tipo_proc_list(request):
    tipo_pro_1 = tipo_proc.objects.all()
    contexto = {'tipo_procs':tipo_pro_1}
    return render(request, 'cirugia/tipo_proc_list.html',contexto)

def tipo_procEdit(request,id_):
    tipoproc = tipo_proc.objects.get(id = id_)
    if request.method == 'GET':
        form = tipo_procform(instance = tipoproc)
    else:
        form = tipo_procform(request.POST, instance = tipoproc)
        if form.is_valid():
            form.save()
        return redirect('tipo_proc_list')
    contexto = {'form':form}
    return render(request, 'cirugia/tipo_proc_form.html',contexto) 
        
class tipo_procCrear(CreateView):
    model = tipo_proc
    form_class = tipo_procform
    template_name = 'cirugia/tipo_proc_form.html'
    success_url=reverse_lazy('tipo_proc_list')

def tipo_procElim(request, id_):
    tipoproceso = tipo_proc.objects.get(id = id_)
    tipoproceso.delete()
    return redirect('tipo_proc_list')



#procedimientos
def procedimiento_list(request):
    
    # archi = xlrd.open_workbook('C:\\CPP\\entvirtual\\src\\cirugia\\archivo.xlsx', on_demand=True)
    # hoja1 = archi.sheet_by_index(11)
    
    # art = procedimiento.objects.all()
    # # ult = tipo_proc.objects.get(id = 6)
    
    # contador = 1
    # for i in art:
    #     if i.id >=56 and i.id <= 76:
    #         name = hoja1.cell_value(contador,0)
        # dur = hoja1.cell_value(contador,1)

    #         # i.tipo_proc = ult           
    #         # i.nombre_proc = name
    
        # i.uvr = dur  
        # i.save()
        # contador += 1
    
    
    
    # archi = xlrd.open_workbook('C:\\CPP\\entvirtual\\src\\cirugia\\archivo.xlsx', on_demand=True)
    # hoja1 = archi.sheet_by_index(10)

    # for i in range(1,hoja1.nrows): 
    #     name = hoja1.cell_value(i,0)
    #     # dur = hoja1.cell_value(i,2)
        
    #     # ult = tipo_proc.objects.get(id=13)
    #     a=procedimiento(
    #                     # tipo_proc = ult,
    #                     nombre_proc = name,
    #                     # duracion_proc = dur,
    #                     )
    #     a.save()

    
    
    procedimiento_1 = procedimiento.objects.all()
    contexto = {'procedimientos':procedimiento_1}
    return render(request, 'cirugia/procedimiento_list.html',contexto)

def procedimientoEdit(request,id_):
    procedimiento1 = procedimiento.objects.get(id = id_)
    if request.method == 'GET':
        form = procedimientoform(instance = procedimiento1)
    else:
        form = procedimientoform(request.POST, instance = procedimiento1)
        if form.is_valid():
            form.save()
        return redirect('procedimiento_list')
    contexto = {'form':form}
    return render(request, 'cirugia/procedimiento_form.html',contexto) 
    
class procedimientoCrear(CreateView):
    model = procedimiento
    form_class = procedimientoform
    template_name = 'cirugia/procedimiento_form.html'
    success_url=reverse_lazy('procedimiento_list')

def procedimientoElim(request, id_):
    procedimiento1 = procedimiento.objects.get(id = id_)
    procedimiento1.delete()
    return redirect('procedimiento_list')




#concepto_honorario
def concepto_honorario_list(request):
    concepto_honorario_1 = concepto_honorario.objects.all()
    contexto = {'concepto_honorarios':concepto_honorario_1}
    return render(request, 'cirugia/concepto_honorario_list.html',contexto)

def concepto_honorarioEdit(request,id_):
    concepto_honorario1 = concepto_honorario.objects.get(id = id_)
    if request.method == 'GET':
        form = concepto_honorarioform(instance = concepto_honorario1)
    else:
        form = concepto_honorarioform(request.POST, instance = concepto_honorario1)
        if form.is_valid():
            form.save()
        return redirect('concepto_honorario_list')
    contexto = {'form':form}
    return render(request, 'cirugia/concepto_honorario_form.html',contexto) 

class concepto_honorarioCrear(CreateView):
    model = concepto_honorario
    form_class = concepto_honorarioform
    template_name = 'cirugia/concepto_honorario_form.html'
    success_url=reverse_lazy('concepto_honorario_list')

def concepto_honorarioElim(request, id_):
    concepto_honorario1 = concepto_honorario.objects.get(id = id_)
    concepto_honorario1.delete()
    return redirect('concepto_honorario_list')



#nombre_canasta
def nombre_canasta_list(request):
    
    # archi = xlrd.open_workbook('C:\\CPP\\entvirtual\\src\\cirugia\\archivo.xlsx', on_demand=True)
    # hoja1 = archi.sheet_by_index(10)

    # for i in range(1,hoja1.nrows): 
    #     name = hoja1.cell_value(i,0)
    #     # dur = hoja1.cell_value(i,2)
        
    #     # ult = tipo_proc.objects.get(id=13)
    #     a=nombre_canasta(
    #                     # tipo_proc = ult,
    #                     nombre_canasta = name,
    #                     # duracion_proc = dur,
    #                     )
    #     a.save()
    
    nombre_canasta_1 = nombre_canasta.objects.all()
    contexto = {'nombre_canastas':nombre_canasta_1}
    return render(request, 'cirugia/nombre_canasta_list.html',contexto)

def nombre_canastaEdit(request,id_):
    nombre_canasta1 = nombre_canasta.objects.get(id = id_)
    if request.method == 'GET':
        form = nombre_canastaform(instance = nombre_canasta1)
    else:
        form = nombre_canastaform(request.POST, instance = nombre_canasta1)
        if form.is_valid():
            form.save()
        return redirect('nombre_canasta_list')
    contexto = {'form':form}
    return render(request, 'cirugia/nombre_canasta_form.html',contexto) 

class nombre_canastaCrear(CreateView):
    model = nombre_canasta
    form_class = nombre_canastaform
    template_name = 'cirugia/nombre_canasta_form.html'
    success_url=reverse_lazy('nombre_canasta_list')

def nombre_canastaElim(request, id_):
    nombre_canasta1 = nombre_canasta.objects.get(id = id_)
    nombre_canasta1.delete()
    return redirect('nombre_canasta_list')



#concepto_canasta
def concepto_canasta_list(request):
    concepto_canasta_1 = concepto_canasta.objects.all()
    contexto = {'concepto_canastas':concepto_canasta_1}
    return render(request, 'cirugia/concepto_canasta_list.html',contexto)

def concepto_canastaEdit(request,id_):
    concepto_canasta1 = concepto_canasta.objects.get(id = id_)
    if request.method == 'GET':
        form = concepto_canastaform(instance = concepto_canasta1)
    else:
        form = concepto_canastaform(request.POST, instance = concepto_canasta1)
        if form.is_valid():
            form.save()
        return redirect('concepto_canasta_list')
    contexto = {'form':form}
    return render(request, 'cirugia/concepto_canasta_form.html',contexto) 

class concepto_canastaCrear(CreateView):
    model = concepto_canasta
    form_class = concepto_canastaform
    template_name = 'cirugia/concepto_canasta_form.html'
    success_url=reverse_lazy('concepto_canasta_list')

def concepto_canastaElim(request, id_):
    concepto_canasta1 = concepto_canasta.objects.get(id = id_)
    concepto_canasta1.delete()
    return redirect('concepto_canasta_list')



#position
def position_list(request):
    position_1 = position.objects.all()
    contexto = {'positions':position_1}
    return render(request, 'cirugia/position_list.html',contexto)

def positionEdit(request,id_):
    position1 = position.objects.get(id = id_)
    if request.method == 'GET':
        form = positionform(instance = position1)
    else:
        form = positionform(request.POST, instance = position1)
        if form.is_valid():
            form.save()
        return redirect('position_list')
    contexto = {'form':form}
    return render(request, 'cirugia/position_form.html',contexto) 

class positionCrear(CreateView):
    model = position
    form_class = positionform
    template_name = 'cirugia/position_form.html'
    success_url=reverse_lazy('position_list')

def positionElim(request, id_):
    position1 = position.objects.get(id = id_)
    position1.delete()
    return redirect('position_list')



#canasta
def canasta_list(request):
    
    # archi = xlrd.open_workbook('C:\\CPP\\entvirtual\\src\\cirugia\\archivo.xlsx', on_demand=True)
    # hoja1 = archi.sheet_by_index(10)
    # cont = 1
    # for i in canasta.objects.all(): 
    #     pos = hoja1.cell_value(cont,2)
    
    #     for m in position.objects.all():
    #         if pos == m.nombre_act:
    #             i.position = m
    #             i.save()
    #     cont += 1
    
    # for i in range(1,hoja1.nrows): 
    #     n_canas = hoja1.cell_value(i,0)
    #     concep = hoja1.cell_value(i,1)
        # pos = hoja1.cell_value(cont,2)
    #     insumo = hoja1.cell_value(i,3)
    #     presen = hoja1.cell_value(i,4)
    #     canti = hoja1.cell_value(i,5)
    #     costo = hoja1.cell_value(i,6)
        
        
        # w = canasta()
        
    #     for j in nombre_canasta.objects.all():
    #         if n_canas == j.nombre_canasta:
    #             w.nombre_canasta = j
                
        
    #     for k in concepto_canasta.objects.all():
    #         if concep == k.nombre_canasta:
    #             w.concepto_canasta = k
                
        
        # for l in position.objects.all():
        #     if pos == l.nombre_act:
        #         w.position = l
                
    #     w.nombre_insumo = insumo
    #     w.presentacion = presen
    #     w.cantidad = canti
    #     w.costo_und = costo
        
    #     w.save()
        
    
    canasta_1 = canasta.objects.all()
    contexto = {'canastas':canasta_1}
    return render(request, 'cirugia/canasta_list.html',contexto)

def canastaEdit(request,id_):
    canasta1 = canasta.objects.get(id = id_)
    if request.method == 'GET':
        form = canastaform(instance = canasta1)
    else:
        form = canastaform(request.POST, instance = canasta1)
        if form.is_valid():
            form.save()
            canasta1.costo_tot = canasta1.costo_und*canasta1.cantidad
            canasta1.save()
        return redirect('canasta_list')
    contexto = {'form':form}

    return render(request, 'cirugia/canasta_form.html',contexto) 

def canastaCrear(request):
    if request.method == 'POST' :
        form = canastaform(request.POST)
        if form.is_valid(): 
            form.save()
            canastaa = canasta.objects.last()
            canastaa.costo_tot = canastaa.costo_und*canastaa.cantidad
            canastaa.save()
        return redirect('canasta_list')
    else:
        form = canastaform()
    
    return render(request, 'cirugia/canasta_form.html', {'form':form} )

def canastaElim(request, id_):
    canasta1 = canasta.objects.get(id = id_)
    canasta1.delete()
    return redirect('canasta_list')



#honorario
def honorario_list(request):
    
    # archi = xlrd.open_workbook('C:\\CPP\\entvirtual\\src\\cirugia\\archivo.xlsx', on_demand=True)
    # hoja1 = archi.sheet_by_index(12)
    
    # cont  = 1
    # for i in honorario.objects.all():
    #     i.costo =0
    #     i.save()
    #     cana = hoja1.cell_value(cont,2)
    #     concep = hoja1.cell_value(cont,3)
        
    #     for m in nombre_canasta.objects.all():
    #         if cana == m.nombre_canasta:
    #             i.nombre_canasta = m
    #             i.save()
        
    #     for n in concepto_honorario.objects.all():
    #         if concep == n.nombre_concep_hon:
    #             i.concepto_honorario = n
    #             i.save()

    #     cont += 1
    
    # cont = 1
    # for i in range(1,hoja1.nrows): 
    #     especi = hoja1.cell_value(i,0)
    #     cir = hoja1.cell_value(i,1)
    #     cana = hoja1.cell_value(cont,2)
    #     concep = hoja1.cell_value(i,3)
    #     info = hoja1.cell_value(i,4)
        

    #     w = honorario()
        
    #     for j in tipo_proc.objects.all():
    #         if especi == j.nombre_tipo_proc:
    #             w.tipo_proc = j
                
    #     for k in procedimiento.objects.all():
    #         if cir == k.nombre_proc:
    #             w.procedimiento=k

    #     for m in canasta.objects.all():
    #         if cana == m.nombre_canasta:
    #             w.canasta = m
                
    #     for n in concepto_honorario.objects.all():
    #         if concep == n.nombre_concep_hon:
    #             w.concepto_honorario = n
                
    #     w.info = info
        
    #     cont += 1
        
    #     w.save()
    
    honorario_1 = honorario.objects.all()
    contexto = {'honorarios':honorario_1}
    return render(request, 'cirugia/honorario_list.html',contexto)

def honorarioEdit(request,id_):
    honorario1 = honorario.objects.get(id = id_)
    if request.method == 'GET':
        form = honorarioform(instance = honorario1)
    else:
        form = honorarioform(request.POST, instance = honorario1)
        if form.is_valid():
            form.save()
        return redirect('honorario_list')
    contexto = {'form':form}
    return render(request, 'cirugia/honorario_form.html',contexto) 

class honorarioCrear(CreateView):
    model = honorario
    form_class = honorarioform
    template_name = 'cirugia/honorario_form.html'
    success_url=reverse_lazy('honorario_list')

def honorarioElim(request, id_):
    honorario1 = honorario.objects.get(id = id_)
    honorario1.delete()
    return redirect('honorario_list')



#constante
def constante_list(request):
    constante_1 = constante.objects.all()
    contexto = {'constantes':constante_1}
    return render(request, 'cirugia/constante_list.html',contexto)

def constanteEdit(request,id_):
    constante1 = constante.objects.get(id = id_)
    if request.method == 'GET':
        form = constanteform(instance = constante1)
    else:
        form = constanteform(request.POST, instance = constante1)
        if form.is_valid():
            form.save()
        return redirect('constante_list')
    contexto = {'form':form}
    return render(request, 'cirugia/constante_form.html',contexto) 

class constanteCrear(CreateView):
    model = constante
    form_class = constanteform
    template_name = 'cirugia/constante_form.html'
    success_url=reverse_lazy('constante_list')

def constanteElim(request, id_):
    constante1 = constante.objects.get(id = id_)
    constante1.delete()
    return redirect('constante_list')



#concepto_salario
def concepto_salario_list(request):
    
    # archi = xlrd.open_workbook('C:\\CPP\\entvirtual\\src\\cirugia\\archivo.xlsx', on_demand=True)
    # hoja1 = archi.sheet_by_index(13)
    

    # for i in range(1,hoja1.nrows): 
    #     especi = hoja1.cell_value(i,0)
        
    #     a= concepto_salario()
    #     a.nombre_concep_sal = especi
    #     a.save()
    
    concepto_salario_1 = concepto_salario.objects.all()
    contexto = {'concepto_salarios':concepto_salario_1}
    return render(request, 'cirugia/concepto_salario_list.html',contexto)

def concepto_salarioEdit(request,id_):
    concepto_salario1 = concepto_salario.objects.get(id = id_)
    if request.method == 'GET':
        form = concepto_salarioform(instance = concepto_salario1)
    else:
        form = concepto_salarioform(request.POST, instance = concepto_salario1)
        if form.is_valid():
            form.save()
        return redirect('concepto_salario_list')
    contexto = {'form':form}
    return render(request, 'cirugia/concepto_salario_form.html',contexto) 

class concepto_salarioCrear(CreateView):
    model = concepto_salario
    form_class = concepto_salarioform
    template_name = 'cirugia/concepto_salario_form.html'
    success_url=reverse_lazy('concepto_salario_list')

def concepto_salarioElim(request, id_):
    concepto_salario1 = concepto_salario.objects.get(id = id_)
    concepto_salario1.delete()
    return redirect('concepto_salario_list')



#rubro
def rubro_list(request):
    rubro_1 = rubro.objects.all()
    contexto = {'rubros':rubro_1}
    return render(request, 'cirugia/rubro_list.html',contexto)

def rubroEdit(request,id_):
    rubro1 = rubro.objects.get(id = id_)
    if request.method == 'GET':
        form = rubroform(instance = rubro1)
    else:
        form = rubroform(request.POST, instance = rubro1)
        if form.is_valid():
            form.save()
        return redirect('rubro_list')
    contexto = {'form':form}
    return render(request, 'cirugia/rubro_form.html',contexto) 

class rubroCrear(CreateView):
    model = rubro
    form_class = rubroform
    template_name = 'cirugia/rubro_form.html'
    success_url=reverse_lazy('rubro_list')

def rubroElim(request, id_):
    rubro1 = rubro.objects.get(id = id_)
    rubro1.delete()
    return redirect('rubro_list')



#salario
def salario_list(request):
    
    # archi = xlrd.open_workbook('C:\\CPP\\entvirtual\\src\\cirugia\\archivo.xlsx', on_demand=True)
    # hoja1 = archi.sheet_by_index(13)
    # cont = 1
    # for i in salario.objects.all():
        
    #     concep = hoja1.cell_value(cont,3)
    #     ubi = hoja1.cell_value(cont,4)
        
    #     for k in concepto_salario.objects.all():
    #         if concep == k.nombre_concep_sal:
    #             i.concepto_salario = k
        
    #     for n in position.objects.all():
    #         if ubi == n.nombre_act:
    #             i.position = n
        
    #     cont += 1
    #     i.save()
    
    # for i in range(1,hoja1.nrows): 
    #     especi = hoja1.cell_value(i,1)
    #     proc = hoja1.cell_value(i,2)
    #     concep = hoja1.cell_value(i,3)
    #     ubi = hoja1.cell_value(i,4)
        
    #     w = salario()
        
    #     for m in tipo_proc.objects.all():
    #         if especi == m.nombre_tipo_proc:
    #             w.tipo_proc = m 

    #     for j in procedimiento.objects.all():
    #         if proc == j.nombre_proc:
    #             w.procedimiento = j
                
    #     for k in concepto_salario.objects.all():
    #         if concep == k.nombre_concep_sal:
    #             w.concepto_salario = k
        
    #     for n in position.objects.all():
    #         if prubioc == n.nombre_act:
    #             w.position = n
                
    #     w.save()
        
    
    salario_1 = salario.objects.all()
    contexto = {'salarios':salario_1}
    return render(request, 'cirugia/salario_list.html',contexto)

def salarioEdit(request,id_):
    salario1 = salario.objects.get(id = id_)
    if request.method == 'GET':
        form = salarioform(instance = salario1)
    else:
        form = salarioform(request.POST, instance = salario1)
        if form.is_valid():
            form.save()
        return redirect('salario_list')
    contexto = {'form':form}
    return render(request, 'cirugia/salario_form.html',contexto) 

class salarioCrear(CreateView):
    model = salario
    form_class = salarioform
    template_name = 'cirugia/salario_form.html'
    success_url=reverse_lazy('salario_list')

def salarioElim(request, id_):
    salario1 = salario.objects.get(id = id_)
    salario1.delete()
    return redirect('salario_list')



#tiempo_proc
# def tiempo_proc_list(request):
#     tiempo_proc_1 = tiempo_proc.objects.all()
#     contexto = {'tiempo_procs':tiempo_proc_1}
#     return render(request, 'cirugia/tiempo_proc_list.html',contexto)

# def tiempo_procEdit(request,id_):
#     tiempo_proc1 = tiempo_proc.objects.get(id = id_)
#     if request.method == 'GET':
#         form = tiempo_procform(instance = tiempo_proc1)
#     else:
#         form = tiempo_procform(request.POST, instance = tiempo_proc1)
#         if form.is_valid():
#             form.save()
#         return redirect('tiempo_proc_list')
#     contexto = {'form':form}
#     return render(request, 'cirugia/tiempo_proc_form.html',contexto) 

# class tiempo_procCrear(CreateView):
#     model = tiempo_proc
#     form_class = tiempo_procform
#     template_name = 'cirugia/tiempo_proc_form.html'
#     success_url=reverse_lazy('tiempo_proc_list')

# def tiempo_procElim(request, id_):
#     tiempo_proc1 = tiempo_proc.objects.get(id = id_)
#     tiempo_proc1.delete()
#     return redirect('tiempo_proc_list')