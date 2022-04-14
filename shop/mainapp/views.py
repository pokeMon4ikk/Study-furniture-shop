# import json
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
import os
from mainapp.models import ProductsItem, Products
from basketapp.models import Basket

module_dir = os.path.dirname(__file__)

# links_menu = [
#     {'href': 'products_all', 'name': 'все'},
#     {'href': 'products_home', 'name': 'дом'},
#     {'href': 'products_office', 'name': 'офис'},
#     {'href': 'products_modern', 'name': 'модерн'},
#     {'href': 'products_classic', 'name': 'классика'},
# ]

main_menu = [
    {'href': 'main', 'name': 'Главная'},
    {'href': 'products:main', 'name': 'Продукты'},
    {'href': 'contact', 'name': 'Контакты'},
]


# Create your views here.

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Products.objects.filter(is_active=True, category__is_active=True)
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Products.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)[:3]
    return same_products


def contact(request,  pk=None):
    # basket = get_basket(request.user)
    content = {
        'title': 'Контакты',
        'main_menu': main_menu,

    }
    return render(request, 'mainapp/contact.html', content)


def products(request, pk=None, page=1):
    # file_path = os.path.join(module_dir, 'json/products.json')
    # products = json.load(open(file_path, encoding='UTF-8'))

    title = 'Продукты'
    links_menu = ProductsItem.objects.filter(is_active=True)

    # basket = get_basket(request.user)
    #
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Products.objects.filter(is_active=True, category__is_active=True).order_by('price')
            category = {'name': 'все', 'pk': 0}
        else:
            category = get_object_or_404(ProductsItem, pk=pk)
            products = Products.objects.filter(category__pk=pk, is_active=True, category__is_active=True)\
                .order_by('price')

        paginator = Paginator(products, 8)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'main_menu': main_menu,
            'links_menu': links_menu,
            'products': products_paginator,
            'category': category,

        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    # same_products = Products.objects.all()[:5]

    content = {
        'title': title,
        'main_menu': main_menu,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', content)


def main(request):
    title = 'Главная'
    products = (
        Products.objects.filter(is_active=True, category__is_active=True).select_related()[:3]
    )
    # basket = get_basket(request.user)
    content = {
        'main_menu': main_menu,
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', content)


def product(request, pk):
    title = 'Страница продукта'
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        'title': title,
        'main_menu': main_menu,
        'links_menu': ProductsItem.objects.all(),
        'product': get_object_or_404(Products, pk=pk),
        'basket': get_basket(request.user),
        'same_products': same_products,
    }

    return render(request, 'mainapp/product.html', content)


def product_price(request, pk):
    product = Products.objects.filter(pk=int(pk)).first()
    if product:
        return JsonResponse({'price': product.price})
    else:
        return JsonResponse({'price': 0})





