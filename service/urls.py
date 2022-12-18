from django.urls import path,include
from service import views #as auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('register', views.RegisterForm.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name = 'logout'),
    path('', views.PostViews.as_view(), name = 'index'),
    path('post/<int:pk>', views.DetailPostView.as_view(), name = 'detail_post'),
    #path('create_post', views.CreatePostView.as_view(), name = 'create_post'),
    path('create_post', views.create_post, name = 'create_post'),
    path('update_post/<int:pk>', views.UpdatePostView.as_view(), name = 'update_post'),
    path('delete_post/<int:pk>', views.DeletePostView.as_view(), name = 'delete_post'),
    path('post/<int:pk>/add_comment', views.AddCommentPostView.as_view(), name = 'add_comment'),
    path('about', views.about, name = 'about'),
    path('upload', views.upload, name = 'upload'),
    path('download', views.download, name = 'download'),
    
]