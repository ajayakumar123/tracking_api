# tracking/views.py
import random
import string
import time
import uuid
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TrackingNumber



class TrackNumberView(APIView):

    def get(self, request, *args, **kwargs):
        origin_country_id = request.query_params.get('origin_country_id')
        destination_country_id = request.query_params.get('destination_country_id')
        weight = request.query_params.get('weight')
        customer_name = request.query_params.get('customer_name')
        customer_slug = request.query_params.get('customer_slug')
        print("11111111111")
        tracking_number = self.generate_unique_tracking_number()
        print("22222222222",tracking_number)
        tracking_record = TrackingNumber.objects.create(
            tracking_number=tracking_number,
            origin_country_id=origin_country_id,
            destination_country_id=destination_country_id,
            weight=weight,
            customer_id=uuid.uuid4(),
            customer_name=customer_name,
            customer_slug=customer_slug
        )
        return Response({
            "tracking_number": tracking_number,
            "created_at": tracking_record.created_at.isoformat(),
        }, status=status.HTTP_200_OK)

    def generate_unique_tracking_number(self):
        timestamp = str(int(time.time()))
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        res = f'TR{timestamp}{random_str}'[:16]
        return res

