from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Cargo


def get_report(request: HttpRequest, id: int):
    cargo: Cargo = get_object_or_404(Cargo, id=id)
    return render(request=request,
                  template_name="cargo/report.html",
                  context=dict(cargo=cargo),
                  )

