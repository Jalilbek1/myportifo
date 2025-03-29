from django.shortcuts import render, redirect
from .models import ContactMessage


# Create your views here.
def home_view(request):
    return render(request, 'creative.html')


def contact_view(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Bazaga saqlash
        ContactMessage.objects.create(name=name, email=email, message=message)

        return redirect("home")  # Foydalanuvchini o‘sha sahifaga qayta yo‘naltirish

    return redirect("home")


def switch_language(request):
    lang = request.GET.get('lang', 'uz')  # Default O'zbekcha
    if lang == 'uz':
        return render(request, 'creative.html')
    elif lang == 'ru':
        return render(request, 'creativeru.html')
    elif lang == 'en':
        return render(request, 'creativeen.html')
    else:
        return render(request, 'creative.html')  # Default holat


def contact_message(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Modelga saqlash
        ContactMessage.objects.create(name=name, email=email, message=message)

        return redirect('home')  # Xabar yuborilgandan keyin bosh sahifaga qaytarish

    return render(request, 'contact.html')  # Sahifani qaytarish
