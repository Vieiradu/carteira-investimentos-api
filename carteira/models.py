from django.conf import settings
from django.db import models


class Ativo(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    nome_empresa = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.ticker


class Transacao(models.Model):
    COMPRA = 'COMPRA'
    VENDA = 'VENDA'
    TIPO_CHOICES = [
        (COMPRA, 'Compra'),
        (VENDA, 'Venda'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transacoes',
    )
    ativo = models.ForeignKey(
        Ativo,
        on_delete=models.PROTECT,
        related_name='transacoes',
    )
    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES)
    quantidade = models.DecimalField(max_digits=15, decimal_places=2)
    preco_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo} {self.quantidade} {self.ativo.ticker}'


class Posicao(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posicoes',
    )
    ativo = models.ForeignKey(
        Ativo,
        on_delete=models.PROTECT,
        related_name='posicoes',
    )
    quantidade = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'ativo'],
                name='uniq_usuario_ativo',
            )
        ]

    def __str__(self):
        return f'{self.usuario} - {self.ativo.ticker}: {self.quantidade}'
