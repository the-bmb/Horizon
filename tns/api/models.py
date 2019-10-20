from django.db import models


class User(models.Model):
    """
    Model for User
    """
    name = models.TextField(
        "name", help_text="Your name")
    email = models.TextField(
        "email", help_text="Your email")
    password = models.TextField(
        "password", help_text="Your password")
    birthday = models.DateField(
        "birthday", help_text="Your birthday")
    id_doc = models.TextField(
        "id_doc", help_text="Your document")

    def __str__(self):
        return '{}'.format(self.name)


class Flight(models.Model):
    """
    Model for flight
    """
    departure = models.DateField(
        "departure", help_text="Departure")
    arrival = models.DateField(
        "arrival", help_text="Arrival")
    simple_rooms = models.IntegerField(
        "simple_rooms", help_text="Simple rooms available")
    double_rooms = models.IntegerField(
        "double_rooms", help_text="Double rooms available")
    price = models.DecimalField(
        "price", decimal_places=2, max_digits=15, help_text="Price")

    class Meta:
        ordering = ["departure"]

    def __str__(self):
        return '{} - {}'.format(self.departure, self.arrival)


class Travelers(models.Model):
    """
    Model for travelers
    """
    f_name = models.TextField(
        "f_name", help_text="First Name")
    l_name = models.TextField(
        "l_name", help_text="Last Name")
    suit_size = models.TextField(
        "suit_size", help_text="Suit size")


class Travel(models.Model):
    """
    Model for travel
    """
    buyer = models.ForeignKey(
        User, related_name='user', on_delete=models.CASCADE,
        verbose_name="Buyer")
    travelers = []
    room = models.IntegerField(
        "room", help_text="Room type")
    flight = models.ForeignKey(
        Flight, related_name='flight', on_delete=models.CASCADE,
        verbose_name="Flight")

    def __str__(self):
        return '{} - {}'.format(self.flight, self.room)
