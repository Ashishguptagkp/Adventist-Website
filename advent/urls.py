from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('child',views.child, name='child'),
    path('childgallery',views.children, name='childgallery'),
    path('com',views.com, name='com'),
    path('commni',views.commni, name='commni'),
    path('contact',views.contact, name='contact'),
    path('event',views.event, name='event'),
    path('health',views.health, name='health'),
    path('help',views.help, name='help'),
    path('sabbat',views.sabbat, name='sabbat'),
    path('sti',views.sti, name='sti'),
    path('study',views.study, name='study'),
    path('wome',views.wome, name='wome'),
    path('women',views.women, name='women'),
    path('you',views.you, name='you'),
    path('youth',views.youth, name='youth'),
    path('contactForm',views.handleContactForm, name='contactForm'),
    
]
