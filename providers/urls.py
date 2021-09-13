from django.urls import path
from . import views

# Using <int:...> and <str:...> so that information can be passed from the url to views.py #
urlpatterns = [
    path('', views.fullProvidersList),
    path('<int:npix>/', views.indProviderPage),
    path('<str:orderedWord>/', views.reorderedProvidersList),
]