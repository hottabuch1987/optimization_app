from rest_framework.routers import DefaultRouter

from services.views import SubscriptionView

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionView)
#http://127.0.0.1:8000/api/v1/subscriptions/?format=json
