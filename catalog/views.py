from django.shortcuts import render

from .models import Category, Product, Tag

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(description__icontains=search_query)
    
    # Category filter
    selected_categories = request.GET.getlist('categories')
    if selected_categories:
        products = products.filter(category__id__in=selected_categories)
    
    # Tags filter (AND logic for multiple tags)
    tag_filters = request.GET.getlist('tags')
    if tag_filters:
        products = products.filter(tags__id__in=tag_filters)
    
    context = {
        'products': products,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'selected_categories': [int(c) for c in selected_categories],
        'selected_tags': [int(t) for t in tag_filters],
        'search_query': search_query,
    }
    return render(request, 'catalog/product_list.html', context)