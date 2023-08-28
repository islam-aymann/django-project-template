from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone


class APIVersionView(APIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response(
            {
                "version": "1.0.0",
                "status": "stable",
                "release_date": timezone.now(),
                "release_notes": "Initial release",
            }
        )
