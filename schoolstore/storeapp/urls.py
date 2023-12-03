
from django.urls import path
from . import views

app_name='storeapp'
urlpatterns = [

    path('',views.home,name="home" ),
    path('login.html',views.login,name="login" ),
    path('register.html',views.register,name="register" ),
    path('new.html',views.new,name="new" ),
    path('form.html',views.form,name="form"),
    path('sucess.html',views.sucess,name="sucess"),
    path('logout.html',views.logout,name="logout")
]