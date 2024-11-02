import uuid

from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.core.cache import cache
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView

from romerio.filters import DoorFilter, CollectionFilter
from romerio.models import Shape, Collection, Bevels, Portal, Colors, Cornice, Boots, Podium, Socket, Door
from romerio.serializers import ShapeSerializer, CollectionSerializer, ConstructorSerializer, PortalSerializer, \
    ColorSerializer, CorniceSerializer, BootsSerializer, PodiumSerializer, SocketSerializer, DoorSerializer, \
    CartSerializer
from romerio.telegram_bot import send_message_to_bot, process_and_send_images
from romerio.translation import translate


def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})


def identification(request):
    unique_id = request.COOKIES.get('unique_id', 'Not available')
    if unique_id == 'Not available':
        unique_id = str(uuid.uuid4())
        response = JsonResponse({'unique_id': unique_id})
        response.set_cookie('unique_id', unique_id, max_age=86400)
        return response
    return JsonResponse({'unique_id': unique_id})


def order(request):
    if request.method == 'POST':
        unique_id = request.POST.get('unique_id')


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        number = request.data.get('phone')
        unique_id = request.data.get('unique_id')
        delivery = request.data.get('delivery')
        measurement = request.data.get('measurement')

        if not (name and number and unique_id):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        filtered_queryset = self.queryset.filter(client_id=unique_id)

        if not filtered_queryset.exists():
            return Response({"error": "No data found for this UID"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(filtered_queryset, many=True)

        images = []

        for item in serializer.data:
            images.append("http://127.0.0.1:8000/static/catalog/background.jpg")
            images.append(item['Shape']['image'].replace('color', item['color']))
            images.append(item['portal']['image'].replace('color', item['color']))
            if item['molding'] and item["Shape"]['cover_type'] == "Emal": images.append(
                item['molding']['image'].replace('color', item['molding_color']))

            message = (f"ФИО: {name}"
                       f"\nНомер: {number}\n"
                       f"\nДоставка: {translate(delivery)}\n"
                       f"\nЗамеры: {translate(measurement)}\n"
                       f"\nДверь:"
                       f"\nКоллекция: {translate(item['collection']['name'].replace("Shpone_", ""))}"
                       f"\nТип: {translate(item['Shape']['cover_type'])}"
                       f"\nФорма: {translate(item['Shape']['name'])}"
                       f"\nЦвет: {translate(item['color'].replace('_', ' '))}"
                       f"\nЦвет-вставки: {translate(item['molding_color'].replace('_', ' ')) if item['molding_color'] else ""}"
                       f"\nНаличник: {translate(item['portal']['name'])}"

                       f"{"\nБагет: " + translate(item['molding']['name']) if item['molding'] else ""}"
                       f"{"\nФреза: " + translate(item['bevel']['name']) if item['bevel'] else ""}"
                       f"{"\nРешётка: " + translate(item['grid']) if item['grid'] else ""}"
                       f"{"\nФреза решётки: " + translate(item['grid_bevel']) if item['grid_bevel'] else ""}"
                       f"{"\nКорниз: " + translate(item['cornice']['name']) if item['cornice'] else ""}"
                       f"{"\nВозвышение: " + translate(item['podium']['name']) if item['podium'] else ""}"
                       f"{"\nРозетки: " + translate(item['socket']['name']) if item['socket'] else ""}"
                       f"{"\nСопожки: " + translate(item['boots']['name']) if item['boots'] else ""}"

                       f"\nКоличество: {item['count']}"
                       f"\nЦена: {item['price']}"
                       f"")
            process_and_send_images(images)
            images.clear()
            send_message_to_bot(message)

            filtered_queryset.delete()

        return Response({"message": "Data processed and sent to Telegram"}, status=status.HTTP_201_CREATED)


def get_cache(cache_key, ViewSet):
    cached_data = cache.get(cache_key)

    if cached_data is None:
        queryset = ViewSet.get_queryset()
        serializer = ViewSet.get_serializer(queryset, many=True)
        cached_data = serializer.data
        cache.set(cache_key, cached_data, timeout=60 * 15)

    return Response(cached_data)


class ShapeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = DoorFilter

    ordering = ['id', 'name', 'price', ]


class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = CollectionFilter

    ordering = ['id']


class DoorDetailView(APIView):
    def get(self, request, shape_id):
        try:
            shape = Shape.objects.get(id=shape_id)
            shape_serializer = ConstructorSerializer(shape)
            portals = Portal.objects.filter(cover_type=shape.cover_type)
            portal_serializer = PortalSerializer(portals, many=True)

            cornice = Cornice.objects.filter(cover_type=shape.cover_type)
            cornice_serializer = CorniceSerializer(cornice, many=True)

            boots = Boots.objects.filter(cover_type=shape.cover_type)
            boots_serializer = BootsSerializer(boots, many=True)

            podium = Podium.objects.filter(cover_type=shape.cover_type)
            podium_serializer = PodiumSerializer(podium, many=True)

            socket = Socket.objects.filter(cover_type=shape.cover_type)
            socket_serializer = SocketSerializer(socket, many=True)

            colors = Colors.objects.filter(cover_type=shape.cover_type)
            if shape.collection.name == "Novara":
                colors = Colors.objects.all()
            color_serializer = ColorSerializer(colors, many=True)

            return Response({
                'shape': shape_serializer.data,
                'portals': portal_serializer.data,
                'colors': color_serializer.data,
                'cornice': cornice_serializer.data,
                'boots': boots_serializer.data,
                'podium': podium_serializer.data,
                'socket': socket_serializer.data
            }, status=status.HTTP_200_OK)
        except Shape.DoesNotExist:
            return Response({'error': 'Shape not found'}, status=status.HTTP_404_NOT_FOUND)


class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = CartSerializer

    def list(self, request, *args, **kwargs):
        unique_id = request.query_params.get('unique_id', None)
        if unique_id is not None:
            queryset = self.queryset.filter(client_id=unique_id)
        else:
            return Response({"detail": "unique_id parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def Main(request):
    return render(request, 'main/index.html')


def privacy(request):
    return render(request, "index.html")


def cart(request):
    return render(request, "index.html")


def catalog(request):
    return render(request, "index.html")


def catalog_element(request, id):
    return render(request, "index.html")
