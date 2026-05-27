from django.db import models


class Performance(models.Model):

    name = models.CharField(
        max_length=100,
        null=False, blank=False,
    )

    author = models.CharField(
        max_length=40,
        null=False, blank=False,
    )

    timespan_minutes = models.PositiveIntegerField(
        null=False, blank=False,
    )

    genre = models.CharField(
        max_length=20,
        null=False, blank=False,
    )

    premiere = models.DateField(
        null=False, blank=False,
    )

    director = models.CharField(
        null=False, blank=False,
    )

    participants = models.TextField(
        null=False, blank=False,
    )

    abstract = models.TextField(
        null=False, blank=False,
    )

    performance_image = models.ImageField(
        null=False, blank=False,
    )
    