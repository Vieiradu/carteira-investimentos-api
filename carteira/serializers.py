from rest_framework import serializers
from .models import Ativo, Transacao


class AtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ativo
        fields = '__all__'


class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'