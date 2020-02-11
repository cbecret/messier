from django.db import models
from pygments.formatters.html import HtmlFormatter


# Définition précise des champs composant les objets de Messier
class Mobject(models.Model):
    messier_number = models.CharField(max_length=100)
    usual_name = models.CharField(max_length=100, blank=True, null=True, default='')
    ngc = models.CharField(max_length=100, null=True, default='')
    constellation = models.CharField(max_length=100, null=True, default='')
    messier_type = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100, null=True, default='')
    distance_value = models.FloatField(null=True, default=0)
    distance_unit = models.CharField(max_length=100)
    magnitude = models.FloatField()
    ascension = models.CharField(max_length=100, null=True, default='')
    discovery_year = models.CharField(max_length=100, null=True, default='')
    discoverer = models.CharField(max_length=100, null=True, default='')
    image_link = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='mobjects', on_delete=models.CASCADE)

    class Meta:
        ordering = ('messier_number', )

    def save(self, *args, **kwargs):
        formatter = HtmlFormatter(full=True)
        super(Mobject, self).save(*args, **kwargs)
