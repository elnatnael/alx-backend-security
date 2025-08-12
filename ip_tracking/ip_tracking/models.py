from django.db import models
from django.utils.timezone import now

class RequestLog(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(default=now)
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ip_address} - {self.path} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Request Log'
        verbose_name_plural = 'Request Logs'