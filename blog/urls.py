from . import views
from django.urls import path

urlpatterns = [
    path('blog/blogs', views.PostList.as_view(), name='blogs'),
    path('blog/', views.index, name='home'),
    path('', views.index, name='home'),
    # path('blog/<int:pk>', views.PostDetail.as_view(), name='post_detail')
    path('blog/<int:id>', views.post_detail, name='post_detail'),
    path('accounts/register', views.register, name='register'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logoutUser, name='logout'),
    path('blog/blogger/<slug:author>', views.blogger, name='blogger'),
]
