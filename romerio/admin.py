from django.contrib import admin
from .models import (
    Collection,
    Shape,
    Molding,
    Portal,
    Cornice,
    Podium,
    Boots,
    Socket,
    Door, Bevels,
)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    list_display = ('name', 'door_type', 'cover_type', 'color', 'price')
    list_filter = ('door_type', 'cover_type', 'color')
    search_fields = ('name',)


@admin.register(Molding)
class MoldingAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name',)
    list_filter = ('color',)


@admin.register(Portal)
class PortalAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name',)
    list_filter = ('color',)


@admin.register(Cornice)
class CorniceAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name',)
    list_filter = ('color',)


@admin.register(Podium)
class PodiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name',)
    list_filter = ('color',)


@admin.register(Boots)
class BootsAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name',)
    list_filter = ('color',)


@admin.register(Socket)
class SocketAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name',)
    list_filter = ('color',)


@admin.register(Bevels)
class BevelsAdmin(admin.ModelAdmin):
    list_display = ('name', 'collection', 'price','icon')
    search_fields = ('name',)

@admin.register(Door)
class DoorAdmin(admin.ModelAdmin):
    list_display = ('collection', 'Shape', 'portal', 'cornice', 'podium', 'boots', 'socket', 'price', 'color')
    list_filter = ('collection', 'Shape', 'portal', 'cornice', 'podium', 'boots', 'socket')
    search_fields = ('collection__name', 'Shape__name', 'color')
