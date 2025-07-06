# contact/urls.py
from django.urls import path
from .views import contact_view, my_contact

app_name = "contact"

urlpatterns = [
    path("danke/", my_contact, name="my_contact"),
]