"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from stock import views

# from stock.views import views_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    url(r'imp/$', views.views_item_imp, name='imp'),
    url(r'imp/ssd', views.render_ssd_person, name='imp_ssd'),
    url(r'imp/hdd', views.render_hdd_person, name='imp_hdd'),
    url(r'cs/$', views.views_item_cs, name='cs'),
    url(r'dev/$', views.views_item_dev, name='dev'),
    url(r'schedule/$', views.views_schedule, name='schedule'),
    url(r'contoh', views.render_contoh, name="contoh")
]
