from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index1, name='index1'),
    path('post/', views.home_view, name='indexhome_view2'),
]