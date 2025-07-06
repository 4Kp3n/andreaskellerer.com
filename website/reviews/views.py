from django.shortcuts import render

# Create your views here.
from reviews.models import Review

def index(request):
    reviews = Review.objects.filter(is_approved=True).order_by('-created_at')[:6]  # z. B. letzte 6
    return render(request, 'index.html', {'reviews': reviews})