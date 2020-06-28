from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<str:id>', views.DetailView.as_view(), name='detail'),
]
