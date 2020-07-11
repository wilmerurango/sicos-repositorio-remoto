import numpy as np
from django.contrib import messages
class defprov():
    obj1 = {}
    obj2 = {}
    obj3 = {}
    obj4 = {}
    obj5 = {}
    
    #incializar los parametros
    def __init__(self, Objeto1=0, Objeto2=0, Objeto3=0, Objeto4=0,Objeto5=0):
        self.obj1 = Objeto1
        self.obj2 = Objeto2
        self.obj3 = Objeto3
        self.obj4 = Objeto4
        self.obj5 = Objeto5
    
    #esta funcion arroja un detalle de manera automatica para aquellos proveedores que tienen uns distribucion porcentual y ademas unos rubros al 100%
    def detalle_automatico(self):

        # obj1: cpp_proveedor
        # obj2: distribucion
        
        contar_induc = self.obj2.count()
        if contar_induc != 0:
            sumaT = 0
            vector_ind= np.zeros([contar_induc,1])
            i=0
            for j in self.obj2:
                vector_ind[i]= (j.distrib/100)*self.obj1.valor_factura
                sumaT += vector_ind[i]
                i = i + 1     
            return vector_ind
        
    def calcular_cpp_proveedor(self):
        #NOTA
        #obj1: centro_costo
        #obj2: distribucion (ya viene filtrado)
        #obj3: cpp_proveedor_detalle
        #obj4: cpp_proveedor (filtrado), "es un objeto unico (get)"
        #obj5: categoria (esta es la categoria de los productos)
        
        
        cont_cc = self.obj1.count()#cuenta cuantos objetos tiene el objeto centro_costos
        contar_detalle = self.obj3.count()#cuenta cuentos elementos tiene el objeto cpp_proveedor_detalle
        
        
        if self.obj5.first().id == self.obj2.last().producto.categoria.id:#esta es la categoria de gases y debe colocarse de primero.

            mat_distri = np.zeros([cont_cc,contar_detalle+1])
            matriz = np.zeros([cont_cc,contar_detalle+1])
            matriz_detalle = np.zeros([cont_cc,contar_detalle+1])#esat matriz no se utiliza en los gases solo se da uso en la sangre, ero hay que colocarlo para que no tire un error al retornar los elemtos
            matriz_iva = np.zeros([cont_cc,contar_detalle+2])
            
            contm = 0 #recorre las filas de la "matriz"
            for i in self.obj1:#recorrer los centros de costo del objeto1
                cont1 = 0
                for k in self.obj3:#recorre cada detalle facturado en la cpp
                    distribucion_tempo = self.obj2.filter(producto = k.producto.id)
                    for j in distribucion_tempo:#recorrer los centros de costos correspondientes al producto seleccionado

                        if i.id == j.centro_costo.id:
                            matriz[contm,cont1] = (j.distrib/100)*((k.cant_produc*j.producto.precio)+(k.cant_flete*k.valor_flete))
                            mat_distri[contm,cont1] = j.distrib
                            mat_distri[contm,contar_detalle] = j.cuenta
                            if j.meneja_iva == 'SI':
                                matriz_iva[contm,cont1] = (j.distrib/100)*(j.valor_iva/100)*(k.cant_produc*j.producto.precio)
                                matriz_iva[contm,contar_detalle+1] = j.cuenta_iva

                    cont1 += 1 
            
                matriz[contm, contar_detalle] = sum(matriz[contm,0:contar_detalle+1])
                matriz_iva[contm, contar_detalle] = sum(matriz_iva[contm,0:contar_detalle+1])
                
                contm += 1

            return (matriz, matriz_iva, mat_distri, matriz_detalle)
        
        else:#aqui se recibe el resto de las categorias

            mat_distri = np.zeros([cont_cc,1])
            matriz = np.zeros([cont_cc,1])
            matriz_iva = np.zeros([cont_cc,2])
            matriz_detalle = np.zeros([cont_cc,contar_detalle +2 ])
            
            contm = 0
            for i in self.obj1:#centro de costo
                acum = 0
                contcolum = 0
                for k in self.obj3:#recorre cada detalle facturado en la cpp
                    if i.id == k.centro_costo.id:
                        acum += (k.cant_produc*k.valor_produc)+(k.valor_flete/contar_detalle) 
                        matriz[contm, 0] = acum
                        matriz_detalle[contm,contcolum] = (k.cant_produc*k.valor_produc)+(k.valor_flete/contar_detalle)  

                    contcolum += 1
                        
                matriz_detalle[contm, contar_detalle] = sum(matriz_detalle[contm,0:contar_detalle+1])
                contm += 1  
                
            #COPIA[almacenar cuenta de iva]================================================
            contm = 0
            for i in self.obj1:#recorrer los centros de costo del objeto1
                cont1 = 0
                for k in self.obj3:#recorre cada detalle facturado en la cpp
                    distribucion_tempo = self.obj2.filter(producto = k.producto.id)
                    for j in distribucion_tempo:#recorrer los centros de costos correspondientes al producto seleccionado

                        if i.id == j.centro_costo.id:
                            matriz_iva[contm,1]=j.cuenta

                    cont1 += 1
                
                contm += 1
            #===================================================== 
                
            for m in range(cont_cc):
                mat_distri[m,0]= round((matriz[m,0]/np.sum(matriz))*100,2)
            
            return (matriz, matriz_iva, mat_distri, matriz_detalle)