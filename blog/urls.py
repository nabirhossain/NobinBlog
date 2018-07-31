from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('author/<name>',views.getAuthor,name='author'),
    path('detail/<int:id>',views.PostDetail, name='post_detail'),
    path('category/<name>',views.PostTopic, name='category'),
    path('login',views.LogIn, name='login'),
    path('logout',views.LogOut, name='logout'),
]