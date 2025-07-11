from rest_framework import serializers
from .models import *
import uuid



class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
        read_only_fields = ['tracking_id']

    def create(self, validated_data):
        sender = validated_data.get('sender_address', '')
        receiver = validated_data.get('receiver_address', '')
        base_cost = 100
        distance_factor = abs(len(sender) - len(receiver))
        validated_data['cost'] = base_cost + distance_factor
        tracking_id = uuid.uuid4().hex[:12].upper()
        validated_data['tracking_id'] = tracking_id
        return super().create(validated_data)     
    
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class ShipmentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentHistory
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)
    history = ShipmentHistorySerializer(many=True, read_only=True)
    class Meta:
        model = Shipment
        fields = '__all__'
        read_only_fields = ['tracking_id', 'history']