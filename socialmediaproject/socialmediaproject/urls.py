"""socialmediaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialmediaapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_list, name='post_list'),
    path('post_list',views.post_list, name='post_list'),
    path('<id>/<slug>',views.post_detail, name='post_detail'),
    path('post_create', views.post_create, name='post_create'),
    path('login', views.user_login, name = 'user_login'),
    path('logout', views.user_logout, name = 'user_logout'),
    path('register',views.user_register, name='user_register'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('like_post', views.like_post, name='like_post'),
    path('<id>/post_edit',views.post_edit, name='post_edit'),
    path('<id>/post_delete',views.post_delete, name='post_delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
