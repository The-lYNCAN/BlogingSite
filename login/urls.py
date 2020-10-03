from django.contrib.auth.decorators import login_required
from django.urls import path
from login import views

app_name = "login"
urlpatterns = [
    path('/index',views.Index_view.as_view(),name='index'),
    path('/signup',views.signup_view.as_view(),name='signup'),
    path('/login',views.login_view.as_view(),name='logins'),
    path('/cblog', login_required(views.Blog_creation.as_view()),name='blogc'),
    path('/list',login_required(views.listing_blogs.as_view()),name='list'),
    path('/detail<pk>',login_required(views.complete_blog.as_view()),name='blog_complete'),
    path('/update<pk>', login_required(views.update_blog.as_view()),name='update'),
    path('/logout', login_required(views.loggout_view.as_view()),name='logout'),
]