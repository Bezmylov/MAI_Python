from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler400
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


handler404 = 'courses.views.error_404'
handler400 = 'courses.views.error_400'