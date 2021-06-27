from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import uuid


class Country(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default="", editable=False, max_length=200)

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.name)

        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Network(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default="", editable=False, max_length=200)
    official = models.BooleanField(default=True)
    description = models.TextField(default="N/A")

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.name)

        super(Network, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Cast(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default="", editable=False, max_length=200)
    image = models.ImageField(default="default.jpg", upload_to="tvshow", max_length=500)
    birthday = models.CharField(default="N/A", max_length=200)
    cast_uuid = models.CharField(default="", editable=False, max_length=100)

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.name)

        if self.cast_uuid == "":
            self.cast_uuid = uuid.uuid4().hex

        super(Cast, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default="", editable=False, max_length=200)

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.name)

        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class TVShowState(models.TextChoices):
    Pending = "Pending"
    Published = "Published"
    Archived = "Archived"
    Deleted = "Deleted"


class TVShow(models.Model):
    title = models.CharField(max_length=200)
    also_known_as = models.CharField(max_length=200, default="N/A")
    description = models.TextField(default="N/A")
    slug = models.SlugField(default="", editable=False, max_length=200)

    image = models.ImageField(default="default.jpg", upload_to="tvshow", max_length=500)
    image_url = models.CharField(max_length=500, default="N/A")

    air_time = models.CharField(max_length=200, default="N/A")
    release_date = models.CharField(max_length=200, default="N/A")
    year = models.CharField(max_length=20, default="N/A")
    date_added = models.DateTimeField(default=timezone.now)

    trailer = models.CharField(max_length=500, default="N/A")
    state = models.CharField(
        max_length=20, choices=TVShowState.choices, default=TVShowState.Pending
    )

    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True
    )
    network = models.ForeignKey(
        Network, on_delete=models.SET_NULL, blank=True, null=True
    )
    genre = models.ManyToManyField(Genre)
    cast = models.ManyToManyField(Cast)

    def save(self, *args, **kwargs):

        if self.slug == "":
            self.slug = slugify(self.title)

        super(TVShow, self).save(*args, **kwargs)

    def latest_release(self):
        return TVShow.objects.get(id=self.id).releasev2_set.order_by("-date_added")[0]

    def __str__(self):
        return self.title


class ReleaseV2(models.Model):
    number = models.CharField(max_length=20)
    date_added = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=200)
    tvshow = models.ForeignKey(TVShow, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Ep.{self.number}"
