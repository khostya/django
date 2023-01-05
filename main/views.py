from django.shortcuts import render


def about(request):
    return render(request, "about.html")


def demand(request):
    return render(request, "demand.html")


def geography(request):
    return render(request, "geography.html")


def skills(request):
    return render(request, "skills.html")


def vacancies(request):
    return render(request, "vacancies.html")

