#Django
from django.urls import path
#from django.views.generic import TemplateView

#View
from users import views

urlpatterns = [

    #Managament
    path(
        route = 'login/', 
        view = views.LoginView.as_view(), 
        name ='login'
    ), 
    path(
        route = 'logout/',
        view =  views.LogoutView.as_view(), 
        name ='logout'
    ),
    path(
        route = 'signup/',
        view =  views.SignupView.as_view(), 
        name='signup'
    ),
    path(
        route = 'me/profile/',
        view =  views.UpdateProfileView.as_view(), 
        name ='update'
    ),

    #Posts
    path(
        route = '<str:username>',
        view = views.UserDetailView.as_view(template_name='users/detail.html'),
        name = 'detail'
    ),
]