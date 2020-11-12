from .models import Producta
from django import forms

class AddProduct (forms.ModelForm):

    class Meta:
        model = Producta
        fields = '__all__'
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'})
           
        }




