from django.urls import path
from . import views

#앱 사용에 필요한 기능 url
urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
    path('index/', views.index),
    #int형식의 post_id를 받아오겠다.
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/delete/', views.delete),
    path('<int:post_id>/edit/', views.edit),
    path('<int:post_id>/update/', views.update),
]