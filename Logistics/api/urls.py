from django.urls import path
from .views import *

urlpatterns = [
    path('warehouses/', WarehouseGenericView.as_view()),
    path('warehouses/<int:pk>/', WarehouseByOne.as_view()),
    path('warehouses/<int:pk>/update/', WarehouseUpdateView.as_view()),
    path('products/', ProductGenericView.as_view()),
    path('products/<int:pk>/', ProductByOne.as_view()),
    path('products/<int:pk>/update/', ProductUpdateView.as_view()),
    path('inventories/', InventoryGenericView.as_view()),
    path('inventories/<int:pk>/', InventoryByOne.as_view()),
    path('inventories/<int:pk>/update/', InventoryUpdateView.as_view()),
    path('inventories/by-warehouse/', InventoryByWarehouseView.as_view()),
    path('shipments/', ShipmentGenericView.as_view()),
    path('shipments/<int:pk>/', ShipmentByOne.as_view()),
    path('shipments/<int:pk>/update/', ShipmentUpdateView.as_view()),
    path('shipments/<int:pk>/mark-delivered/', MarkShipmentDeliveredView.as_view()),
    path('pricing/', PricingView.as_view()),
    path('optimize-routes/', OptimizeRoutesView.as_view()),
    path('assign-driver/', AssignDriverView.as_view()),
    path('drivers/', DriverGenericView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
]