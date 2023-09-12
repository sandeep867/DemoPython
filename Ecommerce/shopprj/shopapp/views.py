from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Category, Product


# Create your views here.


def AllProductCat(request, c_slug=None):
    c_page = None
    product_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        product_list = Product.objects.all().filter(available=True)
    paginator = Paginator(product_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (InvalidPage, EmptyPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'products': products})


def Prodetails(request, c_slug, product_slug):
    try:
        products = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'products': products})
