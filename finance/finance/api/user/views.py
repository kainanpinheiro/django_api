from typing import Any
from django.views import View
from django.http import JsonResponse


class BaseView(View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)


class TesteView(BaseView):
    def get(self, request):
        return JsonResponse({'foo': 1})
