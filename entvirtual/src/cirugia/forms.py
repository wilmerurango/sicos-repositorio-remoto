from django import forms
from cirugia.models import *

class tipo_procform(forms.ModelForm):
    
    archivo = models.FileField()
    class Meta:
        model = tipo_proc
        
        fields = (
            '__all__'   
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
            
class procedimientoform(forms.ModelForm):
    class Meta:
        model = procedimiento
        
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })        
            
class concepto_honorarioform(forms.ModelForm):
    class Meta:
        model = concepto_honorario
        
        fields  =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
        self.fields['nombre_concep_hon'].widget.attrs.update({
                                        'onkeyup':"mayus(this);",
                                        })
                 
class nombre_canastaform(forms.ModelForm):
    class Meta:
        model = nombre_canasta
        
        fields =(
            '__all__'
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
   
class concepto_canastaform(forms.ModelForm):
    class Meta:
        model = concepto_canasta
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
            
        self.fields['nombre_canasta'].widget.attrs.update({
                                            'onkeyup':"mayus(this);",
                                            })
       
class positionform(forms.ModelForm):
    class Meta:
        model = position
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class canastaform(forms.ModelForm):
    
    class Meta:
        model = canasta
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
        self.fields['costo_tot'].widget.attrs['readonly'] = True 

class honorarioform(forms.ModelForm):
    
    class Meta:
        model = honorario
        
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class constanteform(forms.ModelForm):
    class Meta:
        model = constante
        
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class concepto_salarioform(forms.ModelForm):
    
    class Meta:
        model = concepto_salario
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
            
        self.fields['nombre_concep_sal'].widget.attrs.update({
                                            'onkeyup':"mayus(this);",
                                            })

class estanciaform(forms.ModelForm):
    class Meta:
        model = estancia
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })
            
class tipo_estanciaform(forms.ModelForm):
    class Meta:
        model = tipo_estancia
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class salarioform(forms.ModelForm):
    class Meta:
        model = salario
        fields =(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })

class consultaform(forms.ModelForm):
    class Meta:
        model = consulta
        
        fields =(
            '__all__'
        )
    
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control' 
            })
        

        self.fields['procedimiento'].queryset = procedimiento.objects.none()
        
        if 'tipo_proc' in self.data:
            try:
                tipo_proc_id = int(self.data.get('tipo_proc'))
                self.fields['procedimiento'].queryset = procedimiento.objects.filter(tipo_proc_id=tipo_proc_id).order_by('nombre_proc')
            except (ValueError, TypeError):
                print('Error') # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['procedimiento'].queryset = self.instance.tipo_proc.procedimiento_set.order_by('nombre_proc')
