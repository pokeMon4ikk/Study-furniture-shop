from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class ProductsItem(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(ProductsItem, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_description = models.CharField(verbose_name='Краткое описание продукта', max_length=80, blank=True)
    full_description = models.TextField(verbose_name='Полное описание товара', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, default=0)
    sale = models.PositiveIntegerField(verbose_name='Скидка', default=0, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='активна', default=True)
    info_items = models.TextField(verbose_name='Общие параметры', blank=True)

    def __str__(self):
        return f'{self.name}({self.category.name})'

    @staticmethod
    def get_items():
        return Products.objects.filter(is_active=True).order_by('category', 'name')


@receiver(pre_save, sender=ProductsItem)
def update_is_active_on_products(sender, update_fields, instance, **kwargs):
    if update_fields not in ['is_active']:
        return

    if instance.pk:
        if instance.is_active:
            instance.product_set.update(is_active=True)
        else:
            instance.product_set.update(is_active=False)

