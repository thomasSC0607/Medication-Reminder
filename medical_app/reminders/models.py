from django.db import models


class MedicationReminder(models.Model):
    medication_name = models.CharField(max_length=100)
    days_of_week = models.CharField(max_length=50)  # Ejemplo: "Lunes, Miércoles, Viernes"
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.medication_name
