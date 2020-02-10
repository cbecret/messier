from django.db import models
from pygments.formatters.html import HtmlFormatter


class Mobject(models.Model):
    messier_number = models.CharField(max_length=100)
    usual_name = models.CharField(max_length=100, blank=True, null=True, default='')
    ngc = models.CharField(max_length=100)
    constellation = models.CharField(max_length=100)
    messier_type = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100)
    distance_value = models.FloatField()
    distance_unit = models.CharField(max_length=100)
    magnitude = models.FloatField()
    ascension = models.CharField(max_length=100)
    discovery_date = models.DateField()
    discoverer = models.CharField(max_length=100)
    image_link = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='mobjects', on_delete=models.CASCADE)

    class Meta:
        ordering = ('messier_number', )

    def save(self, *args, **kwargs):
        formatter = HtmlFormatter(full=True)
        super(Mobject, self).save(*args, **kwargs)
