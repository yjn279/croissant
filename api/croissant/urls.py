from django.urls import path
from croissant import views


# LIST_METHODS = {
#     'get': 'list',
#     'post': 'create',
# }

# ITEM_METHODS = {
#     'get': 'retrieve',
#     'put': 'update',
#     # 'patch': 'partial_update',
#     'delete': 'destroy',
# }


urlpatterns = [
    path('layers/', views.LayersView.as_view()),
    path('layers/<int:pk>/', views.LayerView.as_view()),
]
