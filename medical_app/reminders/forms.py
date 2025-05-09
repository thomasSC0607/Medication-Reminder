from django import forms
from .models import MedicationReminder

class MedicationReminderForm(forms.ModelForm):
    days_of_week = forms.MultipleChoiceField(
        choices=[
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
            ('Sábado', 'Sábado'),
            ('Domingo', 'Domingo'),
        ],
        widget=forms.CheckboxSelectMultiple,
    )

    start_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'Selecciona la fecha de inicio'
        })
    )

    end_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control datepicker',
            'placeholder': 'Selecciona la fecha de fin'
        })
    )

    class Meta:
        model = MedicationReminder
        fields = ['medication_name', 'days_of_week', 'start_date', 'end_date']
        widgets = {
            'medication_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
