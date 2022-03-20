from django.urls import path
from croissant import views


urlpatterns = [
    path('layers/', views.LayersView.as_view()),
    path('layers/<int:pk>/', views.LayerView.as_view()),
]
