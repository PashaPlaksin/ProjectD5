from django.urls import path
from django.urls import include
from .views import PostList, PostDetail, PostSearch, ChangeNews, AddNews, DeleteNews

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', AddNews.as_view(), name='post_create'),
    path('create/<int:pk>', ChangeNews.as_view(), name='post_update'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='post_delete'),
    path('', PostList.as_view(), name='post'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('user/', PostList.as_view(), name='user_update')

]
