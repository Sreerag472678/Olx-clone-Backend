from django.urls import path
from .views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import Logout_user,UserInfoView,Register

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', Logout_user, name='auth_logout'),
    path('register/', Register.as_view(), name='register'),
    path('user-info/', UserInfoView.as_view(), name='user_info'),
    
]
