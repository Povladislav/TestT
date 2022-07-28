from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base_page, name='main_page'),
    path('input_page/', views.input_page, name='input_page'),
    path('output_page/', views.output_page, name='output_page'),
]
