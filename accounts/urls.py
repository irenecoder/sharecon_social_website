from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('',views.user_login,name="user-login"),

]
