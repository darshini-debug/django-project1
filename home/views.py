from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "variable1": "harry is a great guy",
        "variable2": "priya is a great girl"
    }
    messages.success(request, "this is a test message")
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("welcome to about page")


def services(request):
    query = request.GET.get('query', '')  # ✅ get search text
    context = {
        'query': query.lower()  # ✅ send to template
    }
    return render(request, 'services.html', context)
    # return HttpResponse("welcome to services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if not name or not email:
            return render(request, 'contact.html', {'error': 'Name and Email are required'})

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
        return redirect('/contact/')

    return render(request, 'contact.html')
    # return HttpResponse("welcome to contact page")
