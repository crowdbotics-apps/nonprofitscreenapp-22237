from rest_framework import serializers
from phone.models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = "__all__"
