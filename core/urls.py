from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('find', views.FindView.as_view(), name='find'),
]
