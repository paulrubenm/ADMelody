"""ADMelody URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import ADMelody.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('en/', views.home, name='home'),
    path('en/aboutus/', views.aboutus, name='aboutus'),
    path('en/services/', views.services, name='services'),
    path('en/products/', views.products, name='products'),
    path('en/contact/', views.contact, name='contact'),
    path('en/blog/', views.blog, name='blog'),
    path('en/blog/<int:blog_id>/', views.detail, name="detail"),

    path('', views.homevn, name='homevn'),
    path('aboutus/', views.aboutusvn, name='aboutusvn'),
    path('services/', views.servicesvn, name='servicesvn'),
    path('contact/', views.contactvn, name='contactvn'),
    path('products/', views.productsvn, name='productsvn'),
    path('blog/', views.blogvn, name='blogvn'),
    path('blog/<int:blog_id>/', views.detailvn, name="detailvn"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
