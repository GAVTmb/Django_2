from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipes(request):
    dict_dish = {"dishes": []}
    for key in DATA.keys():
        dict_dish["dishes"].append(key)
    return render(request, 'home page.html', dict_dish)

def dish_omlet(request):
    return render(request, 'omlet.html', DATA)

def dish_pasta(request):
    return render(request, 'pasta.html', DATA)

def dish_buter(request):
    return render(request, 'buter.html', DATA)


