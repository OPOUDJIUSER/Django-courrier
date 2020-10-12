from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView
from . import views

urlpatterns=[
    path('', views.indexView, name='index'),
    path('login/administration/',views.administrationView, name='administration'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', views.registerView.as_view(), name='register'),
    path('passwordreset/', views.passwordresetView.as_view(), name='passwordreset'),
    path('passwordchange/', views.setpasswordView, name='passwordchange'),
    path('administration/', views.administrationView, name='administration'),
    path('login/administration/user_create', views.administrationuser_createView.as_view(), name='administrationuser_create'),
    path('login/administration/user_update/<int:pk>', views.administrationuser_updateView.as_view(), name='administrationuser_update'),
    path('login/administration/user_delete/<int:pk>', views.administrationuser_deleteView.as_view(), name='administrationuser_delete'),
    path('login/administration/user_list', views.administrationuser_listView.as_view(), name='administrationuser_list'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    url(r'^courriers/$', views.book_list, name='book_list'),
    path('courriers/search/$', views.searchView, name='book_list_search'),
    url(r'^courriers/create$', views.book_create, name='book_create'),
    url(r'^courriers/(?P<id>\d+)/update$', views.book_update, name='book_update'),
    url(r'^courriers/(?P<id>\d+)/delete$', views.book_delete, name='book_delete'),


]