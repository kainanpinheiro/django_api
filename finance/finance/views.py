from django.http import JsonResponse
from django.views import View
from typing import Any


class BaseView(View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)


class HealthView(BaseView):
    def get(self, request):
        print(request)
        return JsonResponse({'dado': '0.0.1'})
