from django.core.mail import send_mail
from django.conf import settings


def send_reminder_email(user_email, medication_name):
    subject = "⏰ Recordatorio de Medicación"
    message = f"Hola, recuerda tomar tu medicamento: {medication_name} hoy."
    from_email = settings.EMAIL_HOST_USER  # El remitente
    recipient_list = [user_email]  # Lista de destinatarios

    send_mail(subject, message, from_email, recipient_list)
