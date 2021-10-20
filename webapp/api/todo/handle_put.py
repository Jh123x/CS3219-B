import json

from django.http.response import Http404, HttpResponseNotFound
from ..models import TodoItems
from .util import wrap_response, get_result_json


def handle_put(request, id):
    """Update item to be completed"""
    try:
        item = TodoItems.objects.filter(id=id).get()
    except TodoItems.DoesNotExist:
        return wrap_response(json.dumps(get_result_json(False)))
    item.is_completed = not item.is_completed
    item.save()

    return wrap_response(json.dumps(get_result_json(item.is_completed)))
