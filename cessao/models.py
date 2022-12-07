from django.db import models

class Cessao(models.Model):
    id_cessao = models.IntegerField()
    originador = models.CharField(max_length=250)
    doc_originador = models.IntegerField()
    cedente = models.CharField(max_length=250)
    ccb = models.IntegerField()
    id_externo = models.IntegerField()
    cliente = models.CharField(max_length=250)
    cpf_cnpj = models.CharField(max_length=50)
    endereco = models.CharField(max_length=250)
    cep = models.CharField(max_length=250)
    cidade = models.CharField(max_length=250)
    uf = models.CharField(max_length=50)
    valor_do_emprestimo = models.FloatField()
    valor_parcela = models.FloatField()
    total_parcelas = models.IntegerField()
    parcela = models.IntegerField()
    data_de_emissao = models.DateField()
    data_de_vencimento = models.DateField()
    preco_de_aquisicao = models.FloatField()
    
    