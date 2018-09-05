from auditlog.registry import auditlog
from django.db import models
from django.utils import timezone
import uuid

class Faces(models.Model):
    landmarks = models.CharField(max_length = 2500)
    created_at = models.DateTimeField(default=timezone.now())
    active = models.BooleanField(default=True)

class Shops(models.Model):
    shop_uuid = models.UUIDField(unique=True, default=uuid.uuid4())
    shop_name = models.CharField(max_length=40)

class Locals(models.Model):
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, to_field='shop_uuid')
    name = models.CharField(unique=True, max_length=50)

class Faces_in_shops(models.Model):
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, to_field='shop_uuid')
    face = models.ForeignKey(Faces, on_delete=models.CASCADE, to_field='id')
    local = models.ForeignKey(Locals, on_delete=models.CASCADE, to_field='id')
    counts = models.IntegerField()
    time = models.DateTimeField(default=timezone.now())

# class Logs(models.Model):
#     face_id = models.IntegerField()
#     local_id = models.IntegerField()
#     shop_uuid = models.UUIDField()
#     timestamp = models.DateTimeField(default=timezone.now())

#Auditing
auditlog.register(Faces)
auditlog.register(Shops)
auditlog.register(Locals)
auditlog.register(Faces_in_shops)