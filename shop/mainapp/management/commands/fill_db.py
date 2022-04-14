from django.core.management.base import BaseCommand
from mainapp.models import ProductsItem, Products
from django.contrib.auth.models import User
import json, os

from authapp.models import ShopUser

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='UTF-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):

        categories = load_from_json('productsItems')
        ProductsItem.objects.all().delete()
        for category in categories:
            new_category = ProductsItem(**category)
            new_category.save()

        products = load_from_json('products')
        Products.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductsItem.objects.get(name=category_name)
            product['category'] = _category
            new_product = Products(**product)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('Admin', "Admin@bk.ru", '13583', age=23)
