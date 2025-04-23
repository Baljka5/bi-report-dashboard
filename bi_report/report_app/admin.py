from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Menu, News, Link, Category


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    ordering = ('-published_at',)

class LinkInline(admin.TabularInline):
    model = Link
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [LinkInline]

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    list_filter = ('category',)