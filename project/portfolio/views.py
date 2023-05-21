from django.shortcuts import render
from .models import Works
from .utils import search_works, paginate_works


def home(request):
    works = Works.objects.all()
    context = {
        'works': works,
    }
    return render(request, 'portfolio/home.html', context)


def catalog(request):
    works, search_query = search_works(request)
    custom_range, works = paginate_works(request, works, 6)

    context = {
        'works': works,
        'search_query': search_query,
        'custom_range': custom_range,

    }
    return render(request, 'portfolio/catalog.html', context)


def work_main(request, pk):
    work_obj = Works.objects.get(id=pk)
    context = {
        'work': work_obj,
    }
    return render(request, 'portfolio/work_main.html', context)


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    return render(request, 'portfolio/contact.html')
