import copy as cp

class calculo():
    obj1 = {}
    obj2 = {}
    obj3 = {}
    obj4 = {}
    obj5 = {}
    obj6 = {}
    obj7 = {}
    obj8 = {}
    obj9 = {}
    
    def __init__(self,
                 objeto1 = 0,
                 objeto2 = 0,
                 objeto3 = 0,
                 objeto4 = 0,
                 objeto5 = 0,
                 objeto6 = 0,
                 objeto7 = 0,
                 objeto8 = 0,
                 objeto9 = 0,
                 ):
        self.obj1 = objeto1
        self.obj2 = objeto2
        self.obj3 = objeto3
        self.obj4 = objeto4
        self.obj5 = objeto5
        self.obj6 = objeto6
        self.obj7 = objeto7
        self.obj8 = objeto8
        self.obj9 = objeto9

    def resultado(self):
        # obj1 = nombre_canasta
        # obj2 = honorario
        # obj3 = consulta
        # obj4 = canasta
        # obj5 = salario
        # obj6 = procedimientos
        # obj7 = estancias

        #CREAR UNA LISTA VACIA
        datos_obte = []
        
        #OBTENER EL NOMBRE DE LA CANASTA
        consul_ultimo = self.obj3.last()#ultimo objeto del formulario de consulta (filtro de busqueda)
        canasta_honorario = self.obj2.filter(tipo_proc= consul_ultimo.tipo_proc.id).filter(procedimiento=consul_ultimo.procedimiento.id)#filtrar honortarios para obtener los registros del procedimiento buscado
        print('canasta_honorario nombre',canasta_honorario.count())
        # dependinedo del numero de registros obtener el nombre de la canasta
        if canasta_honorario.count()==0:
            canasta_filtro = self.obj1.get(nombre_canasta="No tiene Canasta")
        else:
            if canasta_honorario.count()==1:
                canasta_filtro = self.obj1.get(id = canasta_honorario.first().nombre_canasta.id)
            else:
                canasta_filtro = self.obj1.get(id = canasta_honorario.first().nombre_canasta.id)
            
        datos_obte.append(canasta_filtro)#agregar el nombre de la cansta a la lista
        
        #CALCULAR EL VALOR TOTAL DE LA CANASTA
        print('eeeeeeeeeeeeeeeee',canasta_filtro)
        canasta = self.obj4.filter(nombre_canasta = canasta_filtro)
        valor_canasta = 0
        for i in canasta:
            valor_canasta += i.costo_tot
            
        datos_obte.append(valor_canasta*(1+consul_ultimo.ganancia/100))#agregar el valor total de la canasta a la lista mas la ganancia
        
        #CALCULAR EL VALOR DE LOS CONCEPTOS DENTRO DE LA CANASTA
        canasta = self.obj4.filter(nombre_canasta = canasta_filtro)
        valor_desechable = 0
        valor_medicamento = 0
        dispositivos_medicos = 0
        valor_paquete_reutili = 0
        valor_otros = 0
        valor_papeleria = 0
        
        for i in canasta:
            if i.concepto_canasta.nombre_canasta[0:10]=="DESECHABLE":
                valor_desechable += i.costo_tot
                
            if i.concepto_canasta.nombre_canasta[0:10]=="MEDICAMENT":
                valor_medicamento += i.costo_tot
                
            if i.concepto_canasta.nombre_canasta[0:10]=="DISPOSITIV":
                dispositivos_medicos += i.costo_tot
                
            if i.concepto_canasta.nombre_canasta[0:7]=="PAQUETE":
                valor_paquete_reutili += i.costo_tot
                
            if i.concepto_canasta.nombre_canasta[0:9]=="PAPELERIA":
                valor_papeleria += i.costo_tot
        
        valor_otros = valor_canasta-valor_desechable-valor_medicamento-dispositivos_medicos-valor_paquete_reutili-valor_papeleria
        
        datos_obte.append(valor_desechable*(1+consul_ultimo.ganancia/100))#agregar el valor de los desechables a la lista
        datos_obte.append(valor_medicamento*(1+consul_ultimo.ganancia/100))#agregar el valor  de los medicamentos a la lista
        datos_obte.append(dispositivos_medicos*(1+consul_ultimo.ganancia/100))#agregar el valor de los dispositivos medicos a la lista
        datos_obte.append(valor_paquete_reutili*(1+consul_ultimo.ganancia/100))#agregar el valor de los paquetes reutilizables a la lista
        datos_obte.append(valor_otros*(1+consul_ultimo.ganancia/100))#agregar el valor total de otros conceptos a la lista
        datos_obte.append(valor_papeleria*(1+consul_ultimo.ganancia/100))#agregar el valor de la papeleria a la lista
        
        
        #calcular el valor de las consultas dentro de los salarios
        salario_fil = self.obj5.filter(tipo_proc = consul_ultimo.tipo_proc.id).filter(procedimiento = consul_ultimo.procedimiento.id)

        valor_consul_aneste = 0
        valor_consul_esp = 0
        
        #calcular el valor de los salarios 
        salario_instrumen = 0
        salario_med_ayudante = 0
        salario_enfer = 0
        # otros = 0
        
        #CALCULAR VALOR DEL HONORARIO DEL ANESTRECILOGO
        honor_anestecio = 0 
        
        #derecho a sala
        dere_sala = 0
        
        #AGREGAR LA DURACION DEL PROCEDMIENTO
        procedimient = self.obj6.filter(nombre_proc = consul_ultimo.procedimiento.nombre_proc)
        duracion = procedimient.first().duracion_proc
        datos_obte.append(duracion)#8
        
        print('este es el salario',salario_fil)
        
        for i in salario_fil:
            
            if i.concepto_salario.nombre_concep_sal[0:22]=="CONSULTA ANESTECIOLOGO":
                valor_consul_aneste += i.costo
            
            if i.concepto_salario.nombre_concep_sal[0:21]=="CONSULTA ESPECIALISTA":
                valor_consul_esp += i.costo
                
            if i.concepto_salario.nombre_concep_sal[0:22]=="SALARIO_INSTRUMENTADOR":
                salario_instrumen += i.costo*(duracion/60)
            
            if i.concepto_salario.nombre_concep_sal[0:22]=="SALARIO_MEDICO_AYUDANT":
                salario_med_ayudante += i.costo*(duracion/60)
                	
            if i.concepto_salario.nombre_concep_sal[0:17]=="SALARIO_ENFERMERA":
                salario_enfer += i.costo*(duracion/60)   
                
            if i.concepto_salario.nombre_concep_sal[0:24]=="HONORARIO ANESTECIOLOGO":
                honor_anestecio += i.costo*(duracion/60) 
                
            if i.concepto_salario.nombre_concep_sal[0:14]=="DERECHO A SALA":
                dere_sala += i.costo*(duracion/60)  
        
        
        #total salario 
        total_salario =  salario_instrumen+salario_med_ayudante+salario_enfer
        
        # #otros
        # otros = total_salario-(salario_instrumen+salario_med_ayudante+salario_enfer+valor_consul_aneste+valor_consul_esp+honor_anestecio+dere_sala)
        
        datos_obte.append(valor_consul_aneste*(1+consul_ultimo.ganancia/100))
        datos_obte.append(valor_consul_esp*(1+consul_ultimo.ganancia/100))
        
        #calcular total consulta
        total_consulta = valor_consul_esp+valor_consul_aneste
        datos_obte.append(total_consulta*(1+consul_ultimo.ganancia/100))
        
        #AGREGAR SALARIOS
        datos_obte.append(salario_instrumen*(1+consul_ultimo.ganancia/100))
        datos_obte.append(salario_med_ayudante*(1+consul_ultimo.ganancia/100))
        datos_obte.append(salario_enfer*(1+consul_ultimo.ganancia/100))
        # datos_obte.append(otros)
        datos_obte.append(total_salario*(1+consul_ultimo.ganancia/100))
    
        #AGREGAR HONORARIO DE ANESTECIOLOGO
        datos_obte.append(honor_anestecio*(1+consul_ultimo.ganancia/100))
        
        #AGREGAR DERECHO A SALA
        datos_obte.append(dere_sala*(1+consul_ultimo.ganancia/100))
        
        
        #ESTANCIAS
        tipo_estan_hosp = self.obj8.last()
        estancias = self.obj7.filter(tipo_estancia =tipo_estan_hosp.id)
        valor_estan = 0
        for i in estancias:
            if i.dividir_por_cama == False:
                valor_estan += i.valor_concepto
            else:
                valor_estan += i.valor_concepto/tipo_estan_hosp.numero_camas
        
        valor_estancia_tot = valor_estan*procedimient.first().dias_estancia
        
        datos_obte.append(valor_estancia_tot*(1+consul_ultimo.ganancia/100))
        datos_obte.append(procedimient.first().dias_estancia)
        if procedimient.first().dias_estancia == 0:
            datos_obte.append(0*(1+consul_ultimo.ganancia/100))
        else:
            datos_obte.append(valor_estan*(1+consul_ultimo.ganancia/100))

        copia_honor = cp.copy(canasta_honorario)
        maximo = 0
        for i in copia_honor:
            if i.concepto_honorario.nombre_concep_hon=="ISS PLENO":
                i.costo = round(procedimient.first().uvr*self.obj9.last().valor_uvt*(1+consul_ultimo.ganancia/100))
                if i.costo >= maximo:
                    maximo= i.costo
            else:
                if i.concepto_honorario.nombre_concep_hon=="ISS + 10%":
                    i.costo = round(procedimient.first().uvr*self.obj9.last().valor_uvt*1.10*(1+consul_ultimo.ganancia/100))
                    if i.costo >= maximo:
                        maximo= i.costo
                else:
                    if i.concepto_honorario.nombre_concep_hon=="SOAT - 20%":
                        i.costo = round(i.costo*self.obj9.last().smdlv*0.8*(1+consul_ultimo.ganancia/100))
                        if i.costo >= maximo:
                            maximo= i.costo
                    else:
                        if i.concepto_honorario.nombre_concep_hon=="TARIFA DIFERENCIAL":
                            i.costo = round(i.costo*(1+consul_ultimo.ganancia/100))
                            if i.costo >= maximo:
                                maximo= i.costo
                        else:
                            i.costo = round((duracion/60)*i.costo*(1+consul_ultimo.ganancia/100))
                            if i.costo >= maximo:
                                maximo= i.costo
            
            
        datos_obte.append(copia_honor)
        
        total = round(maximo + (1+consul_ultimo.ganancia/100)*(valor_canasta + valor_estancia_tot + dere_sala + honor_anestecio + total_salario + total_consulta))
        
        datos_obte.append(total)
        
        
        return datos_obte
