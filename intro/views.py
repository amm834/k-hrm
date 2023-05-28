from django.shortcuts import render

def home(request):
    return render(request, 'intro/home.html')

def features(request):
    return render(request, 'intro/features.html')

def pricing(request):
    return render(request, 'intro/pricing.html')

def about(request):
    return render(request, 'intro/about.html')

def contact(request):
    return render(request, 'intro/contact.html')