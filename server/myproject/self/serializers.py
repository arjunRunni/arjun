from rest_framework import serializers
from self.models import Items
from django.db.models import fields


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('name','rate')

