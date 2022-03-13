from django.urls import path
from croissant import views

urlpatterns = [
    path('layers/', views.layers_list),
    path('layers/<int:pk>/', views.layer_detail),
]
