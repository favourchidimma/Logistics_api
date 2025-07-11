from django.db import models

# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    restock_level = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} in {self.warehouse.name}"

class Shipment(models.Model):
    tracking_id = models.CharField(max_length=100, unique=True)
    sender_address = models.CharField(max_length=200)
    receiver_address = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    current_location = models.CharField(max_length=200)
    estimated_delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True, blank=True)
    sender_phone = models.CharField(max_length=15, null=True, blank=True)
    delivery_window = models.CharField(max_length=100, null=True, blank=True)
    receiver_phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"Shipment {self.tracking_id} from {self.sender_addres} to {self.receiver_address}"
    
class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ShipmentHistory(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="history")
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for {self.shipment.tracking_id} at {self.timestamp}"
