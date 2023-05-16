from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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


class Rooms(models.Model):
    room_id = models.IntegerField()
    room_name = models.CharField(blank=True, default='')
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE)


class Services(models.Model):
    service_id = models.IntegerField()
    service_name = models.CharField()
    service_price = models.IntegerField()
    hotel_id = models.ForeignKey(Hotels, on_delete=models.CASCADE)


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


class DeviceManager(BaseUserManager):

    def create_user(self, device_id, password=None, room_id=None):
        if device_id is None:
            raise TypeError('Devices must have an id.')

        room = Rooms.objects.get(room_id=room_id)

        device = self.model(device_id=device_id, room_id=room)
        device.set_password(password)
        device.save()

        return device

    def create_superuser(self, device_id, password, room_id=None):
        if password is None:
            raise TypeError('Superusers must have a password.')

        room = Rooms.objects.get(room_id=room_id)

        device = self.model(device_id=device_id, password=password, room_id=room)
        device.is_superuser = True
        device.is_staff = True
        device.save()

        return device


class Devices(AbstractBaseUser, PermissionsMixin):
    device_id = models.IntegerField(db_index=True, unique=True)
    room_id = models.ForeignKey(Rooms, null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'device_id'
    REQUIRED_FIELDS = ['room_id']

    objects = DeviceManager()

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
