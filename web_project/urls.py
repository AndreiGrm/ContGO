from django.urls import path
from .views import example_api
from django.contrib import admin

urlpatterns = [
    path('api/example/', example_api),
     path('admin/', admin.site.urls),
]
