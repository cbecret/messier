from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


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
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the mobject.
        """
        lexer = get_lexer_by_name(self.messier_number)
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.usual_name, lexer, formatter)
        super(Mobject, self).save(*args, **kwargs)

    class Meta:
        ordering = ['messier_number']
