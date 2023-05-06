from django.shortcuts import render
from .models import Works
from .utils import search_works


def home(request):
    works = Works.objects.all()
    context = {
        'works': works,
    }
    return render(request, 'portfolio/home.html', context)


def catalog(request):
    works, search_query = search_works(request)
    context = {
        'works': works,
        'search_query': search_query,
    }
    return render(request, 'portfolio/catalog.html', context)


def work_main(request, pk):
    work_obj = Works.objects.get(id=pk)
    context = {
        'work': work_obj,
    }
    return render(request, 'portfolio/work_main.html', context)
