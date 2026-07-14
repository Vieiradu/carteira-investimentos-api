from django.shortcuts import render
from rest_framework import viewsets
from .models import Ativo, Transacao
from .serializers import AtivoSerializer, TransacaoSerializer

class AtivoViewSet(viewsets.ModelViewSet):
    queryset = Ativo.objects.all()
    serializer_class = AtivoSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer