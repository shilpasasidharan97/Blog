from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login_view"),
    path('logout-view/', views.logout_view, name="logout_view"),
    path('register/', views.register_view, name="register_view"),
    path('add-blog/',views.add_blog, name='add_blog'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('category/', views.category, name='category')
]