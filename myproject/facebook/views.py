from django.shortcuts import redirect, render

from django.http import HttpResponse
# Create your views here.

from .models import register_info


def index(request):

    fetch_obj = register_info.objects.all()

    return render(request, 'home.html', {'fetch': fetch_obj})


def contact(request):
    return render(request, 'contact.html')


def save_information(request):

    if request.method == "POST":
        first_name = request.POST.get("fname")
        emailid = request.POST.get("email")
        Age = request.POST.get("age")
        gender = request.POST.get('gender')
        print(gender)

        save_info = register_info(
            name=first_name, email=emailid, age=Age, gender=gender)
        save_info.save()

    return redirect('home')
