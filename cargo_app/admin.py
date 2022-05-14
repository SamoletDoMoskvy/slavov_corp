from django.contrib.admin import (
    ModelAdmin,
    register,
)
from django_object_actions import DjangoObjectActions

from .models import Cargo


@register(Cargo)
class CargoModelAdmin(DjangoObjectActions, ModelAdmin):
    fields = (
        'weight',
        'width',
        'length',
        'height',
        'description',
        'from_destination',
        'to_destination',
    )
    list_display = (
        'weight',
        'width',
        'length',
        'height',
        'description',
        'from_destination',
        'to_destination',
    )
    ordering = (
        '_created_at',
    )

    def external_link(self, request, obj):
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(f'http://127.0.0.1:8000/api/cargo/get_report/{obj.id}')

    external_link.label = 'К накладной'
    external_link.short_description = 'Перейти на страницу накладной'

    change_actions = (
        'external_link',
    )
