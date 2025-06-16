from django.shortcuts import render


def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def portfolio(request):
    return render(request, "main/portfolio.html")


def sertifikat(request):
    return render(request, "main/sertifikat.html")


def contact(request):
    return render(request, "main/contact.html")
