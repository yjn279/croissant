from django.urls import path
from croissant import views

urlpatterns = [
    path('layers/', views.Layers.as_view()),
    path('layers/<int:pk>/', views.Layer.as_view()),
]
