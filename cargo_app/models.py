import random
import re
from datetime import datetime
from barcode import EAN13, Code39
from barcode.writer import ImageWriter


from django.db.models import (
    CharField,
    TextField,
    FloatField,
)

from base.models import AbstractBaseModel
from slavov_backend import settings


class Cargo(AbstractBaseModel):
    id = CharField(
        primary_key=True,
        editable=False,
        max_length=39,
        verbose_name='код накладной',
    )
    weight = FloatField(
        default=0,
        verbose_name='вес',
    )
    width = FloatField(
        default=0,
        verbose_name='ширина',
    )
    length = FloatField(
        default=0,
        verbose_name='длина',
    )
    height = FloatField(
        default=0,
        verbose_name='высота',
    )
    description = TextField(
        max_length=1060,
        blank=True,
        null=True,
        verbose_name='описание',
    )
    from_destination = TextField(verbose_name='откуда')
    to_destination = TextField(verbose_name='куда')

    def save(self, **kwargs):
        """
        Встроенное UUID для пидоров?
        """
        if not self.id:
            currend_index = Cargo.objects.count() + 1
            index_chunk = (10 - len(str(currend_index))) * '0' + str(currend_index)        # l is 10
            datetime_chunk = re.sub(r"\s|-|:|\.", "", str(datetime.now()))                 # l is 20
            random_val = random.randint(int("1" + "0" * 8), int("9" * 9))                  # l is 9
            #                                                                              total l is 39 (zaebis')

            self.id = f"{random_val}{datetime_chunk}{currend_index}"

        super().save(*kwargs)

    @property
    def barcode_uri(self):
        barcode_file = settings.STATICFILES_DIRS[0] / "images" / "barcodes" / f"{str(self.id)}.png"
        if not barcode_file.exists():
            with open(barcode_file.as_posix(), 'wb+') as f:
                Code39(self.id, writer=ImageWriter()).write(f)
        return f"/images/barcodes/{str(self.id)}.png"
