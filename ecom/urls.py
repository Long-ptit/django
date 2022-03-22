"""ecom URL Configuration

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
from django.contrib import admin
from django.urls import path

from home import views as home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.get_home),
    path('homeadmin/', home.get_home_admin),

    path('add_book_form/', home.add_book_form),
    path('add_book', home.add_book),
    path('edit_book/<int:id>/', home.edit_book_form),
    path('edit_book', home.edit_book),
    path('delete_book/<int:id>/', home.delete_book),

    path('add_shoes_form/', home.add_shoes_form),
    path('add_shoes', home.add_shoes),
    path('edit_shoes/<int:id>/', home.edit_shoes_form),
    path('edit_shoes', home.edit_shoes),
    path('delete_shoes/<int:id>/', home.delete_shoes),

    path('add_laptop_form/', home.add_laptop_form),
    path('add_laptop', home.add_laptop),
    path('edit_laptop/<int:id>/', home.edit_laptop_form),
    path('edit_laptop', home.edit_laptop),
    path('delete_laptop/<int:id>/', home.delete_laptop),

    path('add_clothes_form/', home.add_clothes_form),
    path('add_clothes', home.add_clothes),
    path('edit_clothes/<int:id>/', home.edit_clothes_form),
    path('edit_clothes', home.edit_clothes),
    path('delete_clothes/<int:id>/', home.delete_clothes),

    path('add_phone_form/', home.add_phone_form),
    path('add_phone', home.add_phone),
    path('edit_phone/<int:id>/', home.edit_phone_form),
    path('edit_phone', home.edit_phone),
    path('delete_phone/<int:id>/', home.delete_phone),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
