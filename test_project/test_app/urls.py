from django.urls import path
from test_app import views

urlpatterns = [
    path('', views.SearchView.as_view()),
]