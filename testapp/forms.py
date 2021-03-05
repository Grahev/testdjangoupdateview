from django import forms
from . models import myModel

class mainForm(forms.ModelForm):
    class Meta:
        model = myModel
        fields = '__all__'