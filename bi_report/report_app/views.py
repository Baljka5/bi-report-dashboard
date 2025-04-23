from django.shortcuts import render
from .models import Menu

def dashboard_view(request):
    menus = Menu.objects.all()
    return render(request, 'report_app/dashboard.html', {'menus': menus})
