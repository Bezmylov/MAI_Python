from django.urls import path
from .views import HomeworkSubmitView, HomeworkReviewView
from .api import CourseViewSet, HomeworkSubmitAPI
from .views import TestCreateView, TestListView, take_test, test_results
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views

# Настроим маршруты для API
router = DefaultRouter()
router.register(r'api/courses', CourseViewSet)

urlpatterns = [
    # Маршруты для работы с домашними заданиями
    path('homeworks/submit/<int:topic_id>/', HomeworkSubmitView.as_view(), name='submit_homework'),
    path('homeworks/review/<int:pk>/', HomeworkReviewView.as_view(), name='review_homework'),

    # API для отправки домашнего задания
    path('api/homework/submit/', HomeworkSubmitAPI.as_view(), name='api_homework_submit'),

    # Регистрация и аутентификация
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Маршруты для тестов
    path('tests/', TestListView.as_view(), name='test_list'),
    path('tests/create/', TestCreateView.as_view(), name='test_create'),
    path('test/<int:test_id>/take/', take_test, name='take_test'),
    path('test/<int:test_id>/results/', test_results, name='test_results'),

    # Включаем маршруты для API
    *router.urls,  # Добавляем маршруты API

]

# Обработка ошибок
handler404 = 'courses.views.error_404'
handler400 = 'courses.views.error_400'
