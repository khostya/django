from django.shortcuts import render, HttpResponsePermanentRedirect


def about(request):
    return render(request, "about.html")


def demand(request):
    return render(request, "demand.html")


def geography(request):
    return render(request, "geography.html")


def skills(request):
    return render(request, "skills.html")


def main(request):
    return HttpResponsePermanentRedirect("about")


def vacancies(request):
    return render(request, "vacancies.html")

