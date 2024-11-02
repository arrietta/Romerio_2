from rest_framework import serializers

from romerio.models import Shape, Collection, Molding, Grid, Bevels, Portal, Colors, Cornice, Podium, Socket, Boots, \
    Door


class ShapeSerializer(serializers.ModelSerializer):
    collection_name = serializers.CharField(source='collection.name', read_only=True)

    class Meta:
        model = Shape
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = '__all__'


class MoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molding
        fields = '__all__'


class BevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bevels
        fields = ['id', 'name', 'price', 'icon']


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = '__all__'


class CorniceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cornice
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


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = '__all__'


class ConstructorSerializer(serializers.ModelSerializer):
    grids = GridSerializer(many=True, read_only=True, source='grid_set')
    moldings = MoldingSerializer(many=True, read_only=True, source='molding_set')
    bevels = BevelSerializer(many=True, read_only=True, source='collection.bevels_set')
    portals = PortalSerializer(many=True, read_only=True, source='cover_type.portal_set')

    class Meta:
        model = Shape
        fields = "__all__"


class DoorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Door
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer(allow_null=True)
    Shape = ShapeSerializer()
    portal = PortalSerializer()
    molding = MoldingSerializer(allow_null=True)
    bevel = BevelSerializer(allow_null=True)
    cornice = CorniceSerializer(allow_null=True)
    podium = PodiumSerializer(allow_null=True)
    boots = BootsSerializer(allow_null=True)
    socket = SocketSerializer(allow_null=True)

    class Meta:
        model = Door
        fields = '__all__'
