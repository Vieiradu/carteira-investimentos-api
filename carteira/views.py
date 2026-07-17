from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ativo, Transacao
from .serializers import AtivoSerializer, TransacaoSerializer

class AtivoViewSet(viewsets.ModelViewSet):
    queryset = Ativo.objects.all()
    serializer_class = AtivoSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

class CarteiraView(APIView):
    def get(self, request):
        usuario_id = request.query_params.get("usuario")
        transacoes = Transacao.objects.filter(usuario_id=usuario_id).select_related("ativo")

        carteira = {}

        for t in transacoes:
            ticker = t.ativo.ticker #Join para consulta o id do tiker
            if ticker not in carteira:
                carteira[ticker] = {
                    "qtd_comprada": 0,
                    "qtd_vendida": 0,
                    "custo": 0,
                }
                
            if t.tipo == "COMPRA":
                carteira[ticker]["qtd_comprada"] += t.quantidade
                carteira[ticker]["custo"] += t.quantidade * t.preco_unitario
            else:
                carteira[ticker]["qtd_vendida"] += t.quantidade
        return Response(carteira)
                