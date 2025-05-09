from django.core.management.base import BaseCommand
from reminders.models import MedicationReminder
import random
from datetime import date, timedelta


class Command(BaseCommand):
    help = "Poblar la base de datos con recordatorios de medicación"

    def handle(self, *args, **kwargs):
        medicamentos_lista = [
            "Ibuprofeno", "Paracetamol", "Amoxicilina", "Omeprazol", "Metformina",
            "Loratadina", "Aspirina", "Losartan", "Salbutamol", "Atorvastatina"
        ]

        dias_opciones = [
            "Lunes, Miércoles, Viernes",
            "Martes, Jueves",
            "Todos los días",
            "Sábado, Domingo",
            "Lunes, Martes, Miércoles, Jueves, Viernes"
        ]

        # Borrar datos anteriores (opcional)
        MedicationReminder.objects.all().delete()

        # Poblar la base de datos con 10 recordatorios
        for _ in range(10):
            medicamento = random.choice(medicamentos_lista)
            dias = random.choice(dias_opciones)
            fecha_inicio = date.today() + timedelta(days=random.randint(1, 10))
            fecha_fin = fecha_inicio + timedelta(days=random.randint(5, 15))

            MedicationReminder.objects.create(
                medication_name=medicamento,
                days_of_week=dias,
                start_date=fecha_inicio,
                end_date=fecha_fin
            )

        self.stdout.write(self.style.SUCCESS("✅ Base de datos poblada con 10 recordatorios aleatorios 🎉"))
