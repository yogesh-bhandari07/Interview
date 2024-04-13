
from django.contrib import admin
from django.urls import path,include
from management.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('management.urls')),
    path('',home),
]
