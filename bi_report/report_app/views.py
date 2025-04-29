from django.shortcuts import render, get_object_or_404
from .models import News, Category


def dashboard_view(request):
    categories = Category.objects.prefetch_related('links').all()
    news_items = News.objects.order_by('-published_at')[:5]

    return render(request, 'report_app/dashboard.html', {
        'categories': categories,
        'news_items': news_items,
        'active_menu': 'home',
    })


def docs_view(request):
    categories = Category.objects.prefetch_related('links').all()

    return render(request, 'report_app/docs.html', {
        'categories': categories,
        'active_menu': 'docs',
    })


def news_view(request):
    news_items = News.objects.order_by('-published_at')

    return render(request, 'report_app/news.html', {
        'news_items': news_items,
        'active_menu': 'news',
    })
