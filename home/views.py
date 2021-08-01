from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages 

# Create your views here.
def index(request):
    context = {
        "variable1": "Ajit is great. He is the coder",
        "variable2":"Rohan is great"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html" )

def blog(request):
    return render(request, "blog.html" )

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent. Thank you for filling this form. Re-visit for more educational content!!')
    
    return render(request, "contact.html" )
