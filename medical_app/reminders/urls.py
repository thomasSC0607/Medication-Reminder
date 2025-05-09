from django.urls import path
from . import views
from .views import register, user_login, user_logout, send_test_email, send_simple_message

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', views.home, name='home'),
    path('add/', views.add_medication_reminder, name='add_medication_reminder'),
    path('add/save', views.add_medication_reminder, name='add_reminder'),
    path('send-test-email/', send_test_email, name='send_test_email'),
]
