from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    # path('user/profile/<int:pk>/', views.UserProfileView.as_view(), name='user_profile'),

    # path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UserUpdateView.as_view(), name='update'),
    # path('follow/', views.FollowView.as_view(), name='follow'),
    # path('follow/<int:pk>/<int:id>/', views.AddFollowerView, name="add_follower"),

]