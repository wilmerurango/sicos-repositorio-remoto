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

class rubroform(forms.ModelForm):
    class Meta:
        model = rubro
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


# class tiempo_procform(forms.ModelForm):
    
#     class Meta:
#         model = tiempo_proc
        
#         fields =(
#             '__all__'
#         )
        
#     def __init__(self, *args, **kwargs):  
#         super().__init__(*args, **kwargs)  
#         for field in iter(self.fields):  
#             self.fields[field].widget.attrs.update({  
#                 'class': 'form-control'  
#             })