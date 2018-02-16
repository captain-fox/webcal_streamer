from django.db import models
import uuid


class ScheduleFile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid1(), editable=False)
    file = models.FileField(null=False, upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['created']
