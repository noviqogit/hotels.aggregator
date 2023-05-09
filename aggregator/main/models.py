from django.db import models


class Cities(models.Model):
    city_id = models.IntegerField()
    city_name = models.CharField()


class Hotels(models.Model):
    hotel_id = models.IntegerField()
    hotel_name = models.CharField()
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)


class Service(models.Model):
    service_id = models.IntegerField()
    service_name = models.CharField()
    service_price = models.IntegerField()
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE)


class Rooms(models.Model):
    room_id = models.IntegerField()
    room_name = models.CharField()
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE)


class Devices(models.Model):
    device_id = models.IntegerField()
    room_id = models.ForeignKey(Rooms, null=True, on_delete=models.SET_NULL)


class Clients(models.Model):
    client_id = models.IntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    room_id = models.ForeignKey(Rooms, null=True, on_delete=models.SET_NULL)


class Order(models.Model):
    order_id = models.IntegerField()
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()


class OrderInfo(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
