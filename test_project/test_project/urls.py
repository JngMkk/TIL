from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather_app.urls')),
    path('plants/', include('test_app.urls')),
    # path('search/', include('test_app.urls')),
]
