from django.urls import path
from django.views.generic import  TemplateView
from . import views
from django.contrib.auth import views as auth_views
app_name = 'polls'
urlpatterns = [
    path('detail/<int:question_id>/', views.detailView, name = 'detail'),
    path('list/', views.viewlist, name='view_list'),
    path('', views.index, name = 'index'),
    path('<int:question_id>', views.vote, name="vote"),
    path('register/', views.register, name = 'register'),
    #path('register/',views.register.as_view(template_name="polls/register.html"), name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="polls/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]