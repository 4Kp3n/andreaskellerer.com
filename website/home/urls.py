from django.contrib import admin
from django.urls import path, include
from website.home import views

app_name = "website"
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('category/<str:category>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('contact/', views.contactView, name='contact'),
    path('impressum/', views.impressum, name='impressum'),
    path('search/', views.search, name='search'),
    path('services', views.services, name='services'),
    path('testerix', views.testerix, name='testerix'),
    path("success", views.success, name="success"),
]
