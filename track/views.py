# tracking/views.py
import random
import string
import time
import uuid
import re
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TrackingNumber


class TrackNumberView(APIView):

    def get(self, request, *args, **kwargs):
        data = {
            'origin_country_id': request.query_params.get('origin_country_id'),
            'destination_country_id': request.query_params.get('destination_country_id'),
            'weight': request.query_params.get('weight'),
            'customer_id': request.query_params.get('customer_id'),
            'customer_name': request.query_params.get('customer_name'),
            'customer_slug': request.query_params.get('customer_slug'),
        }

        # Validate parameters
        errors = self.validate_data(data)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        tracking_number = self.generate_unique_tracking_number()

        tracking_record = TrackingNumber.objects.create(
            tracking_number=tracking_number,
            origin_country_id=data['origin_country_id'],
            destination_country_id=data['destination_country_id'],
            weight=float(data['weight']),
            customer_id=uuid.uuid4(),
            customer_name=data['customer_name'],
            customer_slug=data['customer_slug']
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

    def validate_data(self, data):
        errors = {}
        # validate origin country id
        if not re.match(r'^[A-Z]{2}$', data['origin_country_id'] or ''):
            errors['origin_country_id'] = "Origin country code must be in ISO 3166-1 alpha-2 " \
                                          "format (e.g., 'US')."

        # validate destination country id
        if not re.match(r'^[A-Z]{2}$', data['destination_country_id'] or ''):
            errors[
                'destination_country_id'] = "Destination country code must be in ISO 3166-1 " \
                                            "alpha-2 format (e.g., 'CA')."

        # Validate weight (decimal, up to three decimal places)
        try:
            weight = float(data['weight'])
            if weight <= 0 or len(str(data['weight']).split('.')[-1]) < 3:
                errors['weight'] = "Weight must be a positive decimal number up to three decimal places."
        except (TypeError, ValueError):
            errors['weight'] = "Weight must be a valid decimal number."

        # Validate customer name
        if not data['customer_name']:
            errors['customer_name'] = "Customer name cannot be empty."

        # Validate customer_slug (kebab-case format)
        def is_kebab_case(slug):
            if not slug:
                return False
            parts = slug.split('-')
            return all(part.islower() and part.isalnum() for part in parts)

        if not is_kebab_case(data['customer_slug']):
            errors['customer_slug'] = "Customer slug must be in slug/kebab-case format (e.g., 'customer-slug')."

        return errors


