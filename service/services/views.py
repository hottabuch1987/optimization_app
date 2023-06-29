from django.conf import settings
from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.core.cache import cache
from clients.models import User
from .models import Subscription, Plan
from .serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related('plan',
        Prefetch('client', queryset=User.objects.all().only('company_name', 'email'))
    )
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        #cache

        price_cache = cache.get(settings.PRICE_CACHE_NAME)
        if price_cache:
            total_price = price_cache
        else:
            total_price = queryset.aggregate(total=Sum('price')).get('total')
            #кладеm в кеш
            cache.set(settings.PRICE_CACHE_NAME, total_price, 60 * 60)
        #cache
        response_data = {'result': response.data}
        response_data['total_amount'] = total_price
        response.data = response_data
        return response
