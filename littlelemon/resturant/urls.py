from django.urls import path
from resturant import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path('booking/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]