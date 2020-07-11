from django import forms
from django.forms.widgets import SelectDateWidget
import datetime
import copy
from django.forms import ModelChoiceField

from facturacion.models import *

#LOGIN
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model=User
        fields=(

            '__all__'
        )
    # def __init__(self, *args, **kwargs):  
    #     super().__init__(*args, **kwargs)  
    #     for field in iter(self.fields):  
    #         self.fields[field].widget.attrs.update({  
    #             'class': 'form-control'  
    #         })  


#=====================SERVICIOS =======================================
class tipo_servform(forms.ModelForm):
    class Meta:
        model = tipo_serv
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     

class serv_publicform(forms.ModelForm):
    class Meta:
        model = serv_public
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     
        self.fields['fecha'].widget.attrs['readonly'] = True  
        
class cpp_serv_publicform(forms.ModelForm):
    class Meta:
        model = cpp_serv_public
        
        fields = (
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     
        self.fields['fecha'].widget.attrs['readonly'] = True  
        self.fields['total'].widget.attrs['readonly'] = True
    
class cuenta_aux_servform(forms.ModelForm):
    class Meta:
        model = cuenta_aux_serv
        
        fields = (
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     
  
class distri_serv_publicform(forms.ModelForm):
    class Meta:
        model = distri_serv_public
        
        fields = (
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     
        self.fields['fecha_distri'].widget.attrs['readonly'] = True  
        
class cpp_servi_detalleform(forms.ModelForm):
    class Meta:
        model = cpp_servi_detalle
        
        fields = (
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     
        self.fields['fecha'].widget.attrs['readonly'] = True  
    
#PROVEEDORES
class cpp_proveedor_detalleform(forms.ModelForm):
    class Meta:
        model = cpp_proveedor_detalle

        fields=(
            '__all__'
        )
                
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     
        self.fields['fecha_cpp_prov_detal'].widget.attrs['readonly'] = True 
        self.fields['producto'].queryset = producto.objects.none()
        
        if 'categoria' in self.data:
            try:
                categoria_id = int(self.data.get('categoria'))
                self.fields['producto'].queryset = producto.objects.filter(categoria_id=categoria_id).order_by('nombre')
            except (ValueError, TypeError):
                print('Error') # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['producto'].queryset = self.instance.categoria.producto_set.order_by('nombre')     
              
class cuenta_auxform(forms.ModelForm):
    class Meta:
        model = cuenta_aux
        
        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  

class cpp_proveedorform(forms.ModelForm):
    class Meta:
        model = cpp_proveedor

        fields = (
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
                        
        self.fields['fecha_cpp_prov'].widget.attrs['readonly'] = True  
        self.fields['valor_cpp_prov'].widget.attrs['readonly'] = True  
    
class proveedorform(forms.ModelForm):
    class Meta:
        model = proveedor

        fields=(
            '__all__'
        )


    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fecharegistro_prov'].widget.attrs['readonly'] = True  
    
class productoform(forms.ModelForm):
    class Meta:
        model = producto
    
        fields =(
            '__all__'
        )
    
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
     
class categoriaform(forms.ModelForm):
    class Meta:
        model = categoria
        
        fields =(
            '__all__'
        )  
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  

class distribucionform(forms.ModelForm):
    class Meta:
        model = distribucion
        
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  

    
#=====================ARRIENDOS=======================================
class inductor_arriform(forms.ModelForm):
    class Meta:
        model = inductor_arri

        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
            self.fields['fecha_induc'].widget.attrs['readonly'] = True 

class cpp_arriendo_detalleform(forms.ModelForm):
    class Meta:
        model=cpp_arriendo_detalle
        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inductor_arri'].queryset = inductor_arri.objects.none()

        if 'arriendo' in self.data:
            try:
                arriendo_id = int(self.data.get('arriendo'))
                self.fields['inductor_arri'].queryset = inductor_Arri.objects.filter(arriendo=arriendo_id).order_by('arriendo')
            except (ValueError, TypeError):
                print('Error') # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['inductor_arri'].queryset = self.instance.arriendo.inductor_arri_set.order_by('arriendo')


    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fecha_cpp_arri_detal'].widget.attrs['readonly'] = True  
        self.fields['valor_cpp_arri_detal'].widget.attrs['readonly'] = True 
        # self.fields['cpp_arriendo'].widget.attrs['readonly'] = True 
        # self.fields['arriendo'].widget.attrs['readonly'] = True 
  
class cpp_arriendoform(forms.ModelForm):
    class Meta:
        model = cpp_arriendo

        fields = (
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['valor_cont'].widget.attrs['readonly'] = True  
        self.fields['fecha_cpp_arri'].widget.attrs['readonly'] = True  
        
class arriendoform(forms.ModelForm):
    class Meta:
        
        model = arriendo

        fields = (
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fechafact_arri'].widget.attrs['readonly'] = True  

class cuenta_arriendo_auxform(forms.ModelForm):
    class Meta:
        model = cuenta_arriendo_aux
        
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  

#============ SERVICIOS MEDICOS================================

class cpp_servicio_medico_detalleform(forms.ModelForm):
    class Meta:
        model=cpp_servicio_medico_detalle

        fields=(
            '__all__'
        )


    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fecha_sm_detalle'].widget.attrs['readonly'] = True

class cpp_servicio_medicoform(forms.ModelForm):
    class Meta:
        model = cpp_servicio_medico
        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fecha_cpp_sm'].widget.attrs['readonly'] = True
        self.fields['valor_sm'].widget.attrs['readonly'] = True

class cpp_servicio_medicoform(forms.ModelForm):
    class Meta:
        model=cpp_servicio_medico

        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fecha_cpp_sm'].widget.attrs['readonly'] = True
        self.fields['valor_sm'].widget.attrs['readonly'] = True

class servicio_medicoform(forms.ModelForm):

    class Meta:
        model=servicio_medico

        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fechafact_servm'].widget.attrs['readonly'] = True


#=====================ESPECIALISTAS=============================
class Tarifaform(forms.ModelForm):
    class Meta:
        model = Tarifa
        
        fields =(
            '__all__'
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['fecha_inicio'].widget.attrs['readonly'] = True
        self.fields['fecha_final'].widget.attrs['readonly'] = True
                
class cuenta_retenform(forms.ModelForm):
    class Meta:
        model = cuenta_reten
        
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  

class centro_actividadform(forms.ModelForm):
    class Meta:
        model = centro_actividad
        
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })   

class retencionform(forms.ModelForm):
    class Meta:
        model = retencion
        
        fields = (
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })   
            # self.fields['xxx'].widget.attrs['readonly'] = True
  
class contratoform(forms.ModelForm):
    class Meta:
        model = contrato
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            }) 
        self.fields['fecha'].widget.attrs['readonly'] = True

class uvtform(forms.ModelForm):
    class Meta:
        model = uvt
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            }) 

class reten_383form(forms.ModelForm):
    class Meta:
        model = reten_383
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            }) 

class sub_activityform(forms.ModelForm):
    class Meta:
        model=sub_activity

        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })   

class actividadform(forms.ModelForm):
    class Meta:
        model=actividad

        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })    

class centro_costoform(forms.ModelForm):
    class Meta:
        model= centro_costo
        fields=(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        
class especialistaform(forms.ModelForm):
    fechafact_esp = forms.DateInput() 
    class Meta:

        model=especialista

        fields =(
            '__all__'
        )
       
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fechafact_esp'].widget.attrs['readonly'] = True

class fac_especialistaform(forms.ModelForm):
    fechafac_esp = forms.DateInput() 
    class Meta:

        model= fac_especialista

        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
        self.fields['fechafac_esp'].widget.attrs['readonly'] = True
        self.fields['acum'].widget.attrs['readonly'] = True
        self.fields['valor'].widget.attrs['readonly'] = True

class tipo_factform(forms.ModelForm):
    class Meta:

        model = tipo_fact

        fields=(
            '__all__'
        )


        widgets={
           'name_fact': forms.TextInput(attrs={'class':'form-control'}),
        }
            
class fac_especialista_detalleform(forms.ModelForm):
    fechafac_detalle = forms.DateInput() 
    
    class Meta:
        model=fac_especialista_detalle
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     
            self.fields['fechafac_detalle'].widget.attrs['readonly'] = True
            
        self.fields['centro_actividad'].queryset = centro_actividad.objects.none()
       
        if 'centro_costo' in self.data:
            try:
                centro_costo_id = int(self.data.get('centro_costo'))
                self.fields['centro_actividad'].queryset = centro_actividad.objects.filter(centro_costo_id=centro_costo_id).order_by('actividad')
            except (ValueError, TypeError):
                print('Error') # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['centro_actividad'].queryset = self.instance.centro_costo.centro_actividad_set.order_by('actividad')

class especialista_cpp_auxform(forms.ModelForm):

    class Meta:
        model=especialista_cpp_aux

        fields=(
            '__all__'

        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  
  