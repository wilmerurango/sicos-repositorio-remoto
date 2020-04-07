import numpy as np
class funcion_serv():
    obj1 = {}
    obj2 = {}
    obj3 = {}
    obj4 = {}
    obj5 = {}
    
    def __init__(self, Objeto1 = 0, Objeto2 = 0, Objeto3= 0, Objeto4 = 0, Objeto5 = 0):
        self.obj1 = Objeto1
        self.obj2 = Objeto2
        self.obj3 = Objeto3
        self.obj4 = Objeto4
        self.obj5 = Objeto5
    
    #calcular las distribuiones del costo de las facturas
    def distri_serv(self):
        #obj1: cpp_serv_public
        #obj2: distri_serv_public
        
        contar_distri = self.obj2.count()
        
        #distribucion del costo
        if contar_distri != 0:
            vector_distri = np.zeros([contar_distri,2])
            cont = 0
            for i in self.obj2:
                vector_distri[cont,0] = (i.distri/100)*self.obj1.costo
                cont += 1
        
        #calcular el iva 
        for i in range(contar_distri):
            vector_distri[i,1] = ((self.obj1.iva/100)*self.obj1.costo)*(vector_distri[i,0]/self.obj1.costo)
           
        return vector_distri