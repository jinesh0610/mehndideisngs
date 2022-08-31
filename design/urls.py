from django.urls import path
from design import views

app_name = 'design'


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about-us/', views.about, name = 'about' ),
    path('contact-us/', views.contact, name ='contact'),
    path('thank_you/', views.thank_you, name ='thanks'),
    path('gallery/', views.gallery, name = 'gallery'),
     path('services/', views.services, name = 'services'),
]