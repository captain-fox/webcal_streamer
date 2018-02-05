from django.db import models


class ScheduleFile(models.Model):
    file = models.FileField(blank=False)
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True, unique=True)
