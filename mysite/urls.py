"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from restaurant_menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant_menu.urls')),
    # Example of not using include, I simply hardcoded, that for this project, homepage will be views.MenuListView.as_view()
    # If I had path('whatever', include('restaurant_menu.urls')), urls from app restaurant menu would look like localhost/whatever/about itd
    # This would be ok if I had one app.
    # path('', views.MenuListView.as_view(), name='home')

]
