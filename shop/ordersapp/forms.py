from django import forms
from ordersapp.models import Order, OrderItem
from mainapp.models import Products


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ()

    price = forms.CharField(label='Цена', required=False)
    total_price = forms.CharField(label='Общая цена', required=False)

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'price':
                field.widget.attrs['readonly'] = 'true'
            self.fields['product'].queryset = Products.objects.filter(is_active=True).select_related()

