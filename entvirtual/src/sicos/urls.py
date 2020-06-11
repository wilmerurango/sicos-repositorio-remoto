"""sicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path, include
from django.contrib.auth.decorators import login_required

from facturacion.views import * 
from cirugia.views import *

from django.conf import settings
from django.views.static import serve

from django.conf.urls import handler404

# handler404 = mi_error_404


# from django.contrib.auth.decorators import login, logout_then_login

urlpatterns = [
    #VISTA DE ADMINSTRADOR
    path('admin/', admin.site.urls),
    
    
    #LOGIN
    path('',LoginView.as_view(template_name= 'Entrada/login.html'), name ='login'),
    #LOGOUT
    path('logout/',LogoutView.as_view(), name ='logout'),

    
    
    #REPORTES  EN EXCEL
    #arriendos
    path('report_arriendo_excel/',Reporte_arriendo_excel.as_view(), name ='report_arriendo_excel'),
    #especialistas
    path('report_especialista_excel/',Reporte_especialista_excel.as_view(), name ='report_especialista_excel'),
    
    
    #PAGINA PRINCIPAL
    path('home', login_required(index), name='home'),
    path('cpp/', login_required(base), name='base'),
    path('cirugia/', login_required(base_cirugia), name='base_cirugia'),
    path('cambiar_pass_form/', login_required(cambiar_pass_form), name='cambiar_pass_form'),
    path('cambiar_pass_form_error/', login_required(cambiar_pass_form_error), name='cambiar_pass_form_error'),
    path('cambiar_pass/', login_required(cambiar_pass), name='cambiar_pass'),

    
    
    #REPORTES EN PDF
    #arriendos
    path('reporteCPP/<int:id_>/',login_required(Reporte_CppArriendo_Pdf),name='reporteCPP'),
    #especialistas
    path('reporte_pdf_esp/<int:id_>/',login_required(Reporte_CppEspecialista_Pdf),name='reporte_pdf_esp'),
    #proveedores
    path('reporte_pdf_proveedores/<int:id_>/',login_required(Reporte_Proveedor_Pdf),name='reporte_pdf_provedores'),
    #servicios
    path('reporte_pdf_servicios/<int:id_>/',login_required(Reporte_servicios_Pdf),name='reporte_pdf_servicios'),

    #CIRUGIA=============================================================================================================
    path('report_procediemtinso_excel/',Reporte_proc_excel.as_view(), name ='Reporte_proc_excel'),
    path('report_honorario_excel/',Reporte_Honorarios_excel.as_view(), name ='Reporte_honor_excel'),
    
    
    #CONSULTA INFORMACION
    path('consulta-procedimiento/',login_required(consulta_info), name ='consulta_info'),
    path('limpiar_consulta/',login_required(limpiar_consulta), name ='limpiar_consulta'),
    path('consulta-lista-proc/', login_required(data_proc_url), name='lista_proc_ajax'),
 
    #tipo_proc
    path('creartipo_proc/',login_required(tipo_procCrear.as_view()), name='tipo_proc_view'),
    path('listtipo_proc/',login_required(tipo_proc_list), name='tipo_proc_list'),
    path('edittipo_proc/<int:id_>/', login_required(tipo_procEdit), name='tipo_proc_edit'),
    path('elimtipo_proc/<int:id_>/', login_required(tipo_procElim), name='tipo_proc_elim'),

    #procedimiento
    path('crearprocedimiento/',login_required(procedimientoCrear.as_view()), name='procedimiento_view'),
    path('listprocedimiento/',login_required(procedimiento_list), name='procedimiento_list'),
    path('editprocedimiento/<int:id_>/', login_required(procedimientoEdit), name='procedimiento_edit'),
    path('elimprocedimiento/<int:id_>/', login_required(procedimientoElim), name='procedimiento_elim'),

    #concepto_honorario
    path('crearconcepto_honorario/',login_required(concepto_honorarioCrear.as_view()), name='concepto_honorario_view'),
    path('listconcepto_honorario/',login_required(concepto_honorario_list), name='concepto_honorario_list'),
    path('editconcepto_honorario/<int:id_>/', login_required(concepto_honorarioEdit), name='concepto_honorario_edit'),
    path('elimconcepto_honorario/<int:id_>/', login_required(concepto_honorarioElim), name='concepto_honorario_elim'),

    #nombre_canasta
    path('crearnombre_canasta/',login_required(nombre_canastaCrear.as_view()), name='nombre_canasta_view'),
    path('listnombre_canasta/',login_required(nombre_canasta_list), name='nombre_canasta_list'),
    path('editnombre_canasta/<int:id_>/', login_required(nombre_canastaEdit), name='nombre_canasta_edit'),
    path('elimnombre_canasta/<int:id_>/', login_required(nombre_canastaElim), name='nombre_canasta_elim'),

    #concepto_canasta
    path('crearconcepto_canasta/',login_required(concepto_canastaCrear.as_view()), name='concepto_canasta_view'),
    path('listconcepto_canasta/',login_required(concepto_canasta_list), name='concepto_canasta_list'),
    path('editconcepto_canasta/<int:id_>/', login_required(concepto_canastaEdit), name='concepto_canasta_edit'),
    path('elimconcepto_canasta/<int:id_>/', login_required(concepto_canastaElim), name='concepto_canasta_elim'),

    #position
    path('crearposition/',login_required(positionCrear.as_view()), name='position_view'),
    path('listposition/',login_required(position_list), name='position_list'),
    path('editposition/<int:id_>/', login_required(positionEdit), name='position_edit'),
    path('elimposition/<int:id_>/', login_required(positionElim), name='position_elim'),

    #canasta
    path('crearcanasta/',login_required(canastaCrear), name='canasta_view'),
    path('listcanasta/',login_required(canasta_list), name='canasta_list'),
    path('editcanasta/<int:id_>/', login_required(canastaEdit), name='canasta_edit'),
    path('elimcanasta/<int:id_>/', login_required(canastaElim), name='canasta_elim'),

    #honorario
    path('crearhonorario/',login_required(honorarioCrear.as_view()), name='honorario_view'),
    path('listhonorario/',login_required(honorario_list), name='honorario_list'),
    path('edithonorario/<int:id_>/', login_required(honorarioEdit), name='honorario_edit'),
    path('elimhonorario/<int:id_>/', login_required(honorarioElim), name='honorario_elim'),

    #constante
    path('crearconstante/',login_required(constanteCrear.as_view()), name='constante_view'),
    path('listconstante/',login_required(constante_list), name='constante_list'),
    path('editconstante/<int:id_>/', login_required(constanteEdit), name='constante_edit'),
    path('elimconstante/<int:id_>/', login_required(constanteElim), name='constante_elim'),
   
    #concepto_salario
    path('crearconcepto_salario/',login_required(concepto_salarioCrear.as_view()), name='concepto_salario_view'),
    path('listconcepto_salario/',login_required(concepto_salario_list), name='concepto_salario_list'),
    path('editconcepto_salario/<int:id_>/', login_required(concepto_salarioEdit), name='concepto_salario_edit'),
    path('elimconcepto_salario/<int:id_>/', login_required(concepto_salarioElim), name='concepto_salario_elim'),

    # estancia
    path('crearestancia/',login_required(estanciaCrear.as_view()), name='estancia_view'),
    path('listestancia/',login_required(estancia_list), name='estancia_list'),
    path('editestancia/<int:id_>/', login_required(estanciaEdit), name='estancia_edit'),
    path('elimestancia/<int:id_>/', login_required(estanciaElim), name='estancia_elim'),
    
    # Tipo Estancia
    path('creartipo_estancia/',login_required(tipo_estanciaCrear.as_view()), name='tipo_estancia_view'),
    path('listtipo_estancia/',login_required(tipo_estancia_list), name='tipo_estancia_list'),
    path('edittipo_estancia/<int:id_>/', login_required(tipo_estanciaEdit), name='tipo_estancia_edit'),
    path('elimtipo_estancia/<int:id_>/', login_required(tipo_estanciaElim), name='tipo_estancia_elim'),

    #salario
    path('crearsalario/',login_required(salarioCrear.as_view()), name='salario_view'),
    path('listsalario/',login_required(salario_list), name='salario_list'),
    path('editsalario/<int:id_>/', login_required(salarioEdit), name='salario_edit'),
    path('elimsalario/<int:id_>/', login_required(salarioElim), name='salario_elim'),

    







    #CONTRATO
    path('crearcontrato/',login_required(contratoCrear.as_view()), name='contrato_view'),
    path('listcontrato/',login_required(contrato_list), name='contrato_list'),
    path('editcontrato/<int:pk>/', login_required(contratoEditar.as_view()), name='contrato_edit'),

    #TARIFA
    path('creartarifa/',login_required(tarifaCrear.as_view()), name='tarifa_view'),
    path('listtarifa/',login_required(tarifa_list), name='tarifa_list'),
    path('edittarifa/<int:pk>/', login_required(tarifaEdit.as_view()), name='tarifa_edit'),


    #UVT
    path('crearuvt/',login_required(uvtCrear.as_view()), name='uvt_view'),
    path('listuvt/',login_required(uvt_list), name='uvt_list'),
    path('edituvt/<int:pk>/', login_required(uvtEditar.as_view()), name='uvt_edit'),

    #RETEN_383
    path('crearreten_383/',login_required(reten_383Crear.as_view()), name='reten_383_view'),
    path('listreten_383/',login_required(reten_383_list), name='reten_383_list'),
    path('editreten_383/<int:pk>/', login_required(reten_383Editar.as_view()), name='reten_383_edit'),


    #RETENCION
    path('crearretencion/',login_required(retencionCrear.as_view()), name='retencion_view'),
    path('listretencion/<int:id_>',login_required(retencion_list), name='retencion_list'),


    #CUENTA DE RETENCIONES
    path('crearcuenta_reten/',login_required(cuenta_retenCrear.as_view()), name='cuenta_reten_view'),
    path('listcuenta_reten/',login_required(cuenta_reten_list), name='cuenta_reten_list'),
    path('editarcuenta_reten/<int:pk>/', login_required(cuenta_retenEdit.as_view()), name='cuenta_reten_edit'),


    #REGISTRO DE ESPECIALISTAS
    path('crearesp/',login_required(especialistaCrear), name='especialista_view'),
    path('listesp/',login_required(especialistas_list), name='especialistas_list'),
    path('editaresp/<int:pk>/', login_required(especialistaEdit.as_view()), name='especialista_edit'),


    #REGISTRO DE FAC_ESPECIALISTAS
    path('crearfactesp/',login_required(fac_especialistaCrear.as_view()), name='fac_especialista_view'),
    path('listarfactesp/',login_required(fac_especialista_list), name='fac_especialista_list'),
    # path('editarfactesp/<int:id_fac>/', fac_especialistaEdit, name='fac_especialista_edit'),


    #REGISTRO DE FAC_ESPECIALISTA_DETALLE
    path('crearfacdetal/<int:id_>/',login_required(fac_especialista_detallecrear), name='fac_especialista_detallecrear_view'),
    path('listarfacdetal/',login_required(fac_especialista_detalle_list), name='fac_especialista_detalle_list'),
    path('editarfacdetal/<int:pk>/', login_required(fac_especialista_detalleEdit.as_view()), name='fac_especialista_detalle_edit'),
    path('load-actividad/', login_required(load_actividad), name='ajax_load_actividad'),

    #REGISTRO DE ESPECIALISTA_CPP_AUX
    path('listauxesp/',login_required(especialista_cpp_aux_list), name='especialista_cpp_aux_list'),
    path('crearauxesp/', login_required(especialista_cpp_auxCrear.as_view()) , name='especialista_cpp_aux_view'),
    path('editcauxesp/<int:pk>/', login_required(especialista_cpp_auxEdit.as_view()), name='especialista_cpp_aux_edit'),


    #REGISTRO DE TIPO_FACT
    path('creartipofact/',login_required(tipo_faccrear.as_view()), name='tipo_fact_view'),
    path('listtipofact/',login_required(tipo_fact_list), name='tipo_fact_list'),
    path('edittipofact/<int:pk>/', login_required(tipo_factEditar.as_view()), name='tipo_fact_editar'),
    

    #REGISTRO DE CENTROS DE COSTOS
    path('listcc/',login_required(centro_costo_list), name='centro_costo_list'),
    path('crearcc/', login_required(centro_costoCrear.as_view()) , name='centro_costo_view'),
    path('editcc/<int:pk>/', login_required(centro_costoEdit.as_view()), name='centro_costo_view'),


    #REGISTRO DE ACTIVIDAD
    path('listact/',login_required(actividad_list), name='actividad_list'),
    path('crearact/', login_required(actividadCrear.as_view()), name='actividad_view'),
    path('editact/<int:pk>/', login_required(actividadEdit.as_view()), name='actividad_edit'),


    #REGISTRO CENTROS DE ACTIVIDAD
    path('listcentroact/',login_required(centro_actividad_list), name='centro_actividad_list'),
    path('crearcentroact/', login_required(centro_actividadCrear.as_view()), name='centro_actividad_view'),
    path('editcentroact/<int:pk>/', login_required(centro_actividadEdit.as_view()), name='centro_actividad_edit'),

    
    #REGISTRO DE SUB_ACTIVITY
    path('listsuba/',login_required(sub_activity_list), name='sub_activity_list'),
    path('crearsuba/', login_required(sub_activityCrear.as_view()), name='sub_activity_view'),
    path('editsuba/<int:pk>/', login_required(sub_activityEdit.as_view()), name='sub_activity_edit'),


    #DETALLE DE fACTURAS
    path('factu/<int:id_>/',login_required(detalle_facturador), name='detalle_facturador_view'),
    path('editarww/<int:id_>/', login_required(fac_especialista_detalle_detalEdit), name='fac_especialista_detalle_detal_edit'),


    #REGISTRO SERVICIO MEDICO
    path('listsm/',login_required(servicio_medico_list), name='servicio_medico_list'),
    path('crearsm/', login_required(servicio_medicoCrear.as_view()), name='servicio_medico_view'),
    path('edit/<int:pk>/', login_required(servicio_medicoEdit.as_view()), name='servicio_medico_edit'),
    

    #REGISTRO CPP SERVICIO MEDICO
    path('listcppsm/',login_required(cpp_servicio_medico_list), name='cpp_servicio_medico_list'),
    path('crearcppsm/', login_required(cpp_servicio_medicoCrear.as_view()), name='cpp_servicio_medico_view'),

    #REGISTRO  DETALLE CPP SERVICIO MEDICO
    path('listcppsmdetal/',login_required(cpp_servicio_medico_detalle_list), name='cpp_servicio_medico_detalle_list'),
    path('editarcppsmdetal/<int:pk>/', login_required(cpp_servicio_medico_detalleEdit.as_view()), name='cpp_servicio_medico_detalle_edit'),
    path('crearcppsmdetal/', login_required(cpp_servicio_medico_detalleCrear), name='cpp_servicio_medico_detalle_view'),
    #___________________________________________________________________________________
    path('listcppsmdetal2/<int:id_>/', login_required(cpp_servicio_medico_detalle_listadetal), name='cpp_servicio_medico_detalle_listadetal'),
    path('editcppsmdetal2/<int:id_>/', login_required(cpp_servicio_medico_detalleEditdetal), name='cpp_servicio_medico_detalleEditdetal'),

    #CREAR ARRIENDOS
    path('listarri/',login_required(arriendo_list), name='arriendo_list'),
    path('creararri/', login_required(arriendoCrear.as_view()), name='arriendo_view'),
    path('editarri/<int:pk>/', login_required(arriendoEdit.as_view()), name='arriendo_edit'),

    #CREAR CPP ARRIENDOS
    path('listacpparri/',login_required(cpp_arriendo_list), name='cpp_arriendo_list'),
    path('crearcpparri/', login_required(cpp_arriendoCrear.as_view()), name='cpp_arriendo_view'),

    #CREAR CPP ARRIENDO DETALLE
    path('listacpparridetal/',login_required(cpp_arriendo_detalle_list), name='cpp_arriendo_detalle_list'),
    path('editcpparridetal/<int:pk>/', login_required(cpp_arriendo_detalleEdit.as_view()), name='cpp_arriendo_detalle_edit'),
    path('crearcpparridetal/',login_required(cpp_arriendo_detalleCrear), name='cpp_arriendo_detalle_view'),#[esta vista no se utiliza pero no se puede borrar]
    #_____________________________________________________________________________________
    path('listacpparridetal2/<int:id_>/', login_required(cpp_arriendo_detalle_listadetal), name='cpp_arriendo_detalle_listadetal'),
    path('editcpparridetal2/<int:id_>/', login_required(cpp_arriendo_detalleEditdetal), name='cpp_arriendo_detalleEditdetal'),

    #INDUCTOR ARRIENDO
    path('listinducarri/',login_required(inductor_arri_list), name='inductor_arri_list'),
    path('editinducarri/<int:pk>/', login_required(inductor_arriEdit.as_view()), name='inductor_arri_edit'),
    path('crearinducarri/', login_required(inductor_arriCrear), name='inductor_arri_view'),
    path('load-arriendo/<int:id_>/', login_required(load_arriendo), name='ajax_load_arriendo'), 
    path('load_arriendo_ajax/', login_required(load_arriendo_ajax), name='ajax_arriendo_lista'), 

    #CUENTAS AUXILIARES DE ARRIENDO
    path('listcuenta_arriendo_aux/',login_required(cuenta_arriendo_aux_list), name='cuenta_arriendo_aux_list'),
    path('crearcuenta_arriendo_aux/', login_required(cuenta_arriendo_auxCrear.as_view()), name='cuenta_arriendo_aux_view'),
    path('editcuenta_arriendo_aux/<int:pk>/', login_required(cuenta_arriendo_auxEdit.as_view()), name='cuenta_arriendo_aux_edit'),


    #CREAR PROVEEDORES
    path('listprov/',login_required(proveedor_list), name='proveedor_list'),
    path('crearprov/', login_required(proveedorCrear.as_view()), name='proveedor_view'),
    path('editprov/<int:pk>/', login_required(proveedorEdit.as_view()), name='proveedor_edit'),

    #CREAR PRODUCTOS
    path('listprod/',login_required(producto_list), name='producto_list'),
    path('crearprod/', login_required(productoCrear.as_view()), name='producto_view'),
    path('editprod/<int:pk>/', login_required(productoEdit.as_view()), name='producto_edit'),

    #CREAR CATEGORIAS
    path('listcat/',login_required(categoria_list), name='categoria_list'),
    path('crearcat/', login_required(categoriaCrear.as_view()), name='categoria_view'),
    path('editcat/<int:pk>/', login_required(categoriaEdit.as_view()), name='categoria_edit'),

    #CREAR DISTRIBUCIONES
    path('listdist/',login_required(distribucion_list), name='distribucion_list'),
    path('creardist/', login_required(distribucionCrear), name='distribucion_view'),
    path('editdist/<int:pk>/', login_required(distribucionEdit.as_view()), name='distribucion_edit'),

    #CREAR CPP PROVEEDORES
    path('listcppprov/',login_required(cpp_proveedor_list), name='cpp_proveedor_list'),
    path('crearcpprov/', login_required(cpp_proveedorCrear.as_view()), name='cpp_proveedor_view'),

    #CREAR CPP PROVEEDORES DETALLE
    path('listcppprovdetal/',login_required(cpp_proveedor_detalle_list), name='cpp_proveedor_detalle_list'),
    path('editcppprovdetal/<int:id_>/', login_required(cpp_proveedor_detalleEdit), name='cpp_proveedor_detalle_edit'),
    path('crearcppprovdetal/<int:id_>/',login_required(cpp_proveedor_detalleCrear), name='cpp_proveedor_detalle_view'),
    #boton detalle de las cpp proveedores
    path('listcppprovdetal2/<int:id_>/', login_required(cpp_prov_detal_list), name='cpp_prov_detal_list'),
    path('editcppprovdetal2/<int:id_>/', login_required(cpp_prov_detalEdit), name='cpp_prov_detal_edit'),

    path('listcppprovsubdetal/<int:id_>/', login_required(cpp_proveedor_subdetalle_list), name='cpp_proveedor_subdetalle_list'),

    #cuentas auxioliares
    path('listcuentaux/',login_required(cuenta_aux_list), name='cuenta_aux_list'),
    path('crearcuentaux/', login_required(cuenta_auxCrear.as_view()), name='cuenta_aux_view'),
    path('editcuentaux/<int:pk>/', login_required(cuenta_auxEdit.as_view()), name='cuenta_aux_edit'),

    path('load-producto/', login_required(load_producto), name='load_producto'),



    #SERV_PUBLIC
    path('listservpublic/',login_required(serv_public_list), name='serv_public_list'),
    path('crearservpublic/', login_required(serv_publicCrear.as_view()), name='serv_public_view'),
    path('editservpublic/<int:pk>/', login_required(serv_publicEdit.as_view()), name='serv_public_edit'),

    #cpp_serv_public
    path('listcpp_serv_public/',login_required(cpp_serv_public_list), name='cpp_serv_public_list'),
    path('crearcpp_serv_public/', login_required(cpp_serv_publicCrear.as_view()), name='cpp_serv_public_view'),
    path('editcpp_serv_public/<int:pk>/', login_required(cpp_serv_publicEdit.as_view()), name='cpp_serv_public_edit'),

    #cuenta_aux_serv
    path('listcuenta_aux_serv/',login_required(cuenta_aux_serv_list), name='cuenta_aux_serv_list'),
    path('crearcuenta_aux_serv/', login_required(cuenta_aux_servCrear.as_view()), name='cuenta_aux_serv_view'),
    path('editcuenta_aux_serv/<int:pk>/', login_required(cuenta_aux_servEdit.as_view()), name='cuenta_aux_serv_edit'),

    #distri_serv_public
    path('listdistri_serv_public/',login_required(distri_serv_public_list), name='distri_serv_public_list'),
    path('creardistri_serv_public/', login_required(distri_serv_publicCrear), name='distri_serv_public_view'),
    path('editdistri_serv_public/<int:pk>/', login_required(distri_serv_publicEdit.as_view()), name='distri_serv_public_edit'),

    #cpp_servi_detalle
    path('listcpp_servi_detalle/<int:id_>/',login_required(cpp_servi_detalle_list), name='cpp_servi_detalle_list'),
    path('editcpp_servi_detalle/<int:id_>/', login_required(cpp_servi_detalleEdit), name='cpp_servi_detalle_edit'),
    
    #tipo_ser
    path('listtipo_serv/',login_required(tipo_serv_list), name='tipo_serv_list'),
    path('creartipo_serv/', login_required(tipo_servCrear.as_view()), name='tipo_serv_view'),
    path('edittipo_serv/<int:pk>/', login_required(tipo_servEdit.as_view()), name='tipo_serv_edit'),  
]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$',serve,
        {
            'document_root': settings.MEDIA_ROOT,
        })
    ]