from django.db import models
import uuid


class TrackingNumber(models.Model):
    tracking_number = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    origin_country_id = models.CharField(max_length=2)
    destination_country_id = models.CharField(max_length=2)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    customer_id = models.UUIDField(default=uuid.uuid4)
    customer_name = models.CharField(max_length=255)
    customer_slug = models.CharField(max_length=255)

    def __str__(self):
        return self.tracking_number
