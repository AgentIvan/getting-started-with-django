from django.shortcuts import render

from .models import Lead

# from django.http import HttpResponse


def home_page(request):
    return render(request, "leads/home_page.html")


def second_page(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, "second_page.html", context)
