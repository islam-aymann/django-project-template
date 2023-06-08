from django.http import JsonResponse


def index(request):
    return JsonResponse("Hello, world. You're at the polls index.")
