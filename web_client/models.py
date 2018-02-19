from django.db import models
from django.core.validators import validate_comma_separated_integer_list
import uuid


class ScheduleFile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
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


class RawCSVEvent(models.Model):

    ref = models.IntegerField(null=True)
    title = models.TextField(blank=True)
    weekday = models.CharField(max_length=20, blank=False)
    time_start = models.TimeField(null=False)
    time_end = models.TimeField(null=False)
    semester_weeks = models.CharField(validators=[validate_comma_separated_integer_list], max_length=100)
    category = models.TextField(blank=True)
    module_code = models.CharField(max_length=10, blank=True)
    room = models.TextField(blank=True)
    teacher = models.CharField(max_length=40, blank=True)
    group = models.TextField(max_length=20, blank=True)

