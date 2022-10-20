from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


app_name='accounts'
urlpatterns = [
    # path('',views.user_login,name="user-login"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    # path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

    path('dashboard/',views.dashboard,name="dashboard"),
    path('',include('django.contrib.auth.urls')),
    path('register/',views.user_registration,name="user_registration"),
    

]
