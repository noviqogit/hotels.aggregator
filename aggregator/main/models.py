from django.db import models
import os
import jwt
from datetime import datetime, timedelta


class Cities(models.Model):
    city_id = models.IntegerField()
    city_name = models.CharField()


class Hotels(models.Model):
    hotel_id = models.IntegerField()
    hotel_name = models.CharField()
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)


class Services(models.Model):
    service_id = models.IntegerField()
    service_name = models.CharField()
    service_price = models.IntegerField()
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE)


class Rooms(models.Model):
    room_id = models.IntegerField()
    room_name = models.CharField(blank=True, default='')
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE)


class Devices(models.Model):
    device_id = models.IntegerField()
    room_id = models.ForeignKey(Rooms, null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'device_id'
    REQUIRED_FIELDS = ['room_id']

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.device_id,
            'exp': int(dt.strftime('%s'))
        }, os.getenv('SECRET_KEY'), algorithm='HS256')

        return jwt.decode(token, algorithms=['HS256', ])


class Clients(models.Model):
    client_id = models.IntegerField()
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    room_id = models.ForeignKey(Rooms, null=True, on_delete=models.SET_NULL)


class Orders(models.Model):
    order_id = models.IntegerField()
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    class Meta:
        ordering = ['created_at']


class OrderInfo(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, null=True, on_delete=models.SET_NULL)
