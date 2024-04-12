import json
from django.core import serializers as core_serializers
from rest_framework import routers, serializers, viewsets
from apps.authentication.models import Quote, User
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser']

class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_serializer = UserSerializer(instance=self.user)
        serialized_user = user_serializer.data
        data['user'] = serialized_user
        print(data)
        return data
    

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Quote
        fields = ('id','user', 'item_name', 'item_description','item_value','installments')

