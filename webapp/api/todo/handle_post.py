import json

from ..models import TodoItems
from .util import wrap_response, get_result_json



def handle_post(request):
    """Handle post requests"""
    description = request.POST.get('description', None)

    if description is not None:
        new_item = TodoItems(description = description)
        new_item.save()

    return wrap_response(json.dumps(get_result_json(description is not None)))
    