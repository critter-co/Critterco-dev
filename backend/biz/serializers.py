from rest_framework import serializers
from .models import Biz


class BizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biz
        fields = '__all__'
        read_only_fields = ['created', 'created_by']
