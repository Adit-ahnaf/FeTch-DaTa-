from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dataview.as_view()),
    path('<int:pk>/', views.Datadetailview.as_view()),
]