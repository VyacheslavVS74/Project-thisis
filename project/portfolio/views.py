from django.shortcuts import render, get_object_or_404, redirect

from .models import Works
from .utils import search_works, paginate_works
from crm.models import Order
from crm.forms import OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


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
    order_works = get_object_or_404(Works, id=pk)
    form = OrderForm(request.POST or None, initial={'order_works': order_works})
    if request.method == 'POST':
        if request.user.is_authenticated:
            if form.is_valid():
                form.order_name = request.user.first_name
                form.order_email = request.user.email
                form.save()
                messages.success(request, 'Заявка отправлена')
                return redirect('work-main', pk=order_works.id)
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'Заявка отправлена')
                return redirect('work-main', pk=order_works.id)
    context = {
        'order_works': order_works,
        'form': form,
    }
    return render(request, 'portfolio/work_main.html', context)


# def thanks_page(request):
#     work_name = Works.objects.first()
#     if request.method == 'POST':
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         name_work = work_name.title
#         element = Order(order_work=name_work, order_name=name, order_phone=phone, order_email=email)
#         element.save()
#         return render(request, 'portfolio/thanks.html', {'name': name})
#     else:
#         return render(request, 'portfolio/thanks.html')


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    return render(request, 'portfolio/contact.html')
