from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name="index"),
    path('user',views.userdata,name="user"),
    path('login',views.login_user,name="login"), 
    path('logout',views.logout_user,name="logout"), 
    path('home',views.Home,name="home"), 
    path('register/',views.Register,name="register"), 
    path('manage/',views.Manage,name="manage"),
    path('patient/',views.Patient,name="patient"),
    path('datauser',views.data_user,name="datauser"),
    path('docter',views.Docter,name="docter"),
    path('appointed',views.Appointed,name="appointed"),

]