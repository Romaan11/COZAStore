from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Product

class HomeView(ListView):
    model = Product
    template_name = "store/home.html"
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_categories'] = Category.objects.filter(is_featured=True)
        context['all_categories'] = Category.objects.all()
        return context

class CategoryListView(ListView):
    model = Category
    template_name = "store/category_list.html"
    context_object_name = 'categories'

class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category_id=category_id)

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = 'product'
