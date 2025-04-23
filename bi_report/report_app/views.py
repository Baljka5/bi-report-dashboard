from django.shortcuts import render, get_object_or_404
from .models import Menu, News, Category


def dashboard_view(request):
    menus = Menu.objects.all()
    news_items = News.objects.order_by('-published_at')[:5]
    categories = Category.objects.prefetch_related('links').all()

    return render(request, 'report_app/dashboard.html', {
        'menus': menus,
        'news_items': news_items,
        'categories': categories,
    })


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'report_app/category_details.html', {
        'category': category,
        'links': category.links.all()
    })
