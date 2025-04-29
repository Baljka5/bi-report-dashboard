from django.shortcuts import render, get_object_or_404
from .models import News, Category

from django.db.models.functions import TruncMonth
from django.db.models import Count


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
    # Сар бүр мэдээг group-лэж авах
    news_by_month = News.objects.annotate(month=TruncMonth('published_at')).order_by('-month', '-published_at')
    months = {}

    for news in news_by_month:
        month_name = news.published_at.strftime('%Y-%m')
        if month_name not in months:
            months[month_name] = []
        months[month_name].append(news)

    return render(request, 'report_app/news.html', {
        'months': months,
        'active_menu': 'news',
    })


def news_detail_view(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'report_app/news_details.html', {
        'news': news,
        'active_menu': 'news',
    })
