import json

from ..models import TodoItems
from django.http.response import HttpResponse


def handle_get(request):
    data = list(map(lambda x: x.to_dict(), TodoItems.objects.all()))
    resp = HttpResponse(json.dumps(data))
    resp.headers['Content-Type'] = "application/json"
    return resp