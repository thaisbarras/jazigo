import os
from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.db import models
from django.forms.utils import ErrorList
import datetime

class Cemiterio(models.Model):
    cemiterio = models.CharField(max_length=100, null=False, blank=False)
    endereco_cemiterio = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    uf = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.cemiterio


class TransferenciaDeOssada(models.Model):
    cemiterio_origem = models.ForeignKey(Cemiterio, on_delete=models.CASCADE, related_name='cemiterio_origem')
    cemiterio_destino = models.ForeignKey(Cemiterio, on_delete=models.CASCADE, related_name='cemiterio_destino')
    nome_responsavel_translado = models.CharField(max_length=100)
    documento_responsavel_translado = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(f'Origem: {self.cemiterio_origem} - Destino: {self.cemiterio_destino}')
    
class Sepultado(models.Model): 
    LOCAIS_SEPULTAMENTO = [
        ("Piraí", "pirai"),
        ("Santanésia", "santanesia"),
        ("Cacaria", "cacaria"),
        ("Arrozal", "arrozal"),
        ("Externo", "externo"),
    ]
    
    def pasta_de_upload(instance, filename):
        name, ext = filename.split('.')
        #file_path = "documentos/{data_falecimento}/{nome_sepultado}/sepultado_{nome_sepultado}.{ext}".format(
            #id=instance.id, nome_sepultado=instance.nome_sepultado, ext=ext) 
        #return file_path       
        return '/'.join(filter(None, ('documentos', str(instance.data_falecimento), instance.nome_sepultado, filename)))

    nome_sepultado = models.CharField(max_length=100)
    data_falecimento = models.DateField() 
    local_sepultamento = models.CharField(max_length=100, choices=LOCAIS_SEPULTAMENTO)
    transferencia_ossada = models.ForeignKey(TransferenciaDeOssada, on_delete=models.SET_NULL, null=True, blank=True)
    certidao_obito = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)
    guia_sepultamento = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)
    termo_concessao_jazigo_perpetuo = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)
    recibo_pagamento = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)
    transferencia_restos_mortais = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)

    '''certidao_obito = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)
    guia_sepultamento = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)
    termo_concessao_jazigo_perpetuo = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)
    recibo_pagamento = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)
    transferencia_restos_mortais = models.FileField(upload_to=pasta_de_upload, blank=True, null=True)'''
    
    def __str__(self) -> str:
        return self.nome_sepultado


'''class Arquivo(models.Model):
    nome_sepultado = models.ForeignKey(Sepultado, on_delete=models.CASCADE)   

    TIPO_DOCUMENTO = [
        ("CERTIDÃO DE ÓBITO", "Certidão de Óbito"),
        ("GUIA DE SEPULTAMENTO", "Guia de Sepultamento"),
        ("TERMO DE CONCESSÃO DE JAZIGO PERPÉTUO", "Termo de Concessão de Jazigo Perpétuo"),
        ("RECIBOS DE PAGAMENTOS", "Recibos de Pagamento"),
        ("TRANSPARÊNCIA DE RESTOS MORTAIS", "Transferência de Restos Mortais"),
    ]

    tipo_documento = models.CharField(max_length=100, choices=TIPO_DOCUMENTO, default='')
    
    #arquivo = models.FileField(pasta_de_uploadupload_to="documentos/%Y/%m/%d/", null=True)
    arquivo = models.FileField(upload_to=pasta_de_upload)

    def __str__(self) -> str:
        return str(self.tipo_documento)'''
       
class QuadraESepultura(models.Model):
    quadra = models.CharField(max_length=10)
    sepultura = models.IntegerField()
    complemento = models.CharField(max_length=10, default=" ", blank=True, null=False)

    def __str__(self) -> str:
        return f'{self.quadra}{self.sepultura}{self.complemento}'



class Concessionario(models.Model):
    nome_concessionaro = models.CharField(max_length=100)
    cpf_concessionario = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    observacao = models.TextField(null=True, blank=True)


    def __str__(self) -> str:
        return self.nome_concessionaro

class Jazigo(models.Model):
    TIPO_JAZIGO = [
        ("Público", "publico"),
        ("Perpétuo", "perpetuo"),
    ]
    
    identificacao_jazigo = models.OneToOneField(QuadraESepultura, on_delete=models.CASCADE, unique=True)
    nome_concessionaro = models.ForeignKey(Concessionario, on_delete=models.CASCADE)
    jazigo_perpetuo_publico = models.CharField(max_length=100, choices=TIPO_JAZIGO)
    observacao = models.TextField(null=True, blank=True)
    nome_sepultado = models.ManyToManyField(Sepultado)      

    def __str__(self) -> str:
        return str(self.identificacao_jazigo)
