from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from django.utils.timezone import now
from reminders.models import Reminder


class SendRemindersCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # Una vez al día
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'reminders.send_reminders'  # Código único

    def do(self):
        today = now().date()
        reminders = Reminder.objects.filter(start_date=today)

        for reminder in reminders:
            send_mail(
                subject=f"Recordatorio: {reminder.medication_name}",
                message=f"No olvides tomar tu medicamento: {reminder.medication_name}",
                from_email="tu-correo@dominio.com",
                recipient_list=[reminder.user_email],
                fail_silently=False,
            )
