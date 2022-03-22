from django.urls import path
from croissant import views


LIST_METHODS = {
    'get': 'list',
    'post': 'create',
}

ITEM_METHODS = {
    'get': 'retrieve',
    'put': 'update',
    # 'patch': 'partial_update',
    'delete': 'destroy',
}


urlpatterns = [
    path('layers/', views.LayersViewSet.as_view(LIST_METHODS)),
    # path('layers/<int:pk>/', views.LayerViewSet.as_view()),
]
