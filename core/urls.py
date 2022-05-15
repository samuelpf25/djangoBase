from django.urls import path

from .views import IndexView #, IndexFormView

urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    #path('contato/',IndexFormView,name = 'contato'),
]