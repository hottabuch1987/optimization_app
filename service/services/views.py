from django.db.models import Prefetch, F
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import User
from .models import Subscription, Plan
from .serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related('plan',
        Prefetch('client', queryset=User.objects.all().only('company_name', 'email'))
    ).annotate(price=F('service__full_price') -
                     F('service__full_price') * F('service__full_price') / 100.00 )
    serializer_class = SubscriptionSerializer
