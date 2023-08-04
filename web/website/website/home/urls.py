from django.contrib import admin
from django.urls import path, include
from website.home import views

app_name = "website"
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('category/<str:category>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('contact/', views.contactView, name='contact'),
    path('references/', views.references, name='references'),
    path('search/', views.search, name='search'),
    path("success", views.success, name="success"),
]
