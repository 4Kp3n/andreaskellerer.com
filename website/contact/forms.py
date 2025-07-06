# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label="Vorname", max_length=100, widget=forms.TextInput(attrs={"class": "w-full p-3 bg-gray-800 rounded"}))
    last_name = forms.CharField(label="Nachname", max_length=100, widget=forms.TextInput(attrs={"class": "w-full p-3 bg-gray-800 rounded"}))
    company = forms.CharField(label="Firma", required=False, widget=forms.TextInput(attrs={"class": "w-full p-3 bg-gray-800 rounded"}))
    email = forms.EmailField(label="E-Mail", widget=forms.EmailInput(attrs={"class": "w-full p-3 bg-gray-800 rounded"}))
    phone = forms.CharField(label="Telefon", required=False, widget=forms.TextInput(attrs={"class": "w-full p-3 bg-gray-800 rounded"}))
    message = forms.CharField(label="Nachricht", widget=forms.Textarea(attrs={"class": "w-full p-3 bg-gray-800 rounded", "rows": 4}))
    consent = forms.BooleanField(label="Ich stimme der Datenverarbeitung zu", widget=forms.CheckboxInput(attrs={"class": "accent-cyan-500"}))
