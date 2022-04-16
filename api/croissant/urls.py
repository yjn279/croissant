from django.urls import path
from croissant import views


urlpatterns = [
    path('/', views.LayersView.as_view()),
    path('layers/', views.LayersView.as_view()),
    path('layers/<int:pk>/', views.LayerView.as_view()),
    path('layers/<int:pk>/children/', views.ChildrenView.as_view()),
]
