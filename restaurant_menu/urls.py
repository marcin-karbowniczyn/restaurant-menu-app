from django.urls import path
from . import views

# We can add urls for this app here, and then include them inside project urls, or hardcode these urls in project urls

urlpatterns = [
    # First argument -> url, Second argument -> function or class to be triggered when user enters the url,
    # as_view -> it renders the class as actual view. Nie potrzebujemy tego w function-based views, tam używamy funkcji render() wewnątrz funkcji
    path('', views.MenuListView.as_view(), name='home')
]
