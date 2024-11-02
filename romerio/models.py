from django.db import models

DOOR_TYPE_CHOICES = [
    ('DO', 'DO'),
    ('Classic', 'Classic'),
]
DOOR_COVER_CHOICES = [
    ('Emal', 'Эмаль'),
    ('Shpone', 'Шпон'),
]
Size_CHOICES = [
    ('Size-1', 'Размер-1'),
    ('Size-2', 'Размер-2'),
]


class Collection(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=DOOR_COVER_CHOICES, default='Emal')

    def __str__(self):
        return self.name


class Shape(models.Model):
    cover_type = models.CharField(max_length=7, choices=DOOR_COVER_CHOICES, default="Emal")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="Standard")
    door_type = models.CharField(max_length=7, choices=DOOR_TYPE_CHOICES)
    has_molding = models.BooleanField(default=False)
    has_bevel = models.BooleanField(default=False, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='shape/')
    has_grid = models.BooleanField(default=False, blank=True, null=True)
    icon = models.ImageField(upload_to='icon/Shape/', default='none')
    Cart_icon = models.ImageField(upload_to='icons/Shape/', default='none')
    glass = models.ImageField(upload_to='glass/', default='none')

    def __str__(self):
        return self.name


class Molding(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, default=1)
    Shape = models.ForeignKey(Shape, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="Standard")
    image = models.ImageField(upload_to='moldings/')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    icon = models.ImageField(upload_to='icon/Molding', default='none')

    def __str__(self):
        return self.name


class Grid(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, default=1)
    Shape = models.ForeignKey(Shape, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='grid/')
    bevel = models.CharField(max_length=255, default="none")
    bevel_icon = models.ImageField(upload_to='icon/grid/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    icon = models.ImageField(upload_to='icon/Grid', default='none')

    def __str__(self):
        return self.name


class Colors(models.Model):
    name = models.CharField(max_length=255)
    additional_price = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    hex = models.CharField(max_length=7, default="#FFFFFF")
    cover_type = models.CharField(max_length=7, choices=DOOR_TYPE_CHOICES, default="Shpone")

    def __str__(self):
        return self.name


class Bevels(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    icon = models.ImageField(upload_to='icon/Bevel', default='none')

    def __str__(self):
        return self.name


class Portal(models.Model):
    cover_type = models.CharField(max_length=7, choices=DOOR_COVER_CHOICES, default="Emal")
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="Standard")
    size = models.CharField(max_length=255, choices=Size_CHOICES, default="Size-1")
    image = models.ImageField(upload_to='portals/')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    icon = models.ImageField(upload_to='icon/Portal/', default='none')

    def __str__(self):
        return self.name


class Cornice(models.Model):
    cover_type = models.CharField(max_length=7, choices=DOOR_COVER_CHOICES, default="Emal")
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="Standard")
    size = models.CharField(max_length=255, choices=Size_CHOICES, default="Size-1")
    image = models.ImageField(upload_to='cornices/')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    icon = models.ImageField(upload_to='icon/Carnice/', default='none')

    def __str__(self):
        return self.name


class Podium(models.Model):
    cover_type = models.CharField(max_length=7, choices=DOOR_COVER_CHOICES, default="Emal")
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="Standard")
    size = models.CharField(max_length=255, choices=Size_CHOICES, default="Size-1")
    image = models.ImageField(upload_to='podiums/')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    icon = models.ImageField(upload_to='icon/Podium/', default='none')

    def __str__(self):
        return self.name


class Boots(models.Model):
    cover_type = models.CharField(max_length=7, choices=DOOR_COVER_CHOICES, default="Emal")
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="Standard")
    size = models.CharField(max_length=255, choices=Size_CHOICES, default="Size-1")
    image = models.ImageField(upload_to='boots/')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    icon = models.ImageField(upload_to='icon/Boots/', default='none')

    def __str__(self):
        return self.name


class Socket(models.Model):
    cover_type = models.CharField(max_length=7, choices=DOOR_COVER_CHOICES, default="Emal")
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255, choices=Size_CHOICES, default="Size-1")
    color = models.CharField(max_length=255, default="Standard")
    image = models.ImageField(upload_to='sockets/')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    icon = models.ImageField(upload_to='icon/Socket/', default='none')

    def __str__(self):
        return self.name


class Door(models.Model):
    client_id = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    Shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    grid = models.CharField(max_length=255, null=True, blank=True)
    grid_bevel = models.CharField(max_length=255, null=True, blank=True)
    molding = models.ForeignKey(Molding, on_delete=models.CASCADE, null=True, blank=True)
    bevel = models.ForeignKey(Bevels, on_delete=models.CASCADE, null=True, blank=True)
    cornice = models.ForeignKey(Cornice, on_delete=models.CASCADE, null=True, blank=True)
    podium = models.ForeignKey(Podium, on_delete=models.CASCADE, null=True, blank=True)
    boots = models.ForeignKey(Boots, on_delete=models.CASCADE, null=True, blank=True)
    socket = models.ForeignKey(Socket, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    color = models.CharField(max_length=255, null=True, blank=True)
    molding_color = models.CharField(max_length=255, null=True, blank=True)
    color_hex = models.CharField(max_length=255, null=True, blank=True)
    count = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, default=1)

    def __str__(self):
        return f"{self.collection.name} - {self.Shape.name}"
