from django.contrib.admin import (
    ModelAdmin,
    register,
)
from django_object_actions import DjangoObjectActions

from .models import Cargo


@register(Cargo)
class CargoModelAdmin(DjangoObjectActions, ModelAdmin):
    fields = (
        'id',
        'weight',
        'width',
        'length',
        'height',
        'description',
        'from_destination',
        'to_destination',
        'price',
        'sender',
        'recipient',
        '_created_at',
        '_updated_at',
    )
    list_display = (
        'id',
        'weight',
        'width',
        'length',
        'height',
        'from_destination',
        'to_destination',
        'price',
        'sender',
        'recipient',
    )
    readonly_fields = (
        'id',
        'price',
        '_created_at',
        '_updated_at',
    )
    ordering = (
        '_created_at',
    )

    def external_link(self, request, obj):
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(f'http://0.0.0.0:80/api/cargo/get_report/{obj.id}')

    external_link.label = 'К накладной'
    external_link.short_description = 'Перейти на страницу накладной'

    change_actions = (
        'external_link',
    )
