from django.http import HttpResponse
from django.shortcuts import render

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

def countpersons(DATA, servings, dish):
    context = {
        'recipe': {

        }
    }

    for ingredient, amount in DATA[dish].items():
        context['recipe'][ingredient] = round(amount * int(servings), 1)

    return context

def omlet(request):
    servings = request.GET.get('servings', 1)
    return render(request, 'calculator/index.html', countpersons(DATA, servings, 'omlet'))

def pasta(request):
    servings = request.GET.get('servings', 1)
    return render(request, 'calculator/index.html', countpersons(DATA, servings, 'pasta'))

def buter(request):
    servings = request.GET.get('servings', 1)
    return render(request, 'calculator/index.html', countpersons(DATA, servings, 'buter'))


