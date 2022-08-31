from pyexpat import model
from django.shortcuts import render,redirect
from django.urls import reverse
from design.models import Contact
# Create your views here.

def home(request):
    return render(request, "index.html")

def gallery(request):
    return render(request, "gallery.html")

def about(request):
    return render(request, "about.html")

def thank_you(request):
    return render(request, "thanks.html")

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        contact = Contact(name = name, phone = phone, note = note)
        contact.save()
        return redirect(reverse('design:thanks'))
    else:
        return render (request, 'contact.html')

def services(request):
    return render(request, "services.html")            


