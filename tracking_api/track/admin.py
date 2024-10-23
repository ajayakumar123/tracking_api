from django.contrib import admin
from .models import TrackingNumber
# Register your models here.


class AdminTrackingNumber(admin.ModelAdmin):
    list_display = (
                'tracking_number',
                'created_at',
                'origin_country_id',
                'destination_country_id',
                'weight',
                'customer_id',
                'customer_name',
                'customer_slug'
                  )
    ordering = ('-created_at',)


admin.site.register(TrackingNumber, AdminTrackingNumber)