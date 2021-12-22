from django.shortcuts import render

# from django.http import HttpResponse


def home_page(request):
    return render(request, "leads/home_page.html")


def second_page(request):
    return render(request, "second_page.html")
