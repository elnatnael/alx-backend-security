from django.db import models
from django.utils.timezone import now

class RequestLog(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(default=now)
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address} - {self.path} - {self.timestamp}"

class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ip_address