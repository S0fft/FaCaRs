from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = "__all__"
