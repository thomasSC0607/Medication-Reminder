from django.core.management.base import BaseCommand
from django.utils.timezone import now
from django.core.mail import send_mail
from medical_app.reminders.models import MedicationReminder


class Command(BaseCommand):
    help = "Envía recordatorios por correo a los usuarios según los días seleccionados"

    def handle(self, *args, **kwargs):
        # Obtener el día actual (Ejemplo: 'Lunes')
        today = now().strftime("%A")

        # Buscar recordatorios que coincidan con el día actual
        reminders = MedicationReminder.objects.filter(days_of_week__icontains=today)

        for reminder in reminders:
            send_mail(
                subject=f"Recordatorio: {reminder.medication_name}",
                message=f"Hoy es {today}, recuerda tomar tu medicamento: {reminder.medication_name}.",
                from_email="tu-correo@dominio.com",
                recipient_list=[reminder.user_email],
                fail_silently=False,
            )

        self.stdout.write(f"Se enviaron {reminders.count()} recordatorios para el día {today}.")
