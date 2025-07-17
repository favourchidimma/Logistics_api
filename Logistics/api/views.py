from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from .serializers import *
import uuid
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class WarehouseGenericView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new warehouse",
        request_body=WarehouseSerializer,
        responses={
            201: WarehouseSerializer,
            400: "Bad Request",
        }
    )
    def post(self, request):
        serializer = WarehouseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        warehouse = Warehouse.objects.create(**serializer.validated_data)
        return Response(WarehouseSerializer(warehouse).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        warehouses = Warehouse.objects.all()
        return Response(WarehouseSerializer(warehouses, many=True).data, status=status.HTTP_200_OK)

class WarehouseByOne(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            warehouse = Warehouse.objects.get(pk=pk)
        except Warehouse.DoesNotExist:
            return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(WarehouseSerializer(warehouse).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            warehouse = Warehouse.objects.get(pk=pk)
        except Warehouse.DoesNotExist:
            return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)
        warehouse.delete()
        return Response({"message": "Warehouse deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class WarehouseUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Update a warehouse",
        request_body=WarehouseSerializer,
        responses={200: WarehouseSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        try:
            warehouse = Warehouse.objects.get(pk=pk)
        except Warehouse.DoesNotExist:
            return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WarehouseSerializer(warehouse, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductGenericView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={
            201: ProductSerializer,
            400: "Bad Request",
        }
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = Product.objects.create(**serializer.validated_data)
        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)

class ProductByOne(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class ProductUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Update a product",
        request_body=ProductSerializer,
        responses={200: ProductSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class InventoryGenericView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new inventory record",
        request_body=InventorySerializer,
        responses={
            201: InventorySerializer,
            400: "Bad Request",
        }
    )
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inventory = Inventory.objects.create(**serializer.validated_data)
        return Response(InventorySerializer(inventory).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        inventories = Inventory.objects.all()
        return Response(InventorySerializer(inventories, many=True).data, status=status.HTTP_200_OK)

class InventoryByOne(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(InventorySerializer(inventory).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
        inventory.delete()
        return Response({"message": "Inventory deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class InventoryUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Update an inventory record",
        request_body=InventorySerializer,
        responses={200: InventorySerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            return Response({"error": "Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InventorySerializer(inventory, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class InventoryByWarehouseView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('warehouse_id', openapi.IN_QUERY, description="Warehouse ID", type=openapi.TYPE_INTEGER, required=True)
        ],
        operation_description="List inventory for a specific warehouse"
    )
    def get(self, request):
        warehouse_id = request.GET.get('warehouse_id')
        if not warehouse_id:
            return Response({"error": "warehouse_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        inventories = Inventory.objects.filter(warehouse_id=warehouse_id)
        return Response(InventorySerializer(inventories, many=True).data, status=status.HTTP_200_OK)

class ShipmentGenericView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new shipment",
        request_body=ShipmentSerializer,
        responses={
            201: ShipmentSerializer,
            400: "Bad Request",
        }
    )
    def post(self, request):
        serializer = ShipmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        validated_data['tracking_id'] = str(uuid.uuid4()).replace('-', '')[:12].upper()
        shipment = Shipment.objects.create(**validated_data)
        return Response(ShipmentSerializer(shipment).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        shipments = Shipment.objects.all()
        return Response(ShipmentSerializer(shipments, many=True).data, status=status.HTTP_200_OK)

class ShipmentByOne(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            shipment = Shipment.objects.get(pk=pk)
        except Shipment.DoesNotExist:
            return Response({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(ShipmentSerializer(shipment).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            shipment = Shipment.objects.get(pk=pk)
        except Shipment.DoesNotExist:
            return Response({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
        shipment.delete()
        return Response({"message": "Shipment deleted"}, status=status.HTTP_204_NO_CONTENT)
class ShipmentUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Update a shipment",
        request_body=ShipmentSerializer,
        responses={200: ShipmentSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        try:
            shipment = Shipment.objects.get(pk=pk)
        except Shipment.DoesNotExist:
            return Response({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShipmentSerializer(shipment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MarkShipmentDeliveredView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Mark a shipment as delivered"
    )
    def post(self, request, pk):
        try:
            shipment = Shipment.objects.get(pk=pk)
        except Shipment.DoesNotExist:
            return Response({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)
        shipment.status = "Delivered"
        shipment.save()
        return Response({"message": "Shipment marked as delivered"}, status=status.HTTP_200_OK)


class PricingView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('origin_zip', openapi.IN_QUERY, description="Origin ZIP", type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('destination_zip', openapi.IN_QUERY, description="Destination ZIP", type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('weight', openapi.IN_QUERY, description="Weight in kg", type=openapi.TYPE_NUMBER, required=True),
            openapi.Parameter('service_level', openapi.IN_QUERY, description="Service level (standard or express)", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        origin = request.GET.get('origin_zip')
        destination = request.GET.get('destination_zip')
        weight = float(request.GET.get('weight', 0))
        service_level = request.GET.get('service_level', 'standard')

        base = 1000
        weight_fee = weight * 50
        multiplier = 1.5 if service_level == 'express' else 1

        estimated_cost = (base + weight_fee) * multiplier

        return Response({"estimated_cost": estimated_cost}, status=status.HTTP_200_OK)
    
class OptimizeRoutesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(
        operation_description="Optimize delivery routes",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'addresses': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_STRING)
                ),
                'time_constraints': openapi.Schema(type=openapi.TYPE_OBJECT)
            },
            required=['addresses']
        )
    )
    def post(self, request):
        addresses = request.data.get('addresses', [])
        optimized_route = sorted(addresses)

        return Response({
            "optimized_route": optimized_route,
            "estimated_time": f"{len(addresses)*15} minutes",
            "total_distance": f"{len(addresses)*5} km"
        }, status=status.HTTP_200_OK)

class DriverGenericView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new driver",
        request_body=DriverSerializer,
        responses={
            201: DriverSerializer,
            400: "Bad Request",
        }
    )
    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        driver = serializer.save()
        return Response(DriverSerializer(driver).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        drivers = Driver.objects.all()
        return Response(DriverSerializer(drivers, many=True).data, status=status.HTTP_200_OK)
    
class DriverDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(DriverSerializer(driver).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)
        driver.delete()
        return Response({"message": "Driver deleted"}, status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_description="Update a driver",
        request_body=DriverSerializer
    )
    def put(self, request, pk):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DriverSerializer(driver, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class AssignDriverView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(
        operation_description="Assign a driver to a shipment",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["shipment_id", "driver_id", "delivery_window"],
            properties={
                "shipment_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "driver_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "delivery_window": openapi.Schema(type=openapi.TYPE_STRING)
            }
        )
    )
    def post(self, request):
        shipment_id = request.data.get("shipment_id")
        driver_id = request.data.get("driver_id")
        delivery_window = request.data.get("delivery_window")

        try:
            shipment = Shipment.objects.get(id=shipment_id)
        except Shipment.DoesNotExist:
            return Response({"error": "Shipment not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            driver = Driver.objects.get(id=driver_id)
        except Driver.DoesNotExist:
            return Response({"error": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)

        shipment.driver = driver
        shipment.delivery_window = delivery_window
        shipment.save()

        return Response({
            "message": "Driver assigned",
            "driver": {
                "name": driver.name,
                "phone": driver.phone,
                "start_time": delivery_window
            }
        }, status=status.HTTP_200_OK)