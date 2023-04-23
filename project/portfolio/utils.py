from .models import Works
from django.db.models import Q


def search_works(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    works = Works.objects.distinct().filter(Q(title__icontains=search_query) |
                                            Q(material__icontains=search_query))

    return works, search_query
