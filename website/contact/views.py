from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Daten extrahieren
            cd = form.cleaned_data
            subject = f"Neue Kontaktanfrage von {cd['first_name']} {cd['last_name']}"
            message = f"""
Vorname: {cd['first_name']}
Nachname: {cd['last_name']}
Firma: {cd.get('company', '')}
E-Mail: {cd['email']}
Telefon: {cd.get('phone', '')}

Nachricht:
{cd['message']}
            """.strip()
            send_mail(
                subject,
                message,
                cd["email"],
                ["contact@andreaskellerer.com"],  # oder settings.ADMINS
            )
            messages.success(request, "Vielen Dank! Ihre Nachricht wurde versendet.")
            return redirect("home")  # oder wohin du nach dem Absenden willst
    else:
        form = ContactForm()
    return render(request, "index.html", {"form": form})

def my_contact(request):
    return render(request, "contact.html")