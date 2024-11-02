from collections import OrderedDict

from rest_framework import serializers

from main.models import *


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = '__all__'


class MoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molding
        fields = '__all__'


class CarniceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carnice
        fields = '__all__'


class PodiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podium
        fields = '__all__'


class SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socket
        fields = '__all__'


class BootsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boots
        fields = '__all__'


class ShapeSerializer(serializers.ModelSerializer):
    # Portal = PortalSerializer(many=True, read_only=True)
    # molding = MoldingSerializer(many=True, read_only=True)
    # carnice = CarniceSerializer(many=True, read_only=True)
    # podium = PodiumSerializer(many=True, read_only=True)
    # Boots = BootsSerializer(many=True, read_only=True)

    class Meta:
        model = Shape
        fields = ['name', 'door_type', 'price', 'collections']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class Shpon_CarniceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shpon_Carnice
        fields = '__all__'


class Shpon_SocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shpon_Socket
        fields = '__all__'


class Shpon_BootsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shpon_Boots
        fields = '__all__'


class Shpon_MoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shpon_Molding
        fields = '__all__'


# shpone_molding = Shpon_MoldingSerializer(many=True, read_only=True)
# shpone_carnice = Shpon_CarniceSerializer(many=True, read_only=True)
# shpone_boots = Shpon_BootsSerializer(many=True, read_only=True)
class ShponeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shpone
        fields = ['name', 'collections', 'door_type', 'price']
