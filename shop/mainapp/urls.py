from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='main'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>/page/<int:page>', mainapp.products, name='page'),
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('product/<int:pk>/price/', mainapp.product_price, name='product_price')
]


