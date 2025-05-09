from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicationReminder
from .forms import MedicationReminderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import send_reminder_email
from django.core.mail import send_mail
from django.http import HttpResponse
import os
import requests


# @login_required
def home(request):
    return render(request, 'reminders/home.html')


def delete_medication_reminder(request, pk):
    reminder = get_object_or_404(MedicationReminder, pk=pk)
    reminder.delete()
    return redirect('add_reminder')

def add_medication_reminder(request):
    if request.method == "POST":
        form = MedicationReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_reminder')
    else:
        form = MedicationReminderForm()

    reminders = MedicationReminder.objects.all()
    return render(request, 'reminders/add_medication_reminder.html', {'form': form, 'reminders': reminders})


# Registro de Usuario
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords must match')
            return redirect('register')

            # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso. Por favor, elige otro.")
            return redirect("register")  # Redirigir al formulario de registro

        user = User.objects.create_user(username, email, password)
        user.save()

        # Enviar correo de bienvenida
        send_reminder_email(email, "¡Bienvenido a MedReminder! 🏥")

        messages.success(request, 'Account created')
        return redirect('login')
    return render(request, 'reminders/register.html')


# Inicio de Sesión
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print("Usuario autenticado:", user)  # Agrega este print para depuración

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'reminders/login.html')


# Cierre de sesion
def user_logout(request):
    logout(request)
    return redirect('login')


def send_test_email(request):
    subject = "Prueba de Mailgun"
    message = "¡Hola! Este es un correo de prueba enviado con Mailgun desde Django."
    from_email = "postmaster@sandbox262e885404534b83b6497732db815c7c.mailgun.org"
    recipient_list = ["thomasbu2004@gmail.com"]  # Reemplaza con tu correo

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse("Correo enviado correctamente")


def send_simple_message(request):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox262e885404534b83b6497732db815c7c.mailgun.org/messages",
        auth=("api", os.getenv('API_KEY', 'API_KEY')),
        data={"from": "Mailgun Sandbox <postmaster@sandbox262e885404534b83b6497732db815c7c.mailgun.org>",
              "to": "Thomas Buitrago <tbuitragou@eafit.edu.co>",
              "subject": "Hello Thomas Buitrago",
              "text": "Congratulations Thomas Buitrago, you just sent an email with Mailgun! You are truly awesome!"})
