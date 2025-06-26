from django.urls import path
from diplom_spo import views

app_name = 'diplom_spo'

urlpatterns = [
    path('diplom_detail', views.diploma_list, name='diplom_detail'),
    path('edit/<int:pk>/', views.diploma_edit, name='diploma_edit'),
]
