from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    # path('login/', views.login_user, name='login'), #also can make separate page for it
    path('logout/', views.logout_user, name='logout'), 
    path('register/', views.register_user, name='register'), 
]
