from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages   

def index(request):
    context = {
        'variable1': "this is a sent",
        'variable2': "Harry is Great"
    }
    # messages.success(request, "this is a test msg")
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        print(name, email, phone, desc)

        if email:
            Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                desc=desc,
                date=datetime.today()
            )
            messages.success(request, "Your message has been sent!")

    return render(request, 'contact.html')