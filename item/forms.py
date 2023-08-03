from django import forms
from .models import CV  # Importa el modelo del currículum si ya lo has definido en models.py

class CVForm(forms.ModelForm):
    class Meta:
        model = CV  # Reemplaza "CV" con el nombre de tu modelo si es diferente
        fields = '__all__'  # O especifica los campos que deseas mostrar en el formulario
