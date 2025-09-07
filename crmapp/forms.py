from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows':3}),
            'notes': forms.Textarea(attrs={'rows':3}),
        }
