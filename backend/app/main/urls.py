from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drf import views as drf_views
from todo import views 

router = routers.DefaultRouter()
router.register('users', drf_views.user_viewset )
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),

]