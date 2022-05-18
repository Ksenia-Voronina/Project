from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def sofia(request):
    return render(request, 'sofia.html')


def monument(request):
    return render(request, 'monument.html')


def yaroslavovo_dvorishche(request):
    return render(request, 'yaroslavovo_dvorishche.html')


def yurievo(request):
    return render(request, 'yurievo.html')


def ryurikovo_gorodishche(request):
    return render(request, 'ryurikovo_gorodishche.html')


def data(request):
    return render(request, 'data.html')


