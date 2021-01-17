from django.urls import path
from . import views

app_name = 'sdgs'


urlpatterns = [
    path('postdetail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # # path('user/profile/<int:pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('post/new/', views.post, name='post_create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post_update'),
    path('postlist/', views.PostListView.as_view(), name='post_list'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),

    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('create/', views.UserCreateView.as_view(), name='create'),
    # path('update/<int:pk>', views.UserUpdateView.as_view(), name='update'),
    # # path('follow/', views.FollowView.as_view(), name='follow'),
    # path('follow/<int:pk>/<int:id>/', views.AddFollowerView, name="add_follower"),

]