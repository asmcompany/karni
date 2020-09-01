from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product


class ProdutList(ListView):
    template_name = "product.html"
    paginate_by = 6

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProdutList, self).get_context_data(*args, **kwargs)
        context['brand'] = 'products brand'
        print(context)
        return context

    def get_queryset(self):
        return Product.objects.all()



