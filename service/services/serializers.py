from rest_framework import serializers

from services.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()

    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.email')
    price = serializers.SerializerMethodField()

    def get_price(self, instance):      #формула расчета
        return instance.price
        # return (instance.service.full_price -
        #         instance.service.full_price * (instance.plan.discount_percent / 100))

    class Meta:
        model = Subscription
        fields = ('id', 'date_joined', 'plan_id', 'client_name', 'email', 'created_at_formatted', 'plan', 'price')
