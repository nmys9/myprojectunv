from rest_framework import serializers
from .models import *

class WiFiFingerprintSerializer(serializers.ModelSerializer):
    class Meta:
        model=WiFiFingerprint
        fields='__all__'