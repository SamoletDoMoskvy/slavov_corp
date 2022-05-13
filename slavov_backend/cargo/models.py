from django.db.models import (
    CharField,
    TextField,
    FloatField,
)

from base.models import AbstractBaseModel


class Cargo(AbstractBaseModel):

    TYPES = (
        ('конверт', 'КОНВЕРТ'),
        ('посылка', 'ПОСЫЛКА'),
        ('ручная кладь', 'РУЧНАЯ КЛАДЬ'),
    )

    name = CharField(
        max_length=255,
        verbose_name='Name',
        description='Название груза',
    )
    type = CharField(
        max_length=255,
        verbose_name='Type',
        choices=TYPES,
        default=TYPES[0][0],
        description='Тип посылки'
    )
    weight = FloatField(
        default=0,
        verbose_name='Weight',
    )
    width = FloatField(
        default=0,
        verbose_name='Width',
    )
    length = FloatField(
        default=0,
        verbose_name='Length',
    )
    height = FloatField(
        default=0,
        verbose_name='Heihgt',
    )
    description = TextField(
        max_length=1060,
        blank=True,
        null=True,
        description='Описание груза',
    )
