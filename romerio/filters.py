import django_filters
from .models import Shape, Collection


class DoorFilter(django_filters.FilterSet):
    class Meta:
        model = Shape
        fields = {
            'cover_type': ['exact', 'in'],  # Allows filtering by exact match or multiple values
            'door_type': ['exact', 'in'],  # 'exact' added for consistency if needed
            'price': ['lt', 'gt'],  # Added 'exact' to allow precise price filtering
            'collection': ['in'],  # Allows filtering by a specific collection or multiple collections
        }


class CollectionFilter(django_filters.FilterSet):
    class Meta:
        model = Collection
        fields = {
            'type': ['exact'],
        }
