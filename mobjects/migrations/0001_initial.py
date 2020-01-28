# Generated by Django 2.1.4 on 2020-01-27 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messier_number', models.CharField(max_length=100)),
                ('usual_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('ngc', models.CharField(max_length=100)),
                ('constellation', models.CharField(max_length=100)),
                ('messier_type', models.CharField(max_length=100)),
                ('dimension', models.CharField(max_length=100)),
                ('distance_value', models.FloatField()),
                ('distance_unit', models.CharField(max_length=100)),
                ('magnitude', models.FloatField()),
                ('ascension', models.CharField(max_length=100)),
                ('discovery_date', models.DateField()),
                ('discoverer', models.CharField(max_length=100)),
                ('image_link', models.TextField()),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobjects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['messier_number'],
            },
        ),
    ]