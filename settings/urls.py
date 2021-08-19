"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.api.viewsets import ProductViewset, CategoryViewset, SubCategoryViewset
from settings import settings

router_v1 = routers.DefaultRouter()

router_v1.register('products', ProductViewset)
router_v1.register('categories', CategoryViewset)
router_v1.register('subcategories', SubCategoryViewset)

urlpatterns = [
    path('v1/', include('rest_framework.urls')),
    path('v1/', include(router_v1.urls)),
    path('', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
