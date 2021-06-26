from django.urls import path
from book_outlet import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:_id>/', views.book_detail, name='book_detail')
]