import json

from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from .todo import handle_get, handle_post, handle_delete, handle_put

# Create your views here.
def index(request):
    """For sanity check"""
    return HttpResponse("<h1>Hello world</h1>")


def todo(request):
    """Create the todo list"""
    methods = {
        "GET": handle_get,
        "POST": handle_post,
        "Default": lambda x: HttpResponseNotAllowed("Method not allowed")
    }
    return methods.get(request.method, methods["Default"])(request)


def update_todo(request, id):
    methods = {
        "DELETE": handle_delete,
        "PUT": handle_put,
        "Default": lambda x: HttpResponseNotAllowed("Method not allowed")
    }

    return methods.get(request.method, methods['Default'])(request, id)