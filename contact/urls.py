from django.urls import path
from . import views

app_name = "contact_app"
urlpatterns = [
    path("contact/", views.contact, name="contact"),
]
