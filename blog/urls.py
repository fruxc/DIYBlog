from . import views
from django.urls import path

urlpatterns = [
    path('blog/blogs', views.PostList.as_view(), name='blogs'),
    path('blog/', views.Index, name='home'),
    path('', views.Index, name='home'),
    path('blog/<int:pk>', views.PostDetail.as_view(), name='post_detail')
]
