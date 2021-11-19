from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from produits import models
from produits import serializers


class ProductViewSet(viewsets.ModelViewSet):

    queryset = models.Product.objects.all()
    serializer_class = serializers.CreateProductSerializer
