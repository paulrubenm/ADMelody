from django.shortcuts import render

from .models import Product

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page = request.GET.get('page')

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
    return render(request, 'products.html', {'products': products, 'items': items, 'page_range': page_range, })
