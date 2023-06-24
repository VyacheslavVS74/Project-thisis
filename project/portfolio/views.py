from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContactForm
from .models import Works
from .utils import search_works, paginate_works
from crm.models import Order
from crm.forms import OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError


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
    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = OrderForm(request.POST or None, initial={'order_works': order_works})
        if form.is_valid():
            order = form.save(commit=False)
            order.sender = sender
            order.order_works = order_works

            if sender:
                order.order_name = sender.first_name
                order.order_email = sender.email
            order.save()
            messages.success(request, 'Заявка отправлена')
            return redirect('work-main', pk=order_works.id)


        # if request.user.is_authenticated:
        #     if form.is_valid():
        #         form.order_name = request.user.first_name
        #         form.order_email = request.user.email
        #         form.save()
        #         messages.success(request, 'Заявка отправлена')
        #         return redirect('work-main', pk=order_works.id)
        # else:
        #     if form.is_valid():
        #         form.save()
        #         messages.success(request, 'Заявка отправлена')
        #         return redirect('work-main', pk=order_works.id)
    context = {
        'order_works': order_works,
        'form': form,
    }
    return render(request, 'portfolio/work_main.html', context)


# def thanks_page(request):
#
#     work_name = Works.objects.first()
#     if request.method == 'POST':
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.user['email']
#         order_work = Works.title
#         element = Order(order_work=work_name, order_name=name, order_phone=phone, order_email=email)
#         element.save()
#         return render(request, 'portfolio/thanks.html', {'name': name})
#     else:
#         return render(request, 'portfolio/thanks.html')


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            subject = 'Message'
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'content': form.cleaned_data['content']
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, form.cleaned_data['email'], ['vsitkov99@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)
