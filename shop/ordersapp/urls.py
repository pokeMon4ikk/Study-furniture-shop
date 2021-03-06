from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'


urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='order_list'),
    path('create', ordersapp.OrderItemCreate.as_view(), name='order_create'),
    path('forming/complete/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),
    path('read/<int:pk>/', ordersapp.OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', ordersapp.OrderDelete.as_view(), name='order_delete'),
]



