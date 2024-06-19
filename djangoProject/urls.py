from django.urls import path
from forum.views import post_list, post_detail, create_post, category_list, category_posts
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('create_post/', create_post, name='create_post'),
    path('categories/', category_list, name='category_list'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('category/<int:category_id>/', category_posts, name='category_posts'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
