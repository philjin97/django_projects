from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:number>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:number>/delete/', views.delete, name='delete'),
    path('<int:number>/edit/', views.edit, name='edit'),
    path('<int:number>/update/', views.update, name='update'),
]