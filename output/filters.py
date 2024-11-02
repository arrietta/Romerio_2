import django_filters

from main.models import Shape, Shpone


class DoorFilter(django_filters.FilterSet):
    class Meta:
        model = Shape
        fields = {
            'door_type': ['in'],
            'price': ['lt', 'gt'],
            'collections': ['in'],
        }


class ShponeFilter(django_filters.FilterSet):
    class Meta:
        model = Shpone
        fields = {
            'door_type': ['in'],
            'price': ['lt', 'gt'],
            'collections': ['in'],
        }