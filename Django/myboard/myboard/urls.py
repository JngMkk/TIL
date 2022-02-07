from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('insertform/', views.insert_form, name='insertform'),
    path('insertres/', views.insert_res),
    path('detail/<int:id>', views.detail, name='detail'),
    path('updateform/<int:id>', views.update_form, name='updateform'),
    path('updateres/', views.update_res),
    path('delete/<int:id>', views.delete)
]
