from django.urls import path
from . import views

#app_name이라는 네임 스페이스를 사용해준다.
#뜻: app_url.py의 주인은 'board'라는 어플리케이션이다.
app_name = 'board'

#앱 사용에 필요한 기능 url
#name속성: 특정한 URL 매핑을 위한 고유 식별 ID의 개념.
#           이 이름을 매퍼에 반전시킬 수 있으며, 매퍼가 처리하도록 설계된 리소스를
#           향하는 URL을 동적으로 생성하기 위해 설정하는 것임.
urlpatterns = [
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('index/', views.index, name='index'),
    #int형식의 post_id를 받아오겠다.
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete', views.comments_delete, name='comments_delete'),
]