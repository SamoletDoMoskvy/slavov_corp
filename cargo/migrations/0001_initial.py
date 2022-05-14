# Generated by Django 4.0.4 on 2022-05-13 21:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('_updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('_is_displayed', models.BooleanField(default=True, verbose_name='Is displayed')),
                ('internal_identifier', models.IntegerField(max_length=255, verbose_name='код товара')),
                ('weight', models.FloatField(default=0, verbose_name='вес')),
                ('width', models.FloatField(default=0, verbose_name='ширина')),
                ('length', models.FloatField(default=0, verbose_name='длина')),
                ('height', models.FloatField(default=0, verbose_name='высота')),
                ('description', models.TextField(blank=True, max_length=1060, null=True)),
                ('from_destination', models.TextField(verbose_name='откуда')),
                ('to_destination', models.TextField(verbose_name='куда')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
