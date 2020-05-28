
class calculo():
    obj1 = {}
    obj2 = {}
    obj3 = {}
    obj4 = {}
    obj5 = {}
    obj6 = {}

    
    def __init__(self,
                 objeto1 = 0,
                 objeto2 = 0,
                 objeto3 = 0,
                 objeto4 = 0,
                 objeto5 = 0,
                 objeto6 = 0,
                 ):
        self.obj1 = objeto1
        self.obj2 = objeto2
        self.obj3 = objeto3
        self.obj4 = objeto4
        self.obj5 = objeto5
        self.obj6 = objeto6


    def resultado(self):
        # obj1 = nombre_canasta
        # obj2 = honorario
        # obj3 = consulta
        # obj4 = canasta
        # obj5 = salario

        #CREAR UNA LISTA VACIA
        datos_obte = []
        
        #OBTENER EL NOMBRE DE LA CANASTA
        consul_ultimo = self.obj3.last()#ultimo objeto del formulario de consulta (filtro de busqueda)
        canasta_honorario = self.obj2.filter(tipo_proc= consul_ultimo.tipo_proc.id).filter(procedimiento=consul_ultimo.procedimiento.id)#filtrar honortarios para obtener los registros del procedimiento buscado
        
        # dependinedo del numero de registros obtener el nombre de la canasta
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
            
        datos_obte.append(valor_canasta)#agregar el valor total de la canasta a la lista
        
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
        
        datos_obte.append(valor_desechable)#agregar el valor de los desechables a la lista
        datos_obte.append(valor_medicamento)#agregar el valor  de los medicamentos a la lista
        datos_obte.append(dispositivos_medicos)#agregar el valor de los dispositivos medicos a la lista
        datos_obte.append(valor_paquete_reutili)#agregar el valor de los paquetes reutilizables a la lista
        datos_obte.append(valor_otros)#agregar el valor total de otros conceptos a la lista
        datos_obte.append(valor_papeleria)#agregar el valor de la papeleria a la lista
        
        salario_fil = self.obj5.filter(tipo_proc = consul_ultimo.tipo_proc).filter(procedimiento = consul_ultimo.procedimiento)
        
        # salario_total = 0
        # for i in salario_fil:
        #     salario_total += i.costo*consul_ultimo.procedimiento.duracion_proc
            
        # datos_obte.append(salario_total)#agregar el valor del salario total a la lista

        valor_consul_aneste = 0
        valor_consul_esp = 0
        for i in salario_fil:
            
            if i.concepto_salario.nombre_concep_sal[0:22]=="CONSULTA ANESTECIOLOGO":
                valor_consul_aneste += i.costo
            
            if i.concepto_salario.nombre_concep_sal[0:21]=="CONSULTA ESPECIALISTA":
                valor_consul_esp += i.costo
            
        datos_obte.append(valor_consul_aneste)
        datos_obte.append(valor_consul_esp)
        
        return datos_obte
