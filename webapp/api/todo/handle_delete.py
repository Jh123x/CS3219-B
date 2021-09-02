import json

from django.http.response import HttpResponseNotFound
from ..models import TodoItems
from .util import wrap_response, get_result_json


def handle_delete(request, id):
    try:
        item = TodoItems.objects.filter(id=id).get()
    except TodoItems.DoesNotExist:
        return wrap_response(json.dumps(get_result_json(False)))
    item.delete()

    return wrap_response(json.dumps(get_result_json(id is not None)))
