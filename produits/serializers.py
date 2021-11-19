from rest_framework import serializers

from produits.models import Product


class CreateProductSerializer(serializers.ModelSerializer):
    """call this class if u need to create a product (only sellers have the right for this one"""

    class Meta:
        model = Product
        fields = "__all__"
