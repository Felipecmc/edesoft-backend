from django.db import models

class Cessao(models.Model):
    id_cessao = models.CharField(max_length=250)
    originador = models.CharField(max_length=250)
    doc_originador = models.CharField(max_length=250)
    cedente = models.CharField(max_length=250)
    ccb = models.CharField(max_length=250)
    cliente = models.CharField(max_length=250)
    cpf_cnpj = models.CharField(max_length=50)
    endereco = models.CharField(max_length=250)
    cep = models.CharField(max_length=250)
    cidade = models.CharField(max_length=250)
    uf = models.CharField(max_length=50)
    valor_do_emprestimo = models.CharField(max_length=250)
    valor_parcela = models.CharField(max_length=250)
    total_parcelas = models.CharField(max_length=250)
    parcela = models.CharField(max_length=250)
    data_de_emissao = models.CharField(max_length=250)
    data_de_vencimento = models.CharField(max_length=250)
    preco_de_aquisicao = models.FloatField()
    
    