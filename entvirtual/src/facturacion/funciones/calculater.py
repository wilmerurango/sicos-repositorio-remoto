import numpy as np
class factura_pdf():

    obj1={}
    obj2= {}
    obj3 = {}
    obj4= {}

    #incializar los parametros
    def __init__(self, Objeto1=0, Objeto2=0, Objeto3=0, Objeto4=0):
        self.obj1 = Objeto1
        self.obj2 = Objeto2
        self.obj3 = Objeto3
        self.obj4 = Objeto4
 
    #calcula la suma del costo total facturado a un especialista
    def summ(self):
        count=0
        for i in self.obj1:    
            count += float(i.valor)
        return count

    #calcula la suma total del costo de los servicios medicos
    def summ_sm(self):
        count=0
        for i in self.obj1:
            count += float(i.valor_sm_detalle)
        return count

    #calcula la suma total del costo de los arriendos
    def summ_arri(self):
        count=0
        for i in self.obj1:
            count += float(i.valor_cpp_arri_detal)
        return count

    #calcula la suma total del costo de los Proveedores
    # def summ_prov(self):
    #     count=0
    #     for i in self.obj1:
    #         count += float(i.valor)
    #     return count
    def summ_prov(self):
        count = 0
        for i in self.obj1:
            count += float(i.cant_produc)
        return count

    #calcular los valores finales para facturacion 
    def factura_esp(self):

        suma_mf = 0
        for i in self.obj1:
            if i.tipo_fact.id == 25:
                b = self.obj3.get(id= i.sub_activity.id)
                print(b)
                suma_mf += i.valor*(b.valor_sa)
            print('esta es la suma de los montos fijos: ',suma_mf)
   
    def calculo_cpp_arriendo(self):
        # obj1: cpp_arriendo
        # obj2: inductor_arri
        
        contar_induc = self.obj2.count()
        if contar_induc != 0:
            sumaT = 0
            vector_ind= np.zeros([contar_induc,1])
            i=0
            for j in self.obj2:
                vector_ind[i]= (j.induc/100)*self.obj1.valor_cpp_arri
                sumaT += vector_ind[i]
                i = i + 1     
            return vector_ind
    
    def suma_cpp_arriendo(self): 
        contar_induc = self.obj2.count()
        if contar_induc != 0:
            sumaT = 0
            vector_ind= np.zeros([contar_induc,1])
            i=0
            for j in self.obj2:
                vector_ind[i]= (j.induc/100)*self.obj1.valor_cpp_arri#*(1-(self.obj1.arriendo.reten/100))
                sumaT += vector_ind[i]
                i = i + 1     
            return sumaT
         
    def monto_acum_esp(self):
        #obj1: fac_especialista_detalle
        sum_acum = 0
        for i in self.obj1:
            sum_acum += i.valor
        return sum_acum

    #ESTA FUNCION ES PARA CCALKULAR EL MONTO DEVENGADO DE LOS ESPECIALISTAS 
    def opera_especialistas(self):
        # NOTA
        # obj1: son los detalles que se estan facturando [mf]
        # obj2: son los tipos de facturacion [tf]
        # obj3: centros actividades
        # onj4: contrato
        
        cont_tf = self.obj2.count()#contar cuantos tipos de factura existen
        contador_mt=0 # para saber en que fila del objeto tipo_fcat va el for
        resul=np.zeros([cont_tf,1])
        
        
        #***Tenga en cuenta que el primer tipo de facturacion RESGISTRADO debe ser MONTO FIJO
        for i in self.obj2: 
            
            mf = self.obj1.filter(tipo_fact=i.id)
        

            if  contador_mt == 0:#este es Monto fijo
                #calcular numero de cuentas repetidas 
                unico = []
                for i in mf:
                    if i.centro_actividad.cuenta not in unico:
                        unico.append(i.centro_actividad.cuenta)
                num_unico = len(unico) 
                
                resulxcuenta_mf = np.zeros((num_unico,1))
                
                for j in range(num_unico):#recorrer las cuentas no repetidas
                    suma_pro = 0
                    for k in mf:#recorrer el objeto de fac_especialista_detalle que solo es de monto fijo
                        if unico[j]==k.centro_actividad.cuenta:
                            suma_pro =  suma_pro + (k.valor * k.centro_actividad.actividad.valor_iss*(1+(k.centro_actividad.actividad.pct_iss/100)))

                    resulxcuenta_mf[j,0] = suma_pro 
                    
                resul[contador_mt,0]=sum(resulxcuenta_mf)

            else:
                
                if contador_mt == 1:#este es Evento
                
                    #calcular numero de cuentas repetidas 
                    unicoe = []
                    for i in mf:
                        if i.centro_actividad.cuenta not in unicoe:
                            unicoe.append(i.centro_actividad.cuenta)
                    num_unico = len(unicoe) 
                    
                    resulxcuenta_ev = np.zeros((num_unico,1))
                    
                    for j in range(num_unico):#recorrer las cuentas no repetidas
                        suma_pro_2 = 0
                        for k in mf:#recorrer el objeto de fac_especialista_detalle 
                            if k.parametrizado == False:
                                if unicoe[j] == k.centro_actividad.cuenta:
                                    suma_pro_2 += k.valor 
                            else:
                                if unicoe[j] == k.centro_actividad.cuenta:
                                    suma_pro_2 += (k.valor * k.centro_actividad.actividad.valor_iss*(1+(k.centro_actividad.actividad.pct_iss/100)))

                        resulxcuenta_ev[j,0] = suma_pro_2
                        
                    resul[contador_mt,0]=sum(resulxcuenta_ev)
                    
                else:#este es Evento-arriendo
                    #calcular numero de cuentas repetidas 
                    unicoea = []
                    for i in mf:
                        if i.centro_actividad.cuenta not in unicoea:
                            unicoea.append(i.centro_actividad.cuenta)
                    num_unico = len(unicoea)
                    
                    resulxcuenta_eva = np.zeros((num_unico,1))
                    
                    for j in range(num_unico):#recorrer las cuentas no repetidas
                        suma_pro_3 = 0
                        for k in mf:#recorrer el objeto de fac_especialista_detalle 
                            if k.parametrizado == False:
                                if unicoea[j] == k.centro_actividad.cuenta:
                                    suma_pro_3 += k.valor 
                            else:
                                if unicoea[j] == k.centro_actividad.cuenta:
                                    suma_pro_3 += (k.valor * k.centro_actividad.actividad.valor_iss*(1+(k.centro_actividad.actividad.pct_iss/100)))

                        resulxcuenta_eva[j,0] = suma_pro_3
                        
                    resul[contador_mt,0]=sum(resulxcuenta_eva)

            contador_mt +=1
        
        total_fact = sum(resul) + self.obj4.valor
        productividad = int(sum(resul))
        print("este es unicoe",unicoe)
        print("este es unico",unico)
        return (resul, total_fact, productividad,  resulxcuenta_ev,resulxcuenta_mf,unicoe,unico, resulxcuenta_eva, unicoea)
          
    #ESTA FUNCION ES PARA CALCULAR LA BASE GRABABLE DE LOS ESPECIALISTAS       
    def retencion_esp(self):
        #obj1: contrato
        #obj2: fac_especialista filtrado con el "id_"
        #obj3: uvt
        #obj4: reten_383
        
        #calcular honorario
        if self.obj1.reten_art_383 == 'NO':
            honorario_cal = 0
        else:
            honorario_cal = self.obj2.valor + self.obj2.glosa
        
        #INGRESOS NO CONSTITUTIVOS DE RENTA
        #calcular Aportes a Pension
    
        if self.obj1.pension_obligado == 'NO':
            incr_aport_pension = 0
        else:
            if self.obj1.razon_social_reglament == 'SI':
                incr_aport_pension = round(self.obj2.valor*0.4*0.16)
            else:
                incr_aport_pension = 0
        
        #calcular Solidaridad Pensional
        if self.obj1.pension_obligado == 'NO':
            incr_solida_pensional=0
        else:
            # if self.obj3.id == 3:
            if self.obj2.valor*0.4 < (self.obj3.smlv*self.obj3.restric_smlv):
                incr_solida_pensional=0
            else:
                incr_solida_pensional = round(self.obj2.valor*0.4*0.01)
        
        #calcular Aportes a Salud 12.5%
        if self.obj1.razon_social_reglament == 'SI':
            incr_aport_salud = round(self.obj2.valor*0.4*0.125)
        else:
            incr_aport_salud = 0
        
        #calcular incr_aport_arl
        incr_aport_arl = round(self.obj2.valor*0.4*0.00522)
        
        #Calcular Aportes Voluntarios a Pension
        if self.obj2.aport_volun_pension > honorario_cal*0.25:
            incr_aport_vol_pension = honorario_cal*0.25
        else:
            incr_aport_vol_pension = self.obj2.aport_volun_pension
        
        # total ingresos no constitutivos de renta
        total_ingre_no_rent = incr_aport_pension + incr_solida_pensional + incr_aport_salud + incr_aport_arl + incr_aport_vol_pension
        
        
        #DEDUCCIONES
        #calcular Intereses Prestamo Viviendas
        if self.obj2.int_pre_vivi > 100*self.obj3.valor_uvt:
            deduc_int_prest_vivienda = round(100*self.obj3.valor_uvt)
        else:
            deduc_int_prest_vivienda = round(self.obj2.int_pre_vivi)
        
        #calcular Plan Complementrio de Salud 
        if self.obj2.plan_comp_salud > 16*self.obj3.valor_uvt:
            deduc_plan_comp_salud = round(16*self.obj3.valor_uvt)
        else:
            deduc_plan_comp_salud = round(self.obj2.plan_comp_salud)
        
        #calcular Dependinte de Cargo
        if self.obj1.dependiente_cargo == 'SI':
            if honorario_cal*0.1 > 32*self.obj3.valor_uvt:
                deduc_depen_cargo = round(32*self.obj3.valor_uvt)
            else:
                deduc_depen_cargo = round(honorario_cal*0.1)
        else:
            deduc_depen_cargo = 0
                
        #total deducciones
        total_deducciones = deduc_depen_cargo + deduc_plan_comp_salud + deduc_int_prest_vivienda
        
        #RENTAS EXTENSAS
        #calcular Aporte Renta Exenta
        if (self.obj2.aport_afc + self.obj2.aport_volun_emple) > 0.3*honorario_cal:
            aport_cuenta_afc = 0
        else:
            aport_cuenta_afc = self.obj2.aport_afc
        
        #calcular Aportes Voluntarios del Empleador
        if (self.obj2.aport_afc + self.obj2.aport_volun_emple) > 0.3*honorario_cal:
            aport_volun_empleador = 0
        else:
            aport_volun_empleador = self.obj2.aport_volun_emple
        
        #calcular Indemnizaciones Laborales
        indemni_lab = self.obj2.indem_lab
        
        #calcular total rentas extensas
        if (incr_aport_vol_pension + aport_cuenta_afc) > (self.obj2.valor + self.obj2.glosa)*0.3:
            total_rent_exten = round((self.obj2.valor + self.obj2.glosa)*0.3)
        else:
            total_rent_exten = round(incr_aport_vol_pension + aport_cuenta_afc)
        
        #calcular total rentas extensas dos
        total_rent_exten_dos = indemni_lab + aport_volun_empleador + aport_cuenta_afc
       
        #TOTAL RENTAS EXTENSAS
        # calcular renta extensa laboral 
        if honorario_cal == 0:
            tasa_re_rent_exent_lab = 0
        else:
            tasa_re_rent_exent_lab = honorario_cal - total_ingre_no_rent - total_deducciones  - total_rent_exten_dos
        
        re_rent_exent_lab = round(tasa_re_rent_exent_lab*(self.obj2.rent_exten_lab/100))
        
        #calcular Total Deducciones + Renta Exenta
        re_deduc_rent_exent = round(total_rent_exten+total_deducciones+re_rent_exent_lab)
        
        if honorario_cal == 0:
            tasa_re_deduc_rent_exent = 0
        else:
            tasa_re_deduc_rent_exent = round((re_deduc_rent_exent/(honorario_cal - total_ingre_no_rent))*100,2)
        
        #calcular Tope Deducciones + Renta Extensa
        if honorario_cal == 0:
            re_tope_rent_exent_lab = 0
        else:
            re_tope_rent_exent_lab = round((honorario_cal-total_ingre_no_rent)*(self.obj2.top_deduc_rent_exte/100))
        
        #calcular Total Base Gravable para Retención
        if honorario_cal == 0:  
            re_total_base_grav_reten = 0
        else:
            if re_deduc_rent_exent > re_tope_rent_exent_lab:
                re_total_base_grav_reten = honorario_cal - total_ingre_no_rent - re_tope_rent_exent_lab
            else:
                re_total_base_grav_reten = honorario_cal - total_ingre_no_rent - re_deduc_rent_exent
         
        #calcular Valor base gravable en UVT
        re_base_grav_reten_uvt = round(re_total_base_grav_reten/self.obj3.valor_uvt,2)
        
        print('esta es la base', re_base_grav_reten_uvt)
        #calcular retencion en la fuente expresada en UVT
        re_fuente_uvt = 0
        for i in self.obj4:
            if re_base_grav_reten_uvt > i.minimo and re_base_grav_reten_uvt <= i.maximo:
                re_fuente_uvt = round(((re_base_grav_reten_uvt - i.resta)*(i.porcent/100)) + i.adicion,1)
        
        #calcular retencion en pesos
        re_valor_reten = round(re_fuente_uvt*self.obj3.valor_uvt)
        
        return (honorario_cal, 
                incr_aport_pension, 
                incr_solida_pensional, 
                incr_aport_salud, 
                incr_aport_arl, 
                incr_aport_vol_pension,
                aport_volun_empleador,
                indemni_lab, 
                re_rent_exent_lab, 
                re_deduc_rent_exent, 
                re_tope_rent_exent_lab, 
                re_total_base_grav_reten,
                re_valor_reten, 
                deduc_int_prest_vivienda, 
                deduc_plan_comp_salud, 
                deduc_depen_cargo, 
                re_base_grav_reten_uvt, 
                re_fuente_uvt,
                aport_cuenta_afc,
                
                total_ingre_no_rent,
                total_deducciones,
                total_rent_exten_dos
                
                )