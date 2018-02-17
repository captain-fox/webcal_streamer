from django.db import models
import uuid


class ScheduleFile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid1(), editable=False)
    file = models.FileField(null=False, upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['created']


class Term(models.Model):

    title = models.TextField(blank=False)
    term_begins = models.DateField(null=False)
    term_ends = models.DateField(null=False)
    holidays_begin = models.DateField(null=False)
    holidays_end = models.DateField(null=False)


class SwitchedDay(models.Model):

    term = models.ForeignKey(Term, related_name='switched_days', on_delete=models.CASCADE)
    replaces = models.DateField()
    replaced_with = models.DateField()
