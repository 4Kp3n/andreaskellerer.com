from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from website.home.models import Blog
#import random
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from .forms import ContactForm
import re

from reviews.models import Review

# New contact form
def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    # TODO add explicit check for POST method
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("/success")
        else:
            return HttpResponse('TEST')
    return render(request, "contact.html", {"form": form})

def success(request):
    return render(request, 'success.html')

# Create your views here.
def index (request):
    #blogs = Blog.objects.all()
    #random_blogs = random.sample(list(blogs), 3)
    #context = {'random_blogs': random_blogs}
    #return render(request, 'index.html', context)
    reviews = Review.objects.filter(is_approved=True).order_by('-created_at')[:3]
    return render(request, "index.html", {"reviews": reviews})

def about (request):
    return render(request, 'about.html')

def privacy (request):
    return render(request, 'privacy.html')

def impressum (request):
    return render(request, 'impressum.html')
def testerix (request):
    return render(request, 'testerix.html')

def contact (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        invalid_imput = ['', ' ']
        if name in invalid_imput or email in invalid_imput or phone in invalid_imput or message in invalid_imput:
            messages.error(request, 'One or more fields are empty!')
        else:
            email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            phone_pattern = re.compile(r'^[0-9]{10}$')

            if email_pattern.match(email) and phone_pattern.match(phone):
                form_data = {
                'name':name,
                'email':email,
                'phone':phone,
                'message':message,
                }
                message = '''
                From:\n\t\t{}\n
                Message:\n\t\t{}\n
                Email:\n\t\t{}\n
                Phone:\n\t\t{}\n
                '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
                send_mail('You got a mail!', message, '', ['dev.ash.py@gmail.com'])
                messages.success(request, 'Your message was sent.')
                # return HttpResponseRedirect('/thanks')
            else:
                messages.error(request, 'Email or Phone is Invalid!')
    return render(request, 'contact.html', {})

def services (request):
    return render(request, 'services.html')

#def blog(request):
#    return render(request, 'blog.html')
#   blogs = Blog.objects.all().order_by('-time')
#   paginator = Paginator(blogs, 3)
#   page = request.GET.get('page')
#   blogs = paginator.get_page(page)
#   context = {'blogs': blogs}
#   return render(request, 'blog.html', context)

def category(request, category):
    category_posts = Blog.objects.filter(category=category).order_by('-time')
    if not category_posts:
        message = f"No posts found in category: '{category}'"
        return render(request, "category.html", {"message": message})
    paginator = Paginator(category_posts, 3)
    page = request.GET.get('page')
    category_posts = paginator.get_page(page)
    return render(request, "category.html", {"category": category, 'category_posts': category_posts})

def categories(request):
    all_categories = Blog.objects.values('category').distinct().order_by('category')
    return render(request, "categories.html", {'all_categories': all_categories})

def search(request):
    query = request.GET.get('q')
    query_list = query.split()
    results = Blog.objects.none()
    for word in query_list:
        results = results | Blog.objects.filter(Q(title__contains=word) | Q(content__contains=word)).order_by('-time')
    paginator = Paginator(results, 3)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    if len(results) == 0:
        message = "Sorry, no results found for your search query."
    else:
        message = ""
    return render(request, 'search.html', {'results': results, 'query': query, 'message': message})

def blogpost (request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        context = {'blog': blog}
        return render(request, 'blogpost.html', context)
    except Blog.DoesNotExist:
        context = {'message': 'Blog post not found'}
        return render(request, '404.html', context, status=404)