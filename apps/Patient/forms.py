from django import forms 
from .models import Patient

# Create the form class.
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        exclude = ('date',)
        
        widgets = {
            'full_name' : forms.TextInput(attrs={'placeholder': 'ชื่อ นามสกุล'}),
            'atk_date' : forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'}),
            'rt_pcr' : forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'}),
            'birth_day' : forms.DateInput(format=('%Y-%m-%d'),attrs={'type': 'date'}),
            'symptom' : forms.Textarea(attrs={'rows':2}),            
            'address' : forms.Textarea(attrs={'rows':2}),            
        }
