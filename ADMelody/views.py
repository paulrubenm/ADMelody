from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from products.models import Product
from blog.models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


def home(request):
    return render(request, 'index-en.html')


def aboutus(request):
    return render(request, 'aboutus-en.html')


def services(request):
    return render(request, 'services-en.html')


def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, 'products-en.html', {'products': products, 'items': items, 'page_range': page_range, })


def contact(request):
    if request.method == "POST":
        name_of_person = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        Subject = request.POST['Subject']
        textarea = request.POST['textarea']
        call_info = "[Website Contact]" + " " + name_of_person
        message_body = "Message:" + textarea + "\n" + "\n" + "Email:" + " " + email + "\n" + "\n" + \
            "Name:" + name_of_person + "\n" + "\n" + "Phone Number:" + \
            phone + "\n" + "\n" + "Subject:" + Subject
        send_mail(
            call_info,  # subject
            message_body,  # message
            email,  # from email
            ['anhduongbeauty.2009@gmail.com'],  # to email
        )

        return render(request, 'contact-en.html', {'name_of_person': name_of_person})
    else:
        return render(request, 'contact-en.html', {})


def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page', 1)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, 'allblogs-en.html', {'blogs': blogs, 'items': items, 'page_range': page_range, })


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail-en.html', {'blog': detailblog})


def homevn(request):
    return render(request, 'index-vn.html')


def aboutusvn(request):
    return render(request, 'aboutus-vn.html')


def servicesvn(request):
    return render(request, 'services-vn.html')


def contactvn(request):
    if request.method == "POST":
        name_of_person = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        Subject = request.POST['Subject']
        textarea = request.POST['textarea']
        call_info = "[Website Contact]" + " " + name_of_person
        message_body = "Message:" + textarea + "\n" + "\n" + "Email:" + " " + email + "\n" + "\n" + \
            "Name:" + name_of_person + "\n" + "\n" + "Phone Number:" + \
            phone + "\n" + "\n" + "Subject:" + Subject
        send_mail(
            call_info,  # subject
            message_body,  # message
            email,  # from email
            ['anhduongbeauty.2009@gmail.com'],  # to email
        )

        return render(request, 'contact-vn.html', {'name_of_person': name_of_person})
    else:
        return render(request, 'contact-vn.html', {})


def productsvn(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, 'products-vn.html', {'products': products, 'items': items, 'page_range': page_range, })


def blogvn(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page', 1)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return render(request, 'allblogs-vn.html', {'blogs': blogs, 'items': items, 'page_range': page_range, })


def detailvn(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail-vn.html', {'blog': detailblog})
